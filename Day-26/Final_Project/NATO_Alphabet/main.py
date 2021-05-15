import pandas

# TODO 1. Create a dictionary in this format:

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data.to_dict()
result = {row.letter: row.code for (index, row) in data.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
should_continue = True
while should_continue:
    word = input("Enter a word: ").upper()
    try:
        output_list = [result[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        should_continue = False
        print(output_list)
