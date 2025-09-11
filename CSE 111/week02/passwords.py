import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
           "[", "]", "{", "}", "|", ";", ":", '"', "'", ",", ".", "<", ">", "?", "/", "`", "~"]

def input_password():
    
    word = input("Enter the password you want to check (if you want to quit type 'Q or q'): ")
    return word

def word_in_file(word, filename, case_sensitive=False):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    if case_sensitive == True:
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f:
                if word == line.strip():
                    #print("it works "+line)
                    return True
        return False
        
    if case_sensitive == False:
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f:
                line = line.lower()
                word = word.lower()
                if word.lower() == line.strip().lower():
                    #print("it works "+line)
                    return True
        return False
    pass

def word_has_character(word, character_list):
    for ch in word:
        if ch in character_list:
            return True
    return False

def word_complexity(word):
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

def password_strength(password, min_length=10, strong_length=16):
    if word_in_file(password, 'wordlist.txt', False):
        print("Password is a dictionary word and is not secure.")
        return 0
    if word_in_file(password, 'toppasswords.txt', True):
        print("Password is a commonly used password and is not secure.")
        return 0
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    complexity = word_complexity(password)
    return 1 + complexity


def main():
    print("Welcome to the password checker tool. The tool will check the strength of your password.")
    while True:
        word = input_password()
        if word.lower() == 'q':
            print("Goodbye")
            break
        strength = password_strength(word)
        print(strength)

if __name__ == "__main__":
    main()