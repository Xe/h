from util import hook

import requests

@hook.command
def minecraft(pls):
    r = requests.get("http://xeserv.us/api/minecraft.json")

    data = r.json()

    if not data["online"]:
        return "fluttershy.yochat.biz is down, oh noes"

    if data["players"] == None:
        return "fluttershy.yochat.biz has no online players"

    return "fluttershy.yochat.biz has the following players: " + " ".join(data["players"]) 

@hook.command
def tf2(pls):
    pass
