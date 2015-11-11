from util import hook
from random import choice
from data.bobross import quotes

@hook.regex("^[Bb]ob [Rr]oss fact$")
@hook.command
def bobross(inp):
    return choice(quotes)
