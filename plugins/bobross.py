from util import hook
from random import choice

import json

quotes = []

with open("./plugins/data/bobross.json", "r") as fin:
    print fin
    quotes = json.load(fin)

@hook.regex("^[Bb]ob [Rr]oss fact$")
@hook.command
def bobross(inp):
    return choice(quotes)
