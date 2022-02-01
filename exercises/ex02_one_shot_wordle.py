"""EX02 - One Shot Wordle - Another cute step toward Wordle."""

__author__ = "730489697"

secret_word: str = "python"
user_word: str = input(f"What is your {len(secret_word)}-letter guess? ")
# "len(secret_word)" can be used instead of "6" so that the program runs for words of any length.
idx: int = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

boxes: str = ""

while len(user_word) != len(secret_word):
    # a while loop can be used to prompt a user to input a word until it is the correct length (rather than exiting the program early).
    user_word = input(f"That was not {len(secret_word)} letters! Try again: ")
    # an f-string format can be used when concatenating non-string values within a larger string.

while idx < len(secret_word):
    # the word python is six letters long with indices 0-5. as a result, this while loop will repeat until
    # it reaches index 5. in a five letter word, the while loop would repeat until it reaches index 4.
    if user_word[idx] == secret_word[idx]:
        # if the letter guessed appears in the secret word and is in the correct position, a green box will be added.
        boxes += GREEN_BOX
        idx += 1
        # the += operator adds value to a counter variable. in this case, idx += 1 means the same thing as idx = idx + 1.
        # value is added to the index variable to signal the while loop to evaluate the next index in the user's word and secret word.
    else:
        found_anywhere: bool = False
        alternate_idx: int = 0
        # the alternate index is used to check whether a character in a specific index in the user's word appears in a different index in the secret word.
        while alternate_idx < len(secret_word):
            if user_word[idx] == secret_word[alternate_idx]:
                found_anywhere = True
                # if the letter is found somewhere in the word, the boolean value will change to "True" to later signify the program to add a yellow box to the string.
                alternate_idx = len(secret_word)
            else:
                alternate_idx += 1
        if found_anywhere:
            boxes += YELLOW_BOX
            # if the letter is found in the word but not in the correct index, a yellow box will be added.
        else:
            boxes += WHITE_BOX
            # if the letter is not found in the word, a white box will be added.
        idx += 1
print(boxes)
# the boxes will be printed only after the while loop is done running (hence why it is indented at the same level as the first while command) 
# to prevent the boxes from being printed too many times.

if len(user_word) == len(secret_word):
    if user_word == secret_word:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")