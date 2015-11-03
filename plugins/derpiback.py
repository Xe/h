from util import hook

import requests

@hook.command
def derpiback(pls):
    r = requests.get("https://derpibooru.org")
    if "J6-eVNTVvMk" in r.text:
        return "nope derpibooru is still down for maintenance, at soonest it will be tomorrow"

    return "yep"
