import pandas as pd

data = pd.read_csv('data/morse.csv')
morse_dict = {row.letter: row.morse for (index, row) in data.iterrows()}

print("\nWelcome to Morse code translator. \n ")


def translate():
    print("Enter the phrase to translate into Morse code.")
    phrase = input("NOTE: Any special characters undefined by Mose code will be included as is.\n")

    translation = []

    for char in phrase.upper():
        if char == " ":
            translation.append("/")
        elif char not in morse_dict.keys():
            translation.append(char)
        else:
            translation.append(morse_dict[char])

    print(f"\nThat translates to\n{' '.join(translation)}\nin Morse code.\n")

    repeat = input("Would you like to translate another phrase? Y/n: \n")
    if repeat[0].upper() == "Y":
        translate()
    else:
        print("Thank you. Have a nice day.")
        return

translate()

