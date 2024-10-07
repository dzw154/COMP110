"""Ex02."""

__author__ = "730677774"

# Defines variables
secret_word: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = ""
count_index: int = 0
guess: str = input("What is your " + str(len(secret_word)) + "-letter guess? ")

# While the guess is of a different length than the secret word
# Ask for another input
while len(guess) != len(secret_word):
    guess = input("That was not " + str(len(secret_word)) + " letters! Try again: ")

# While 
while count_index < len(secret_word):
    # If the letters at the current index match, add a green box to the result string
    if guess[count_index] == secret_word[count_index]:
        result += GREEN_BOX
    # Otherwise, check if the letter exists at any other index in the word
    else:
        guess_exist: bool = False
        alt_index: int = 0
        while alt_index < len(secret_word) and not guess_exist:
            if guess[count_index] == secret_word[alt_index]:
                guess_exist = True
            else:
                alt_index += 1
        # If the letter exists at a different index, add a yellow box to the result string, otherwise add a white box
        if guess_exist:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    count_index += 1

# Prints out how many letters you got correct and if you got the word correct
print(result)
if (guess == secret_word):
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
