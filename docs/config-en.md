## Configuration item

| Variable name | Non-empty | Description |
| :-----| :----: | :---- |
| mj.discord.guild-id / Yes | discord server ID |
| mj.discord.channel-id / Yes | discord channel ID |
| mj.discord.user-token / Yes / discord user Token |
| mj.discord.session-id / no | discord user SessionID, it is recommended to copy and replace it from the interactions request |
| mj.discord.user-agent / No | The user-agent when calling the discord interface and connecting to wss, it is recommended to copy from the browser network |
| mj.api-secret / No / Interface key, empty does not enable authentication; when calling the interface, you need to add the request header mj-api-secret |
| mj.notify-hook | no | Global task status change callback address |
| mj.notify-notify-pool-size / no | Notify the callback thread pool size, the default is 10 |
| mj.task-store.type / No / task storage method, default in_memory (memory \ lost after restart), optional redis |
| mj.task-store.timeout | No | Task expiration time, delete after expiration, default 30 days |
| mj.queue.core-size | no | number of concurrency, the default is 3 |
| mj.queue.queue-size | No | Waiting queue, default length 10 |
| mj.queue.timeout-minutes / No | Task timeout, the default is 5 minutes |
| mj.proxy.host / no | Proxy host, set when the global proxy does not take effect |
| mj.proxy.port / No | Proxy port, set when the global proxy does not take effect |
|mj.ng-discord.server |No / https://discord.com Reverse address |
| mj.ng-discord.cdn |No / https://cdn.discordapp.com Reverse address |
|mj.ng-discord.wss/No/wss://gateway.discord.gg reverse address|
| mj.translate-way / no |The way to translate Chinese prompt into English, you can choose null (default), baidu, gpt |
| mj.baidu-translate.appid / No | appid translated by Baidu /
| mj.baidu-translate.app-secret / no | Baidu translated app-secret |
| mj.openai.gpt-api-url / no | Customize the interface address of gpt, no configuration is required by default |
| mj.openai.gpt-api-key /No | gpt's api-key |
| mj.openai.timeout | No | The timeout for openai calls, the default is 30 seconds |
| mj.openai.model /no |openai model, default gpt-3.5-turbo |
| mj.openai.max-tokens | No | Returns the maximum number of words in the result, the default is 2048 |
| mj.openai.temperature | No | similarity (0-2.0), default 0 |
| spring.redis / No | The task storage method is set to redis, you need to configure redis-related properties |

### spring.redis configuration reference
```yaml
spring:
redis:
host: 10.107.xxx.xxx
port: 6379
password: xxx
```