from util import hook

import requests, re, random

regex = re.compile(re.escape("cat"), re.IGNORECASE)
kittenrex = re.compile(re.escape("kitten"), re.IGNORECASE)
preggorex = re.compile(re.escape("pregmant"), re.IGNORECASE)

@hook.regex("PHP sadness$")
def php_fact(inp):
    return "http://phpsadness.com/sad/" + str(random.randint(0,53))

@hook.regex("^printer fact$")
@hook.command
def printerfact(inp, say=None):
    r = requests.get('https://catfacts-api.appspot.com/api/facts?number=1')
    fact = r.json()['facts'][0]
    inp = "printer"
    return kittenrex.sub("baby "+ inp, regex.sub(inp, fact))
