
import requests
import logging
import json

apiurl="https://discord.com/api/v9"
log = logging.getLogger(__name__)

class Route():


    async def http(self,method,url,*args,**kwargs):
        if method=="GET":
            if kwargs.get("TOKEN"):
                re = requests.get(url,headers={"Authorization": "Bot "+kwargs.get("TOKEN")})
            else:
                re = requests.get(url)
            print(re.text)
            return re
        elif method=="POST":
            re = requests.post(url)
            return re
        else:
            log.warning("你麼到這的")
            raise Exception("不支援的method")


    async def httplogin(self,token):
        logging.debug(token)
        await self.http("GET",apiurl+"/users/@me",TOKEN=token)


    async def getgateway(self,encoded="json",v=9):
        get = await self.http("GET",apiurl+"/gateway")
        get = get.json()
        print(get)
        data = f"{get['url']}?encoding={encoded}&v={v}"
        return data
        