from random import choice
from util import hook

quotes = []

with open("./plugins/data/plinkett.txt", "r") as fin:
    quotes = fin.readlines()

@hook.command
@hook.regex("^plinkett fact$")
def plinkett(inp):
    return choice(quotes)
