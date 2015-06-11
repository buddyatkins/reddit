__author__ = 'buddyatkins'

import praw
import time
import traceback
from pprint import pprint
import datetime
import time
from D3XB1ModBot.scripts import updateFaFList




print('Logging in')
r = praw.Reddit("/r/Diablo3XboxOne Moderator")
r.login("Diablo3XBoxOneModBot", "diablo")
already_done = []
print('Logged in')

###Find a Friend update###
updateFaFList(r)


