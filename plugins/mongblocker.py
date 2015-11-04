from util import hook

@hook.regex("\x07")
def kickbell(line, input=None, conn=None):
    conn.msg("ChanServ", "KICK " + input.params.split()[0] + " " + input.nick + " You have won the no-bell peace prize")
    input.notice("Please do not send the bell character to " + input.params.split()[0] + ". You have just disrupted the experience for a lot of people.")
