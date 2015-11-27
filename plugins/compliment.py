import re
import requests
from util import hook

@hook.command
@hook.regex("^feel good fact$", re.IGNORECASE)
def compliment(inp):
    r = requests.get("http://compliment.b303.me/")
    return r.text
