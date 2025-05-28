# I used the time library to store how much time the player took until he got it right.
import time

def jogar_word_guessing(secret_word):
    """
    Executes a word guessing game in the style of Wordle,
    keeping track of the number of attempts and elapsed time.
    """
    secret_word = secret_word.lower()
    n = len(secret_word)
    attempts = 0
    hint = ["_"] * n

    print("Welcome to the word guessing game!")
    print("Your hint is:", " ".join(hint))

    # Start the timer
    start_time = time.time()

    while True:
        guess = input("What is your guess? ").strip().lower()
        attempts += 1

        if len(guess) != n:
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        if guess == secret_word:
            # Stop the timer
            elapsed = time.time() - start_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)

            print("Congratulations! You guessed it!")
            print(f"It took you {attempts} guesses and {minutes} minute(s) {seconds} second(s).")
            break

        # Generate new hint
        hint = []
        for i, ch in enumerate(guess):
            if ch == secret_word[i]:
                hint.append(ch.upper())
            elif ch in secret_word:
                hint.append(ch.lower())
            else:
                hint.append("_")

        print("Your hint is:", " ".join(hint))


if __name__ == "__main__":
    jogar_word_guessing("mosiah")
