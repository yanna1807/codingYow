#9/5/2024
import sys
from time import sleep
import time as ticktack

def forYou():
    lyrics = [
        ("Two old friends", 0.1),
        ("Meet again", 0.2),
        ("Wearin' older faces", 0.1),
        ("...", 0.2),
        ("And talk about the places they've been", 0.1),
        ("...", 0.2),
        ("Two old sweethearts", 0.1),
        ("Who fell apart", 0.2),
        ("Somewhere a long ago", 0.1),
        ("How are they to know", 0.1),
        ("Someday they'd meet again", 0.1),
        ("And have a need for more than reminiscin'", 0.1),
        ("Maybe this time", 0.1),
        ("It'll be lovin' they'll find", 0.1),
        ("Maybe now they can be more than just friends", 0.1),
        ("She's back in his life", 0.1),
        ("And it feels so right", 0.1),
        ("Maybe this time, love won't end", 0.1)
    ]
        
    delays = (0.4, 0.7, 0.5, 0.6, 0.3, 0.6, 0.3, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)

    for him, (line, delay) in enumerate(lyrics):
        for relate in line:
            print(relate, end = "")
            sys.stdout.flush()
            sleep(delay)
        ticktack.sleep(delays[him])
        print("")

forYou()

again = input(str("Do you want to play the second verse of this song: yes/no? "))

def forHim():
    lyrics = [
        ("It's the same old feeling back again", 0.1),
        ("It's the one they had way back when", 0.2),
        ("They were too young to know when love is real", 0.1),
        ("...", 0.2),
        ("But somehow some things never change", 0.1),
        ("And even time hasn't cooled the flame", 0.1),
        ("It's burnin' even brighter than it did before", 0.2),
        ("They got another chance and if they take it", 0.1),
        ("Maybe this time", 0.1),
        ("It'll be lovin' they'll find", 0.1),
        ("Maybe now they can be more than just friends", 0.1),
        ("She's back in his life", 0.1),
        ("And it feels so right", 0.1),
        ("Maybe this time, love won't end", 0.1)
    ]

    delays = (0.4, 0.7, 0.5, 0.6, 0.3, 0.6, 0.3, 0.2, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1, 0.1)

    for thatGuy, (line, delay) in enumerate(lyrics):
        for seym in line:
            print(seym, end = "")
            sys.stdout.flush()
            sleep(delay)
        ticktack.sleep(delays[thatGuy])
        print("")

if again == "yes":
    forHim()
    print("Do you want the bridge? bwahahahaha I'm still working on it")
else:
    print("Try this next time nalang HEHE :)")




