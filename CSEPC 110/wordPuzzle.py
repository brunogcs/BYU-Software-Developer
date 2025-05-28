'''

'''
print("Welcome to the word guessing game!")
number_try = 0

#Select the secret word
secret_word = 'nefi'.lower()
len_secret_word = len(secret_word)
hint = (" _" * len_secret_word).strip()  # Inicializa o hint com sublinhados e espaços

#Ask for the first guess
print(f"Your hint is: {hint}")
user_guess = input("What is your guess? ").lower()
len_user_guess = len(user_guess)
number_try = number_try + 1

#Loop until the user get it right
while user_guess != secret_word:
    # Comparar o comprimento do hint e do palpite
    while len_user_guess != len_secret_word:
        number_try = number_try + 1
        print("Sorry, the guess must have the same number of letters as the secret word.")
        user_guess = input("What is your guess? ")
        len_user_guess = len(user_guess)

    # Atualizar o hint com as letras corretas
    for i, letter in enumerate(secret_word):
        if letter == user_guess[i]:
            hint = hint[:2 * i] + letter + hint[2 * i + 1:]
    
    #Apresenta de forma atualizada o hint e pede um novo palpite
    print(f"Updated hint: {hint}")
    user_guess = input("What is your guess? ").lower()
    len_user_guess = len(user_guess)

    #Contabiliza a quantidade de tentativas
    number_try = number_try + 1

# Congratulation message
print("Congratulations! You guessed it!")
print(f"It took you {number_try} guesses.")