import websockets
import json
import asyncio
import logging
import sys

logger = logging.getLogger(__name__)
webs = websockets

class Clientgateway():



    DISPATCH           = 0
    HEARTBEAT          = 1
    IDENTIFY           = 2
    PRESENCE           = 3
    VOICE_STATE        = 4
    VOICE_PING         = 5
    RESUME             = 6
    RECONNECT          = 7
    REQUEST_MEMBERS    = 8
    INVALIDATE_SESSION = 9
    HELLO              = 10
    HEARTBEAT_ACK      = 11
    GUILD_SYNC         = 12


    def __init__(self, token,url):
        self.token = token
        self.url = url

    async def receive(self,response):
        logger.debug(response)




    async def send(self,url,payload):
        print(url)
        print(payload)
        async with websockets.connect(url) as websocket:
            await websocket.send(json.dumps(payload))

            response = await websocket.recv()
            logger.debug(response)





    async def clientgate(self):


        logger.info("Connecting to gateway")

        await self.identity()



    async def identity(self):
        payload = {
            'op': self.IDENTIFY,
            'd': {
                'token': self.token,
                'properties': {
                    '$os': sys.platform,
                    '$browser': 'FBKdc',
                    '$device': 'FBKdc',
                    '$referrer': '',
                    '$referring_domain': ''
                },
                'compress': True,
                'large_threshold': 250,
                'v': 3
            }
        }
        await self.send(self.url,payload)