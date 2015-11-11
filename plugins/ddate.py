from util import hook
from ddate.base import DDate

import datetime

@hook.command
def ddate(inp):
    return str(DDate())
