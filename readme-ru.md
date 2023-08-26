# midjourney-proxy

## Запуск
### Как отдельный контейнер

1. Прописать конфиг
- Создать папку myconfig в корне проекта.
- Скопировать туда файл по пути src/main/resources/application.yml<br>
(Необязательно) скопировать по этому же пути файл banned-words.txt, если в промпте встретится какое-то слово из списка, запрос не будет выполнен
- Заменить значения guild-id (id сервера), channel-id (id канала в этом сервере), user-token (токен юзера, можно получить по этому [гайду](https://www.howtogeek.com/879956/what-is-a-discord-token-and-how-do-you-get-one/))<br>
Авторы также рекомендуют заменить session-id на свое значение, но вроде работает и так

ИЛИ

Создать файл .env, прописать там переменные окружения MJ_DISCORD_GUILD_ID, MJ_DISCORD_CHANNEL_ID и MJ_DISCORD_USER_TOKEN

2. Сбилдить образ 
```shell
docker build . -t midjourney-proxy
```
3. Запустить контейнер
- Linux:
```shell
docker run -d --name midjourney-proxy -p 8080:8080 -v $(pwd)/myconfig:/home/spring/config midjourney-proxy
```
- Windows (PowerShell):
```shell
docker run -d --name midjourney-proxy -p 8080:8080 -v ${pwd}/myconfig:/home/spring/config midjourney-proxy
```
- Linux или Windows через переменные окружения:
```shell
docker run -d --name midjourney-proxy -p 8080:8080 -e mj.discord.guild-id=${MJ_DISCORD_GUILD_ID} -e mj.discord.channel-id=${MJ_DISCORD_CHANNEL_ID} -e mj.discord.user-token=${MJ_DISCORD_USER_TOKEN} midjourney-proxy
```

### Через docker compose

1. Создать файл .env, прописать там переменные окружения MJ_DISCORD_GUILD_ID, MJ_DISCORD_CHANNEL_ID и MJ_DISCORD_USER_TOKEN

2. Запустить
```shell
docker compose -f docker-compose.yml up
```

## Особенности
Максимум поддерживается 3 джобы (идут параллельно) и 10 запросов в очереди - ограничения midjourney. Если все 3 джобы будут заполнены, то апишка аккумулирует запросы внутри себя, затем по мере освобождения джоб, закидывает промпты из очереди.

Если в промпте встретится слово из забаненных (banned-words.txt), то апишка вернет ответ с `"code": 24`. Если же сам бот миджорни посчитает запрос плохим (например, dead crown), то апишка в информации о таске укажет `"status": "FAILURE"`.

## За что могут забанить
Злоупотребление API REST (недостаточное ожидание между запросами) может привести к блокировке/отключению телефона вашей учетной записи. В идеале постараться вообще не ловить rate limit.

## Команды
Адрес по-умолчанию:
```shell
localhost:8080
```

### Task
Все промежуточные и финальные результаты имеют вид:
| Field | Type | Example | Description |
|:-----:|:----:|:----|:----|
| id | string | 1689231405853400 / Task ID |
| action | string | IMAGINE | Task type: IMAGINE (drawing), UPGRADE (selected to enlarge), VARIATION (selected to transform), REROLL (re-execution), DESCRIBE (graphic text), BLEAND (picture mixing) |
| status | string | SUCCESS | Task status: NOT_START (not started), SUBMITTED (submitted for processing), IN_PROGRESS (in execution), FAILURE (FAILED), SUCCESS (successful) |
| prompt | string | cat cat | prompt word |
| promptEn | string | Cat | English prompt word |
|description | string | /imagine cat / task description |
| submitTime | number | 1689231405854 | Submission time |
| startTime | number | 1689231442755 | Start execution time |
| finishTime | number | 1689231544312 / End time |
| progress | string | 100% / Task progress |
| imageUrl | string | https://cdn.discordapp.com/attachments/xxx/xxx/xxxx.png | The url of the generated image, there is a value when it is successful or executed, it may be png or webp |
|failReason | string | [Invalid parameter] Invalid value | Cause of failure, there is a value when it fails |
| properties | object / {"finalPrompt": "Cat"} / Extended properties of the task, used internally by the system |

### imagine
`/mj/submit/imagine` - генерация изображения
```json
{
    "base64Array": ["<image>", ...],
    "prompt": "<prompt>",
    "notifyHook": "<webhook>",
    "state": "<state>"
}
```
- `<image>` - (необязательно) изображение в base64 формате, но перед base64 строкой инфа об изображении data uri, например `data:image/png;base64,`<br>
- `<prompt>` - текстовый промпт<br>
- `<notifyHook>` - (необязательно) адрес вебхука, туда будут отправляться сообщения о готовности изображения
- `<state>` - (необязательно) пользовательские параметры (?)

1. запрос был принят:
```json
"status": "SUBMITTED"
```
2. изображение в процессе генерации:
```json
"status": "IN_PROGRESS"
```
поле imageUrl может быть null

3. изображение было сгенерировано:
```json
"status": "SUCCESS"
```

### change
`/mj/submit/change`<br>
или `/mj/submit/change-simple`<br>
для выполнения действий UPSCALE, VARIATION и REROLL

`/mj/submit/change`
```json
{
  "action": "<action>",
  "index": <index>,
  "notifyHook": "<webhook>",
  "state": "<state>",
  "taskId": "<task_id>"
}
```
- `<action>` - одно из значений: UPSCALE, VARIATION или REROLL
- `<index>` - если action UPSCALE или VARIATION, то index это номер изображения
- `<webhook>` - (необязательно) адрес вебхука, туда будут отправляться сообщения о готовности изображения
- `<state>` - (необязательно) пользовательские параметры (?)
- `<task_id>` - номер таски, в процессе которого было создано изображение (возвращается как ответ на любой из запросов imagine либо change VARIATION)

`/mj/submit/change-simple`
делает то же самое, что и `/mj/submit/change`, но запросы делаются по-другому
```json
{
  "content": "<task_id> <simple-action><index>",
  "notifyHook": "<webhook>",
  "state": "<state>"
}
```
- `<simple-action>` - U для UPSCALE, V для VARIATION