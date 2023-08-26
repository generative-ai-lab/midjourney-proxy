# # SCRIPT TAKEN FROM "https://github.com/Monst3red/Discord-Token-Login-Tool"

import logging
import os

logging.basicConfig(filename='/home/midjourney-authorization/logs/logs.log',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

logging.info("Logger initialized")

token = os.getenv("MJ_DISCORD_USER_TOKEN")
user_agent = os.getenv("USER_AGENT")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

logging.info("Webdriver downloaded")

options = Options()
options.add_argument('--headless')
options.add_argument(f'--user-agent={user_agent}')

script = '''
    const login = (token) => {
        setInterval(() => document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`, 100);
        setTimeout(() => location.reload(), 2500);
    };''' + f'login("{token}")' # adapted from "https://gist.github.com/m-Phoenix852/b47fffb0fd579bc210420cedbda30b61"

logging.info("Trying to login in discord")

driver = webdriver.Chrome(options=options)
driver.get("https://discord.com/login")
driver.execute_script(script)

logging.info('Successful logging')