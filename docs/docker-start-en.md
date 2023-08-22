## Docker Deployment tutorial

1. Create application in the/xxx/xxx/config directory.yml (mj configuration item), banned-words.txt (optional, overwriting the default sensitive word file); refer to the file under src/main/resources
2. Start the container and map the config directory
```shell
docker run -d --name midjourney-proxy \
-p 8080:8080 \
-v /xxx/xxx/config:/home/spring/config \
novicezk/midjourney-proxy:2.4
```
3. Access`http://ip:port/mj 'View API documentation

Attachment: Do not map the config directory method, set the parameters directly in the startup command
```shell
docker run -d --name midjourney-proxy \
-p 8080:8080 \
-e mj.discord.guild-id=xxx \
-e mj.discord.channel-id=xxx \
-e mj.discord.user-token=xxx \
novicezk/midjourney-proxy:2.4
```