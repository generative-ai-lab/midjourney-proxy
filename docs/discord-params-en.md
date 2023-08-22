## Get discord configuration parameters

### 1. Get user token
Enter the channel, open the network, refresh the page, and find the request for 'messages`. The authorization here is the user token, and then set it to`mj.discord.user-token`

![User Token](img_8.png)

### 2. Get user SessionID
Enter the channel, open the network, send the/imagine drawing command, and find the request for 'interactions`. The session_id here is the user's SessionID, and then set it to`mj.discord.session-id`

![User Session](params_session_id.png)

### 3. Get server ID and channel ID

Take out the server ID and channel ID from the url of the channel, and then set it to the configuration item
![Guild Channel ID](img_9.png)