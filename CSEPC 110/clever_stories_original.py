"""
Explaining the creative part:

1 - I decided to include an introduction to the game.
"""

#introduction
print("""Welcome to Mad Libs - A word game that consists of one player prompting others for a list of words to 
substitute for blanks in a story before reading aloud""")

#resquest
print("\nNow, you will be asked to input a adjective, animal, verb, exclamation word:")
adjective = input("Write one adjective: ")
animal = input("Write one animal: ")
first_verb = input("Write the first one verb: ")
exclamation = input("Write one exclamation: ")
second_verb = input("Write the second one verb: ")
third_verb = input("Write the third one verb: ")

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

print(f"""
The other day, I was really in trouble. It all started when I saw a very
{adjective} {animal} {first_verb} down the hallway. "{exclamation_capitalized}!" I yelled. But all
I could think to do was to {second_verb} over and over. Miraculously,
that caused it to stop, but not before it tried to {third_verb}
right in front of my family.
""")