"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730489697"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
single_character: str = input("Enter a single character: ")
if len(single_character) != 1:
    print("Error: Character must be a single character")
    exit()
print("Searching for " + single_character + " in " + user_word)

counting_matches: int = 0

if single_character == user_word[0]:
    print(single_character + " found at index 0")
    counting_matches = counting_matches + 1
if single_character == user_word[1]:
    print(single_character + " found at index 1")
    counting_matches = counting_matches + 1
if single_character == user_word[2]:
    print(single_character + " found at index 2")
    counting_matches = counting_matches + 1
if single_character == user_word[3]:
    print(single_character + " found at index 3")
    counting_matches = counting_matches + 1
if single_character == user_word[4]:
    print(single_character + " found at index 4")
    counting_matches = counting_matches + 1

if counting_matches == 1:
    print("1 instance of " + single_character + " found in " + user_word)
else:
    if counting_matches > 1:
        print(str(counting_matches) + " instances of " + single_character + " found in " + user_word)
    else:
        print("No instances of " + single_character + " found in " + user_word)