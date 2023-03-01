import pandas

nato_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet.iterrows()}

is_incorrect = True

while is_incorrect:
    try:
        word = input("Type a word: ").upper()
        word = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        pass
    else:
        is_incorrect = False
        print(word)

