import os

from util import hook

@hook.command
def source(inp):
    if inp == "pull":
        os.system("git pull")
        return "updating..."
    return "my source code: https://git.xeserv.us/xena/h"
