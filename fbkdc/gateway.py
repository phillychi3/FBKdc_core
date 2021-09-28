import websockets
import json
import asyncio
import logging
import sys
import threading
import time
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
        self.allive = True





    async def startlink(self):
        while self.allive:
            async with websockets.connect(self.url) as websocket:


                while True:
                    response = await websocket.recv()

                    response = json.loads(response)
                    print("------------------------------------------------------")
                    print(response)
                    op = response["op"]
                    #data = response.get('d')
                    #seq = response.get('s')

                    if op != self.DISPATCH:


                        if op == self.HEARTBEAT_ACK:
                            print("IS HEARTBEAT_ACK")
                            continue

                        if op == self.HEARTBEAT:
                            print("IS HEARTBEAT")

                            beat =  {
                            'op':self.HEARTBEAT,
                            'd': time.time()
                            }
                            
                            await websocket.send(json.dumps(beat))
                            
                        if op == self.HELLO:
                            print("IS HELLO")
                            beat =  {
                            'op': self.HEARTBEAT,
                            'd': time.time()
                            }
                            await websocket.send(json.dumps(beat))
                            payload = {
                                'op': self.IDENTIFY,
                                'd': {
                                    'token': self.token,
                                    "intents": 513,
                                    'properties': {
                                        '$os': sys.platform,
                                        '$browser': 'FBKdc',
                                        '$device': 'FBKdc',
                                        '$referrer': '',
                                        '$referring_domain': ''
                                    }
                                }
                            }
                            await websocket.send(json.dumps(payload))

                        if op == self.INVALIDATE_SESSION:
                            print("is INVALIDATE_SESSION")
                            self.allive = False
                            await websocket.close()
                            await self.RECONNECT()


    async def RECONNECT(self):
        print("i am here")
        self.allive = True
        await self.startlink()

