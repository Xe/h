import re

from util import hook

@hook.command(autohelp=False)
def help(inp, bot=None, pm=None):
    ".help [command] -- gives a list of commands/help for a command"

    pm("Lol, you think there's help. How cute.")
