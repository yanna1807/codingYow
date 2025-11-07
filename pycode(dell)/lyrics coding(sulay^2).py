#8/24/2024
#dili ni akoa nga code hehe sulay^2 lng..
import sys
from time import sleep
import time

def print_lyrics():
    lines = [
        ("This was the very first page", 0.1), 
        ("Not where the storyline ends", 0.1),
        ("My thoughts will echo your name", 0.1),
        ("Until I see you again", 0.1),
        ("These are the words I held back", 0.1),
        ("As I was leaving too soon", 0.1),
        ("I was enchanted to meet you", 0.1),
        ("Please, don't be in love with someone else", 0.1),
        ("Please, don't have somebody waiting on you...", 0.2)
    ]

    delays = (0.2, 0.3, 0.3, 0.3, 0.2, 0.2, 0.1, 0.3, 0.2)
    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            print(char, end = "")
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print("")

print_lyrics()
    