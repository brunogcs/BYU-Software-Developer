"""
Explaining the creative part:

1 - I decided to include an introduction to the game.
2 - I created game modes, the first one has the main history, the second one has three random histories 
selected by the software
"""

import random

#1 - introduction
print("""Welcome to Mad Libs - A word game that consists of one player prompting others for a list of words to 
substitute for blanks in a story before reading aloud""")

#Choose random or the main history
print("""\nWe have two game modes: the first mode follows the main story, while the second mode selects a random 
story from our database.\n""")

history_choose = input("Please enter '1' to choose the main story or '2' to select a random story: ")

#resquest
print("\nNow, please provide the following words: an adjective, an animal, three verbs, and an exclamation.")
adjective   = input("Write one adjective: ")
animal      = input("Write one animal: ")
first_verb  = input("Write the first one verb: ")
exclamation = input("Write one exclamation: ")
second_verb = input("Write the second one verb: ")
third_verb  = input("Write the third one verb: ")

"""
adjective: happy
animal: zebra
verb: sneeze
exclamation: hooray
verb: read
verb: drive
"""

#format
exclamation_capitalized = exclamation.capitalize()

if history_choose == "1":
    print(f"""
    The other day, I was really in trouble. It all started when I saw a very
    {adjective} {animal} {first_verb} down the hallway. "{exclamation_capitalized}!" I yelled. But all
    I could think to do was to {second_verb} over and over. Miraculously,
    that caused it to stop, but not before it tried to {third_verb}
    right in front of my family.
    """)
    exit()

#2 - Select Random History

random_number = random.randint(1, 3)

if history_choose == "2" and random_number == 1:

    print(f"""
    Last weekend, I went to the park and encountered a very
    {adjective} {animal} that started to {first_verb} in front of me. 
    "{exclamation_capitalized}!" I shouted in surprise. I quickly decided to 
    {second_verb} to get away from it. To my amazement, that made it 
    {third_verb} right in front of all the other visitors.
    """)

if history_choose == "2" and random_number == 2:

    print(f"""
    One evening, I was watching TV when I noticed a very
    {adjective} {animal} {first_verb} across my living room. 
    "{exclamation_capitalized}!" I exclaimed, startled. I thought I should 
    {second_verb} to distract it. Surprisingly, that made it 
    {third_verb} just as my friends walked in.
    """)

if history_choose == "2" and random_number == 3:

    print(f"""
    During my vacation, I found myself in a strange situation when a very
    {adjective} {animal} began to {first_verb} on the beach. 
    "{exclamation_capitalized}!" I cried out, trying to get everyone's attention. 
    I instinctively started to {second_verb} to make it go away. 
    To my shock, it then decided to {third_verb} right in front of the crowd.
    """)