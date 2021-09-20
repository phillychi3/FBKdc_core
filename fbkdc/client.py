"""
這裡放說明拉
"""
import logging 
import asyncio
from .route import *
from .gateway import *
log = logging.getLogger(__name__)



class Clent():


    def __init__(self,token=None):
        self.loop = asyncio.get_event_loop() 
        self.token = token



    async def login(self):
        log.info("login with token")

        await Route().httplogin(self.token)
        
        

    async def connect(self):
        log.info("connect")
        gatewayurl = await Route().getgateway()
        logging.debug(gatewayurl)
        await Clientgateway(self.token,gatewayurl).startlink()



    async def startbot(self):
        log.info("startbot")
        await self.login()
        await self.connect()
        

    def run(self,token):


        loop = self.loop
        self.token = token


        logging.info("run")
        print("run")

        async def runner():
            await self.startbot()
        future = asyncio.ensure_future(runner(), loop=loop)

        try:
            loop.run_forever()
        except KeyboardInterrupt:
            log.info("KeyboardInterrupt failed")