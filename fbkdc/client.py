"""
這裡放說明拉
"""
import logging 
import asyncio
from .route import *

log = logging.getLogger(__name__)



class Clent():


    def __init__(self):
        self.loop = asyncio.get_event_loop() 




    async def login(self,token):
        log.info("login with token")
        print(token)
        await Route().httplogin(token)

    async def connect(self):
        log.info("connect")

    async def startbot(self,token):
        log.info("startbot")
        await self.login(token)
        

    def run(self,token):


        loop = self.loop


        logging.info("run")
        print("run")

        async def runner():
            await self.startbot(token)
        future = asyncio.ensure_future(runner(), loop=loop)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            log.info("failed")