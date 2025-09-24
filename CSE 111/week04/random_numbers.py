import random

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        numbers_list.append(random.randint(1, 100))
    return numbers_list

def append_random_words(words_list, quantity=1):
    for _ in range(quantity):
        words_list.append(random.choice(words_list))
    return words_list

def main():
    # Create a list of numbers
    numbers_list = [0, 1] #print("Initial list of numbers:", numbers_list)
    words_list = ["apple", "banana"]

    print("\nList of Numbers:\n")
    # Call append_random_numbers with one argument
    append_random_numbers(numbers_list)
    print("After appending 1 random number:", numbers_list)

    # Call append_random_numbers with two arguments
    append_random_numbers(numbers_list, 5)
    print("After appending 5 random numbers:", numbers_list)

    random.shuffle(numbers_list)
    print("Shuffled list of numbers:", numbers_list)

    print("\nList of words:\n")
    # Call append_random_words with one argument
    append_random_words(words_list)
    print("After appending 1 random word:", words_list)

    # Call append_random_words with two arguments
    append_random_words(words_list, 3)
    print("After appending 3 random words:", words_list)

    # Creative Enhancement: Shuffle the lists and print them
    
    random.shuffle(words_list)
    print("Shuffled list of words:", words_list)

if __name__ == "__main__":
    main()