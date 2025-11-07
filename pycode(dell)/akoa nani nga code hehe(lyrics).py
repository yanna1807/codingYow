#8/24/2024 and 8/25/2024 - 8/31/2024(my_own_code)
import sys
from time import sleep
import time as t

def bored():
    lyrics = [
        ("Full moon, bedroom, stars in your eyes", 0.1),
        ("Last night, the first time that I realized", 0.1),
        ("The glow between us", 0.2),
        ("felt so right", 0.3),
        ("We sat on the edge of the bed", 0.1),
        ("and you said", 0.1),
        ("I never knew that I could feel this way", 0.1),
        ("Love today", 0.1),
        ("can be", 0.1),
        ("so difficult", 0.1),
        ("But what we have", 0.0),
        ("I know", 0.1),
        ("is different", 0.1),
        ("'Cause when", 0.0),
        ("I'm with you,", 0.1),
        ("the world stops", 0.0),
        ("turning", 0.2),
        ("Could I love you any more?", 0.1),
        (".....", 0.3),
        ("Could I love you any more?", 0.1),
        (".....", 0.1),
        ("Could I love you any more?", 0.1),
        ("......", 0.2),
        ("Sunrise, time flies, feels like a dream", 0.1),
        ("Being close inhaling hard to believe", 0.1),
        (".....", 0.1),
        ("Seven billion people", 0.1),
        ("in the world", 0.0),
        ("Finding you", 0.1),
        ("is like", 0.1),
        ("a miracle", 0.1),
        ("Only this wonder remains", 0.1),
        (".....", 0.2),
        ("Could I love you any more?", 0.1),
        ("....", 0.2),
        ("Could I love you any more?", 0.1),
        ("....", 0.2),
        ("Could I love you any more?...", 0.1)
    ]
    delays = (0.1, 0.1, 0.8, 0.5, 0.8, 0.4, 0.3, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.1, 0.9, 0.0, 0.7, 0.0, 0.9, 0.8, 0.2, 0.4, 0.2, 0.1, 0.2, 0.0, 0.0, 0.0, 
              0.2, 0.2, 0.9, 0.1, 0.9, 0.1, 0.7, 0.1, 0.1)
    
    for m, (line, lah_delay) in enumerate(lyrics):
        for lah in line:
            print(lah, end = "")
            sys.stdout.flush()
            sleep(lah_delay)
        t.sleep(delays[m])
        print("")

bored()

try_again = str(input("Do you want to play again: y/n? "))
if try_again == 'y':
    bored()
    chances = 0
    while chances <= 0:
        bored()
        chances += 1
    else: 
        print("That's all lang po hehe :)")
else:
    print("Okay! Bye :)")
