from util import hook

import requests, re, random

regex = re.compile(re.escape("cat"), re.IGNORECASE)
kittenrex = re.compile(re.escape("kitten"), re.IGNORECASE)

@hook.regex("PHP sadness$")
def php_fact(inp):
    return "http://phpsadness.com/sad/" + str(random.randint(0,53))

@hook.regex("(.*) fact$")
def printerfact(inp, say=None):
    if len(inp.group(1).split()) != 1:
        return None

    r = requests.get('https://catfacts-api.appspot.com/api/facts?number=1')
    fact = r.json()['facts'][0]
    inp = inp.group(1)
    return kittenrex.sub("baby "+ inp, regex.sub(inp, fact))
