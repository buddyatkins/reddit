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

# r.send_message("diablo3xboxonemodbot","Test message","Just testing yo")

pms = r.get_unread(unset_has_mail=True, update_user=True)
i = 0
runFaF = False
for pm in pms:
    print("\nMessage %d"%i)
    pprint(vars(pm))
    i += 1
    try:
        if pm.link_title == "Find a Friend: Even Newer and More Official":
            runFaF = True
    except:
        pass
    pm.mark_as_read()
if runFaF = True:
    updateFaFList(r)
