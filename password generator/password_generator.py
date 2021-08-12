import random


def getPassword(pword_strength):
    if pword_strength == 'strong':
        upper_alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        lower_alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        other_chars = ["!", ",", "@", "%", "£", "(", ")", "=", ".", "#"]

        def upper_case():
            u1 = random.randint(0,25)
            upper_letter_random = upper_alphabet[u1]
            print(upper_letter_random, end='')

        def lower_case():
            l1 = random.randint(0,25)
            lower_letter_random = lower_alphabet[l1]
            print(lower_letter_random, end='')

        def special_chars():
            s1 = random.randint(0,9)
            special = other_chars[s1]
            print(special, end='')

        def numbers():
            n1 = random.randint(0,10)
            print(n1, end='')

        def pword():
            print("Your password has been generated: ", end=' ')
            upper_case()
            lower_case()
            upper_case()
            numbers()
            special_chars()
            upper_case()
            upper_case()
            numbers()
            special_chars()
            lower_case()
            lower_case()
            special_chars()

        pword()

    elif pword_strength == 'weak':
        f = open(r"words.txt")
        lines = f.readlines()
        def pick_password():
            word = random.choice(lines)
            print(word.rstrip("\n"), end='')
        print("Your password has been generated: ", end='')
        pick_password()
        pick_password()
        f.close()
    else:
        print("Hmmm, I am not sure what that means. Run the program again - I can only accept the values of 'weak' or 'strong'")


pword_strength = input("Do you want a weak or strong password? ")
getPassword(pword_strength)