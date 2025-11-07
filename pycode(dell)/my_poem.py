import sys
from time import sleep
import time as stopper

def my_poem():
    hehe = [
        ("I made this poem for him since this was the day (September 14,2024), I liked him very much to the point that I only think of him alone..:))", 0.1),
        ("It begins with...", 0.1),
        ("\nI never knew that my feelings would bloom again,", 0.1),
        ("I thought I'll stop liking someone but you showed up.", 0.1),
        ("You made my heart change my mind by letting you in,", 0.1),
        ("When I'm with you, I felt like I am at the top.", 0.1),

        ("\nYour brown eyes lit up when we looked at each other,", 0.1),
        ("Consequently, I must stop myself from falling.", 0.1),
        ("It's hard to fall for you for you have a partner,", 0.1),
        ("It's even harder to not fall for who you are.", 0.1),

        ("\nI particularly like your personality,", 0.1),
        ("Thus, I only admire you just like crescent moon.", 0.1),
        ("Every night, I always seek the half moon that's bright,", 0.1),
        ("Since, I'm not into stars for it's just too many.", 0.1),
        
        ("\nI only want to admire you from afar boy,", 0.1),
        ("Even though some people already notices it.", 0.1),
        ("One thing I knew is you already replaced him,", 0.1),
        ("I thought it's still him but it's already you guy.", 0.1),

        ("\nThis poem entitled 'Realizations' and there's a reason for that and I won't disclose it hehe...remain mysterious lang ang peg beh char :)", 0.1)
    ]

    delays = (0,1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
             
    for only_him, (line, delay) in enumerate(hehe):
        for okay in line:
            print(okay, end= "")
            sys.stdout.flush()
            sleep(delay)
        stopper.sleep(delays[only_him])
        print("")

my_poem()

def my_poem2():
    for_him = [
        ("\nThere's another poem that I made a few days ago (October 5, 2024) because of boredom or maybe I was thinking of someone that time :)", 0.1),
        ("It starts with:", 0.1),
        ("\nIf only you knew,", 0.1),
        ("The truth aren't revealed.", 0.1),
        ("Might be old or new,", 0.1),
        ("Should remain unfold.", 0.1),

        ("\nIf this goes on then,", 0.1),
        ("We will just let go.", 0.1),
        ("But if fate goes in,", 0.1),
        ("Then the don't must do.", 0.1),
        
        ("\nThe title of this poem is the 'Hidden Truth or So' MWEHE :)", 0.1)
    ]

    delay = (0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1)
    for myOldFriend, (line, delays) in enumerate(for_him):
        for strangersAgain in line:
            print(strangersAgain, end = '')
            sys.stdout.flush()
            sleep(delays) 
        stopper.sleep(delay[myOldFriend])
        print(" ")

my_poem2()

def my_poem3():
    noisesHuhu = [
        ("\nA third one, I made this poem on October 9, 2024 entitled 'Overwhelm' because of noise bwhahahahah lol", 0.1),
        ("Violins I hear,", 0.1),
        ("Noises from my ear.", 0.1),
        ("Busy everywhere,", 0.1),
        ("And I was so near.", 0.1),

        ("\nThe peace I won't feel,", 0.1),
        ("Makes me want to flee.", 0.1),
        ("A way if I will,", 0.1),
        ("Yet I want to lay", 0.1)
    ]

    for line, delay in noisesHuhu:
        for char in line:
            print(char, end='')
            sys.stdout.flush()
            sleep(delay)  
        stopper.sleep(delay)  
        print(" ")  

my_poem3()




    



