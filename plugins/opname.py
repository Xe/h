from random import choice
from random import randint
from util import hook

prefix = []
suffix = []

#Read prefix and suffix lines in
with open("./plugins/data/opname_prefix.txt", 'r') as prefixfile:
    prefix = prefixfile.readlines()
with open("./plugins/data/opname_suffix.txt", 'r') as suffixfile:
    suffix = suffixfile.readlines()

#Strip lines and prune junk lines
for ix in [prefix, suffix]:
    for junk in range(len(ix)-1, -1, -1):
        ix[junk] = ix[junk].strip()

@hook.command
def opname(inp):
    #Create phrase
    phrase = "OPERATION %s %s %s" % \
                (choice(prefix), choice(prefix), choice(suffix))

    return phrase.upper()

