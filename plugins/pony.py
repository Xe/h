from util import hook
from ddate.base import DDate

import datetime
import ponyapi

def get_time(ep):
    now = datetime.datetime(2006, 1, 1)
    now = now.now()
    then = now.fromtimestamp(int(ep[u"air_date"]))
    td = then-now

    return now, then, td

@hook.command
def when(inp, say=None):
    #"Shows the countdown to the new episode of My Little Pony: Friendship is Magic!"

    ep = ponyapi.newest()
    now, then, td = get_time(ep)
    seasonep = ""

    if inp == "discord":
        return "%s will air on %s" % (ep[u"name"], DDate(then))

    if ep[u"is_movie"]:
        seasonep = "(a movie)"
    else:
        seasonep = "(season %d episode %d)" % (ep[u"season"], ep[u"episode"])

    reply = "%s %s will air on %s in %d days!" % (
                ep[u"name"], seasonep, then.strftime("%a, %d %b %Y %H:%M:%S"),
                td.days)

    return reply

@hook.command
def randomep(inp):
    #"Shows a random episode of My Little Pony: Friendship is Magic"
    ep = ponyapi.random()

    seasonep = ""

    if ep[u"is_movie"]:
        seasonep = "(a movie)"
    else:
        seasonep = "(season %d episode %d)" % (ep[u"season"], ep[u"episode"])

    return "%s %s" % (ep[u"name"], seasonep)
