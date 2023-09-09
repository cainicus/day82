import pandas as pd

data = pd.read_csv('data/morse.csv')
morse_dict = {row.letter: row.morse for (index, row) in data.iterrows()}

# print(morse_dict)

print("Enter the phrase to translate into Morse code.")
phrase = input("NOTE: Only enter letters, spaces and numbers. No punctuation.\n").upper()

translation = []

for char in phrase:
    if char == " ":
        translation.append("/")
    else:
        translation.append(morse_dict[char])

print(' '.join(translation))