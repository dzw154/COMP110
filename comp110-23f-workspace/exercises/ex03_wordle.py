"""Ex02."""

__author__ = "730677774"

# Defines the secret word
secret_word: str = "codes"


def contains_char(word: str, letter: str) -> bool:
    """Checks if a letter is inside of a word."""
    assert len(letter) == 1
    count_index: int = 0
    while count_index < len(word):
        if letter == word[count_index]:
            return True
        else:
            count_index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Checks whether the letters of a given word are present in a secret word and if those letters are in the correct positions."""
    assert len(guess) == len(secret)
    result: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    count_index: int = 0
    while count_index < len(guess):
        if guess[count_index] == secret[count_index]:
            result += GREEN_BOX
        elif contains_char(secret, guess[count_index]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        count_index += 1
    return result


def input_guess(expect_length: int) -> str:
    """Checks if a user's guess is of a desired length."""
    guess: str = input(f"Enter a {expect_length} character word: ")
    while len(guess) != expect_length:
        guess = input(f"That wasn't {expect_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    player_turn: int = 1
    win_condition: bool = False
    while player_turn <= 6 and not win_condition:
        print(f"=== Turn {player_turn}/6 ===")
        guess: str = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            win_condition = True
        else:
            player_turn += 1
    if win_condition:
        print(f"You won in {player_turn}/6 turns! ")
    else:
        print("X/6 - Sorry, try again tomorrow!")
    return


if __name__ == "__main__":
    main()