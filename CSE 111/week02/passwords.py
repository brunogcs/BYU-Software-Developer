'''
2 - Passwords should be checked against both a list of known passwords and a list of dictionary of words. 
María has provided both a dictionary file that contains about 70,000 words and a file that contains the top 1 million passwords used.
'''
import os

LOWER=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS=["0","1","2","3","4","5","6","7","8","9"]
SPECIAL=["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", """, """, ",", ".", "<", ">", "?", "/", "`", "~"]

def input_password():
    
    word = input("Enter the password you want to check (if you want to quit type 'Q or q'): ")
    return word

def word_in_file(word, filename, case_sensitive=False):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(base_dir, filename)

    if case_sensitive == True:
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f:
                if word in line.strip():
                    #print("it works "+line)
                    return True
        return False
        
    if case_sensitive == False:
        with open(filepath, "r", encoding="utf-8") as f:
             for line in f:
                line = line.lower()
                word = word.lower()
                if word in line.strip():
                    #print("it works "+line)
                    return True
        return False
    pass

def word_has_character(word, character_list):
    pass

def word_complexity(word):
    pass

def password_strength(word, min_length=10, strong_length=16):
    if len(word) < 8:
        return "Weak"
    elif len(word) < 12:
        return "Medium"
    else:
        return "Strong"

def main():
    print("Welcome to the password checker tool. The tool will check the strength of your password.")
    word = ''
    while word not in ['Q', 'q']:
        word = input_password()
        print(word)
        exit() ##########
        on_top_passwords = word_in_file(word, 'toppasswords.txt', True)
        on_dictionary = word_in_file(word, 'wordlist.txt', False)
        password_checked = password_strength(word)
        if word not in ['Q', 'q']:
            print('the password "' + word + '" was checked and is: ' + password_checked)
        else:
            print("Goodbye")

if __name__ == "__main__":
    main()

    ABaDDon