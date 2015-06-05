__author__ = 'buddyatkins'

import praw
import time
import traceback
from pprint import pprint


SUBREDDIT = "Diablo3XboxOne"
#This is the sub or list of subs to scan for new posts.
#For a single sub, use "sub1".
#For multiple subreddits, use "sub1+sub2+sub3"
WAIT = 30
#The number of seconds between cycles. Bot is completely inactive during
#this time.

print('Logging in')
r = praw.Reddit("/r/Diablo3XboxOne Moderator")
r.login("Diablo3XBoxOneModBot", "diablo")
