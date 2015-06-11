__author__ = 'buddyatkins'

import praw
import time
import traceback
from pprint import pprint
import datetime
import time

def updateFaFList(r):
    #get Find a Friend info and split out text
    faf = r.get_submission(url='http://www.reddit.com/r/Diablo3XboxOne/comments/397h7e/find_a_friend_even_newer_and_more_official/', comment_sort='new')
    postTextSplit = faf.selftext.split('\n')
    print("Retrieved Find a Friend post")


    #list of all gamer tags already in the list
    GTList = []
    for entry in postTextSplit[10:]:
        GTList.append(entry.split(" | ")[0])

    #Build list of new submissions
    entryList = []
    GTDropList = []
    count = 0
    print("Processing comments")
    for comment in faf.comments:
        fullStop = False
        fullContinue = True
        #if older than initiation then kill loop!! We done son!
        if comment.created_utc < 1433874168:
            print("Reached the designated beginning")
            break
        #if already replied to kill the loop!!
        for reply in comment._replies:
            if reply.body == 'Added to the list' or "INVALID" in reply.body.upper():
                print("Reached comments already processed")
                fullStop = True
                break
        if fullStop == True:
            break

        #Split up the reply
        if "\n" in comment.body:
            replyBodySplit = comment.body.split("\n")
        else:
            print("--Found comment with invalid formatting")
            comment.reply("Invalid formatting: Please use carriage returns to separate categories. Resubmit a new top level comment with updated formatting to be added to the list.")
            continue

        #Set defaults
        GT = "-"
        Class = "-"
        classList = []
        Paragon = "-"
        Style = "-"
        Legit = "-"
        Location = "[Link]"
        Other = "-"
        Permalink = None

        #Fill in attributes
        for item in replyBodySplit:
            if "GT" in item.upper():
                GT = item.split(":")[1].strip()
            if "PARAGON" in item.upper():
                Paragon = item.split(":")[1].strip()
            if "STYLE" in item.upper():
                if "SOFT" in item.split(":")[1].strip().upper():
                    Style = "Softcore"
                if "HARD" in item.split(":")[1].strip().upper():
                    Style = "Hardcore"
            if "LOCATION" in item.upper():
                Location = item.split(":")[1].strip()
            if "OTHER" in item.upper():
                Other = item.split(":")[1].strip()
            if "CLASS" in item.upper():
                if "WIZ" in item.split(":")[1].strip().upper():
                    classList.append("Wizard")
                if "BARB" in item.split(":")[1].strip().upper():
                    classList.append("Barb")
                if "CRU" in item.split(":")[1].strip().upper() or "SADER" in item.split(":")[1].strip().upper():
                    classList.append("Crusader")
                if "WD" in item.split(":")[1].strip().upper() or "WITCH" in item.split(":")[1].strip().upper():
                    classList.append("WD")
                if "DH" in item.split(":")[1].strip().upper() or "DEMON" in item.split(":")[1].strip().upper():
                    classList.append("DH")
                if "MONK" in item.split(":")[1].strip().upper():
                    classList.append("Monk")
                print(item.split(":")[1].strip().upper())
                if "ANY" in item.split(":")[1].strip().upper() or "ALL" in item.split(":")[1].strip().upper():
                    classList = ["All"]
                Class = "/".join(classList)
            if "LEGIT" in item.upper():
                if "NO" in item.split(":")[1].strip().upper():
                    Legit = "Not Legit"
                elif "YES" in item.split(":")[1].strip().upper():
                    Legit = "Legit"
                elif "LEGIT" in item.split(":")[1].strip().upper():
                    Legit = "Legit"
                elif "YEP" in item.split(":")[1].strip().upper():
                    Legit = "Legit"
                elif "HACK" in item.split(":")[1].strip().upper():
                    Legit = "Not Legit"

        if Location == "[Link]":
            Location = Location + "(" + comment.permalink + ")"
        else:
            Location = "["+Location+"]"+ "(" + comment.permalink + ")"

        if GT in GTList:
            GTDropList.append(GT)
            print("--Found an update")
        if GT == "-":
            comment.reply("Invalid gamer tag. Please fix your reply and respond with a new top level comment to be added to the list.")
            print("--Found an invalid comment")
            continue
        Date = time.strftime("%d/%m/%Y")

        #Build Entry
        Entry = " | ".join([GT,Class, Paragon, Style, Legit, Location, Date])
        entryList.append(Entry)
        comment.reply("Added to the list")
        count += 1
        print("Processed %d new entry" % count)

    if len(GTDropList) > 0:
        print("Removing updated entries")
        for i in range(len(GTDropList)):
            for j, row in enumerate(postTextSplit):
                if GTDropList[i] in row:
                    del postTextSplit[j]
                    print("Dropped %s from list" % GTDropList[i])

    print("Adding entries to the list")
    postTextSplitUpdated = postTextSplit[:22]
    postTextSplitUpdated.extend(entryList)
    postTextSplitUpdated.extend(postTextSplit[22:])
    postTextUpdated = "\n".join(postTextSplitUpdated)
    print("Updating post table")
    faf.edit(postTextUpdated)
    print("Update complete")

# GTDropList = ['drop1','drop2']
# postTextSplit = ['drop1 and this','some example','drop2 and stuff','other junk','other nunk']
# for i in range(len(GTDropList)):
#     for j,row in enumerate(postTextSplit):
#         if GTDropList[i] in row:
#             del postTextSplit[j]
# print(postTextSplit)