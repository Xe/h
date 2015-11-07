from util import hook

@hook.regex("thanks mr skeltal")
def skeltal(_):
    return "https://www.youtube.com/watch?v=10pqeNBg5d0"

@hook.regex(r"^([hH])$")
def h(inp, channel=None, conn=None):
    return inp.group(1)

@hook.regex("dQw4w9WgXcQ")
def rickrollProtector(inp):
    return "linked a rick roll, watch out"

@hook.regex("[kK]-[lL]ine")
def kline(inp):
    return "http://i.imgur.com/FQjQgyB.jpg"

@hook.command
def botsnack(inp):
    return ":D"
