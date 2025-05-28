'''
Overview

Many games and puzzles require iteration where a person (or a computer) repeats the same steps for each piece in the game or each spot in a puzzle. For this assignment, you will create an interactive word puzzle game that allows the user to make guesses until they get the answer correct, and hints are provided along the way.

Wordle is a web-based word game that became popular online in the early part of 2022. (You can learn more about it from the Wordle Wikipedia page. If you want, you can play it online for free from the New York Times page.)

For this assignment, you'll create a puzzle game that follows a similar pattern.
Project Description

The program contains a hidden secret word stored in a variable. This word can have any number of letters in it. When the program runs, the user is shown underscores ( _ ) for each letter of the word.

The user then enters a guess. If the guess is correct, the user wins and the game is over.

If the guess is not correct, the user will be given a hint to help them improve their guess for the next round.

The game continues prompting the user for new guesses and showing them hints until they guess the word correctly. When the game is over, the program displays the number of guesses that were made.

The guess must be the same number of letters as the secret word. If the guess has a different numbers of letters, the user is given a message explaining this, and no hint is provided.

The hint shows the letters of the guess, but each letter is rendered in a special way as follows:

    An underscore _ indicates that the letter was not present in the secret word.

    A lowercase letter indicates that the letter was present somewhere in the secret word, but not at that position.

    An uppercase letter indicates that the letter was present at that exact spot in the secret word. (In other words, if the second letter in the guess is also the second letter in the secret word, then that letter is shown as a capital.)

For example, if the secret word were: mosiah, then the program would initially display:


Your hint is: _ _ _ _ _ _

If the user's guess were: temple, they would learn that the m in temple is the only letter in the secret word, but it is in the wrong spot, so it would be displayed in lowercase as shown:


Your hint is: _ _ m _ _ _

But if the user instead guessed: moroni, they would receive the following as a hint:


Your hint is: M O _ o _ i

Notice that in the hint above, the M and the first O from moroni are capitalized, because those letters are also the first two letters of mosiah.

The i and the second o from moroni are displayed, because they are present in the secret word, but they are shown in lowercase, because the the letters in the secret word at that location are different.

The r and the n from moroni are not displayed, but instead an underscore is shown in each place, because these letters are not present in the secret word in any location.

A sample of the complete program might look as follows:


Welcome to the word guessing game!

Your hint is: _ _ _ _ _ _ 
What is your guess? temple
Your hint is: _ _ m _ _ _ 
What is your guess? moroni
Your hint is: M O _ o _ i 
What is your guess? hhhhhh
Your hint is: h h h h h H 
What is your guess? mosiah  
Congratulations! You guessed it!
It took you 4 guesses.

Because capital letters have meaning in our hints, the secret word should be all lower case. Similarly, when the user enters their guess, you should convert it to lowercase prior to checking for matches.

If the guess has a different number of letters than the secret word, it still counts as a guess, but the user does not receive a hint. This is shown in the following example:


Welcome to the word guessing game!



What is your guess? temple
Your hint is: _ _ m _ _ _ 
What is your guess? mosiah


'''
number_try = 0

#Select the secret word
secret_word = 'nefi'.upper()
len_secret_word = len(secret_word)
hint = (" _" * len_secret_word).strip()  # Inicializa o hint com sublinhados e espaços

#Ask for the first guess
print(f"Your hint is: {hint}")
user_guess = input("What is your guess? ").upper()
len_user_guess = len(user_guess)
number_try = number_try + 1

#Loop until the user get it right
while user_guess != secret_word:
    # Comparar o comprimento do hint e do palpite
    while len_user_guess != len_secret_word:
        print("Sorry, the guess must have the same number of letters as the secret word.")
        user_guess = input("What is your guess? ")
        len_user_guess = len(user_guess)

    # Atualizar o hint com as letras corretas
    for i, letter in enumerate(secret_word):
        if letter == user_guess[i]:
            hint = hint[:2 * i] + letter + hint[2 * i + 1:]
    
    #Apresenta de forma atualizada o hint e pede um novo palpite
    print(f"Updated hint: {hint}")
    user_guess = input("What is your guess? ").upper()
    len_user_guess = len(user_guess)

    #Contabiliza a quantidade de tentativas
    number_try = number_try + 1

# Congratulation message
print("Congratulations! You guessed it!")
print(f"It took you {number_try} guesses.")