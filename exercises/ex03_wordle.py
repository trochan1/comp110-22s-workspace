"""EX03 - Structured Wordle - Yet another cute step toward Wordle."""

__author__ = "730489697"


def contains_char(word: str, character: str) -> bool:
    """Returns True if character is found within word and False if character is not found within word."""
    assert len(character) == 1
    idx: int = 0
    while idx < len(word):
        # a while loop can be used to prompt a user to input a word until it is the correct length (rather than exiting the program early).
        if character == word[idx]:
            return True
        else:
            idx += 1
            # the += operator adds value to a counter variable. in this case, idx += 1 means the same thing as idx = idx + 1.
    return False


def emojified(user_word: str, secret_word: str) -> str:
    """Returns a string of emojis."""
    assert len(user_word) == len(secret_word)
    idx: int = 0
    boxes: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while idx < len(secret_word):
        if(user_word[idx] == secret_word[idx]):
            boxes += GREEN_BOX
        elif contains_char(secret_word, user_word[idx]):
            boxes += YELLOW_BOX
            # if the letter is found in the word but not in the correct index, a yellow box will be added.
        else:
            boxes += WHITE_BOX
            # if the letter is not found in the word, a white box will be added.
        idx += 1
    return boxes
    # the boxes will be returned only after the while loop is done running (hence why it is indented at the same level as the first while command) 
    # to prevent the boxes from returning too early and stopping the function.


def input_guess(number: int) -> str:
    """This is a string that asks the user to imput a guess of a specific length."""
    word_length: str = input(f"Enter a {number} character word: ")
    # an f-string format can be used when concatenating non-string values within a larger string.
    while len(word_length) != number:
        word_length = input(f"That wasn't {number} chars! Try again: ")
    return word_length


def main() -> None:
    """The main game loop is the point of the program."""
    answer: str = "codes"
    g_string: str = ""
    turns: int = 0
    while turns < len(answer):
        print(f"=== Turn {turns +1}/6 ===")
        g_string: str = input_guess(len(answer))
        emoji: str = emojified(g_string, answer)
        print(emoji)
        if g_string == answer:
            print(f"You won in {turns+1}/6 turns!")
            break
        turns += 1
    if g_string > answer:
        print("x/6 - Sorry, try again tomorrow!")


main()