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


faf = r.get_submission(
    url='http://www.reddit.com/r/Diablo3XboxOne/comments/397h7e/find_a_friend_even_newer_and_more_official/',
    comment_sort='new')
postTextSplit = faf.selftext.split('\n')
print("Retrieved Find a Friend post")

import datetime

for i, row in enumerate(postTextSplit):
    if ":--|" in row:
        listStart = i+1
        break
for row in postTextSplit[listStart:]:
    rowSplit = row.split(" | ")
    GT = rowSplit[0]
    date = datetime.strptime(rowSplit[-1],'%m/%d/%Y')
    if date < datetime.time

        lastMonth = first - datetime.timedelta(days=1)

        print(datetime.date.today())
        print(datetime.date.today() - datetime.timedelta(weeks=4))
