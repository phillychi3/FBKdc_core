
import requests
import logging


apiurl="https://discord.com/api/v9"
log = logging.getLogger(__name__)

class route():


    def http(self,method,url,*args,**kwargs):
        if method=="GET":
            if kwargs.get("TOKEN"):
                re = requests.get(url,headers={"Authorization": "Bot "+kwargs.get("TOKEN")})
            else:
                re = requests.get(url)
            return re
        elif method=="POST":
            re = requests.post(url)
            return re
        else:
            log.warning("你麼到這的")


    async def login(self,TOKEN):
        await self.http("GET",apiurl+"/auth/login",TOKEN)
