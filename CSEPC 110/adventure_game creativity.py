print("Welcome to Butterflies and Dogs, the text RPG history game that will blow your mind.")
print("The game gives you choices and consequences, so choose wisely.")
print("The game will provide you with two or three options, and depending on what you choose, you can win or lose the game.")

def part1():
    story_part1 = input("""You find yourself at the edge of an enchanted forest, known for its magical 
creatures and hidden treasures. As you stand there, you feel a mix of excitement and apprehension.\n
CHOICE 1:

ENTER THE FOREST
TURN BACK AND HEAD HOME
Choose ENTER THE FOREST or TURN BACK AND HEAD HOME: """).strip().upper()
    
    if story_part1 == "ENTER THE FOREST" or story_part1 == "TURN BACK AND HEAD HOME":
        return story_part1
    else:
        print("Invalid choice. Please choose a valid option.")
        return part1()  # Retry the input

def part2(story_part1):
    if story_part1 == "ENTER THE FOREST":  # Enter the forest.
        story_part2 = input("""\nYou step into the cool shade of the trees. The air is filled with the sound of rustling leaves and distant animal calls.

CHOICE 2:

FOLLOW THE SOUND OF A BUBBLING BROOK
INVESTIGATE A STRANGE GLOWING LIGHT
Choose FOLLOW THE SOUND OF A BUBBLING BROOK or INVESTIGATE A STRANGE GLOWING LIGHT: """).strip().upper()
        
        if story_part2 not in ["FOLLOW THE SOUND OF A BUBBLING BROOK", "INVESTIGATE A STRANGE GLOWING LIGHT"]:
            print("Invalid choice. Please choose a valid option.")
            return part2(story_part1)  # Retry the input

    elif story_part1 == "TURN BACK AND HEAD HOME":  # Turn back and head home.
        story_part2 = input("""\nYou retrace your steps, feeling a sense of relief as you leave the forest behind. However, as you walk, you notice a shadowy figure watching you from the treeline.
CHOICE 2:

CONFRONT THE SHADOWY FIGURE
QUICKEN YOUR PACE AND IGNORE IT
Choose CONFRONT THE SHADOWY FIGURE or QUICKEN YOUR PACE AND IGNORE IT: 
""").strip().upper()
        
        if story_part2 not in ["CONFRONT THE SHADOWY FIGURE", "QUICKEN YOUR PACE AND IGNORE IT"]:
            print("Invalid choice. Please choose a valid option.")
            return part2(story_part1)  # Retry the input

    return story_part2

def part3(story_part1, story_part2):
    if story_part1 == "ENTER THE FOREST":  # Enter the forest
        if story_part2 == "FOLLOW THE SOUND OF A BUBBLING BROOK":  # Follow the sound of a bubbling brook
            while True:
                story_part3 = input("""\nYou make your way through the underbrush, the sound of the bubbling brook growing louder with each step. As you approach, you see the water glistening in the dappled sunlight. The brook is surrounded by vibrant wildflowers and smooth stones.

CHOICE 3:

SIT BY THE BROOK
LOOK FOR FISH OR OTHER WILDLIFE
FOLLOW THE BROOK UPSTREAM
Choose SIT BY THE BROOK, LOOK FOR FISH OR OTHER WILDLIFE, or FOLLOW THE BROOK UPSTREAM: """).strip().upper()

                if story_part3 in ["SIT BY THE BROOK", "LOOK FOR FISH OR OTHER WILDLIFE", "FOLLOW THE BROOK UPSTREAM"]:
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

            if story_part3 == "SIT BY THE BROOK":
                print("You sit by the brook, feeling the cool water on your fingers. As you relax, you drift off to sleep. When you wake up, you discover it was just a dream, and you are safe at home.")
            elif story_part3 == "LOOK FOR FISH OR OTHER WILDLIFE":
                print("As you peer into the water, you spot a shimmering fish. Suddenly, it jumps out and transforms into a magical creature that grants you a wish. You wish for adventure, and the creature takes you on a journey through the enchanted forest!")
            elif story_part3 == "FOLLOW THE BROOK UPSTREAM":
                print("You follow the brook upstream and discover a hidden waterfall. Behind the waterfall, you find a treasure chest filled with gold and jewels. You have found the treasure of the enchanted forest!")

        elif story_part2 == "INVESTIGATE A STRANGE GLOWING LIGHT":  # Investigate a strange glowing light
            while True:
                story_part3 = input("""\nCuriosity piqued, you move cautiously toward the glowing light. As you get closer, you notice it pulsating softly, casting an ethereal glow on the surrounding trees. The air feels charged with energy.

CHOICE 3:

APPROACH THE LIGHT SLOWLY
CALL OUT TO SEE IF ANYONE ELSE IS NEARBY
DECIDE TO TURN BACK
Choose APPROACH THE LIGHT SLOWLY, CALL OUT TO SEE IF ANYONE ELSE IS NEARBY, or DECIDE TO TURN BACK: """).strip().upper()

                if story_part3 in ["APPROACH THE LIGHT SLOWLY", "CALL OUT TO SEE IF ANYONE ELSE IS NEARBY", "DECIDE TO TURN BACK"]:
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

            if story_part3 == "APPROACH THE LIGHT SLOWLY":
                print("As you approach the light, it reveals a friendly fairy who offers to guide you through the forest. You embark on a magical adventure together, discovering hidden wonders.")
            elif story_part3 == "CALL OUT TO SEE IF ANYONE ELSE IS NEARBY":
                print("Your voice echoes through the trees, and suddenly, a group of forest creatures appears. They invite you to join their celebration, and you dance under the stars until dawn.")
            elif story_part3 == "DECIDE TO TURN BACK":
                print("Feeling uneasy, you turn back. As you leave, the light flickers and fades, but you feel a sense of relief. You return home, safe and sound, with a story to tell.")

    elif story_part1 == "TURN BACK AND HEAD HOME":  # Turn back and head home
        if story_part2 == "CONFRONT THE SHADOWY FIGURE":  # Confront the shadowy figure
            while True:
                story_part3 = input("""\nYou take a deep breath and step toward the treeline, determined to face whatever is watching you. As you approach, the figure becomes clearer—a tall silhouette with glowing eyes. It seems to be waiting for you to make the first move.

CHOICE 3:

ASK THE FIGURE WHO IT IS AND WHAT IT WANTS
PREPARE TO DEFEND YOURSELF
TRY TO COMMUNICATE PEACEFULLY
Choose ASK THE FIGURE WHO IT IS AND WHAT IT WANTS, PREPARE TO DEFEND YOURSELF, or TRY TO COMMUNICATE PEACEFULLY: """).strip().upper()

                if story_part3 in ["ASK THE FIGURE WHO IT IS AND WHAT IT WANTS", "PREPARE TO DEFEND YOURSELF", "TRY TO COMMUNICATE PEACEFULLY"]:
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

            if story_part3 == "ASK THE FIGURE WHO IT IS AND WHAT IT WANTS":
                print("The figure reveals itself to be a guardian of the forest. It thanks you for your bravery and grants you a magical token that will protect you in your future adventures.")
            elif story_part3 == "PREPARE TO DEFEND YOURSELF":
                print("As you prepare for a confrontation, the figure steps forward and reveals itself to be a friendly spirit. It offers you guidance and wisdom for your journey ahead.")
            elif story_part3 == "TRY TO COMMUNICATE PEACEFULLY":
                print("Your peaceful gesture is met with kindness. The figure shares stories of the forest and its secrets, and you leave with newfound knowledge and respect for nature.")

        elif story_part2 == "QUICKEN YOUR PACE AND IGNORE IT":  # Quicken your pace and ignore it
            while True:
                story_part3 = input("""\nYou feel a surge of adrenaline as you quicken your pace, trying to put distance between yourself and the shadowy figure. The feeling of being watched lingers, but you focus on getting to safety.

CHOICE 3:

LOOK BACK TO SEE IF THE FIGURE IS FOLLOWING YOU
FIND A NEARBY ROAD OR PATH
SEEK SHELTER IN A NEARBY BUILDING
Choose LOOK BACK TO SEE IF THE FIGURE IS FOLLOWING YOU, FIND A NEARBY ROAD OR PATH, or SEEK SHELTER IN A NEARBY BUILDING: """).strip().upper()

                if story_part3 in ["LOOK BACK TO SEE IF THE FIGURE IS FOLLOWING YOU", "FIND A NEARBY ROAD OR PATH", "SEEK SHELTER IN A NEARBY BUILDING"]:
                    break
                else:
                    print("Invalid choice. Please choose a valid option.")

            if story_part3 == "LOOK BACK TO SEE IF THE FIGURE IS FOLLOWING YOU":
                print("You glance back and see the figure has vanished. Relieved, you continue home, but the experience leaves you with a sense of wonder about the unknown.")
            elif story_part3 == "FIND A NEARBY ROAD OR PATH":
                print("You find a path that leads you safely out of the forest. As you walk, you reflect on your adventure and the lessons learned about courage and curiosity.")
            elif story_part3 == "SEEK SHELTER IN A NEARBY BUILDING":
                print("You find an old cabin and take refuge inside. As night falls, you hear stories of the forest from the cabin's owner, who shares tales of magic and mystery.")

    else:
        print("Invalid choice. Please choose a valid option.")
        return part3(story_part1, story_part2)  # Retry the input

    return story_part3

def part4(story_part1, story_part2, story_part3):
    if story_part1 == "ENTER THE FOREST":
        if story_part2 == "FOLLOW THE SOUND OF A BUBBLING BROOK":
            if story_part3 == "SIT BY THE BROOK":
                print("You wake up from your dream, realizing it was just a fantasy. However, you feel inspired to explore the world beyond your home.")
            elif story_part3 == "LOOK FOR FISH OR OTHER WILDLIFE":
                print("Your wish for adventure leads you to discover a hidden realm filled with magical creatures. You become their protector.")
            elif story_part3 == "FOLLOW THE BROOK UPSTREAM":
                print("The treasure you found grants you the ability to communicate with animals, and you become a legendary figure in the forest.")

        elif story_part2 == "INVESTIGATE A STRANGE GLOWING LIGHT":
            if story_part3 == "APPROACH THE LIGHT SLOWLY":
                print("The fairy guides you to a secret garden where you find eternal happiness and friendship.")
            elif story_part3 == "CALL OUT TO SEE IF ANYONE ELSE IS NEARBY":
                print("The celebration with the forest creatures becomes a yearly festival, and you are honored as their guest of honor.")
            elif story_part3 == "DECIDE TO TURN BACK":
                print("You return home, but the memory of the light stays with you, inspiring you to seek magic in everyday life.")

    elif story_part1 == "TURN BACK AND HEAD HOME":
        if story_part2 == "CONFRONT THE SHADOWY FIGURE":
            if story_part3 == "ASK THE FIGURE WHO IT IS AND WHAT IT WANTS":
                print("The guardian grants you a quest to protect the forest, and you become a hero in your own right.")
            elif story_part3 == "PREPARE TO DEFEND YOURSELF":
                print("The spirit teaches you the ways of magic, and you become a powerful sorcerer.")
            elif story_part3 == "TRY TO COMMUNICATE PEACEFULLY":
                print("You form a bond with the guardian, and together you restore balance to the forest.")

        elif story_part2 == "QUICKEN YOUR PACE AND IGNORE IT":
            if story_part3 == "LOOK BACK TO SEE IF THE FIGURE IS FOLLOWING YOU":
                print("You realize that facing your fears is the first step to overcoming them, and you become more courageous in life.")
            elif story_part3 == "FIND A NEARBY ROAD OR PATH":
                print("You find a new path that leads to unexpected adventures, and you become a traveler of the world.")
            elif story_part3 == "SEEK SHELTER IN A NEARBY BUILDING":
                print("The stories you hear inspire you to write your own tales, and you become a famous storyteller.")

def main():
    story_part1 = part1()
    story_part2 = part2(story_part1)
    story_part3 = part3(story_part1, story_part2)  # Grand finale
    print("\n")
    part4(story_part1, story_part2, story_part3)  # Add part 4 for endings

if __name__ == "__main__":
    main()