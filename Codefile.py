import random

def choose_word():
    words = ['apple', 'banana', 'orange', 'grape', 'strawberry', 'kiwi', 'pineapple']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while True:
        print("\nAttempts left:", attempts)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect!")
            attempts -= 1
            if attempts == 0:
                print("You're out of attempts! The word was '{}'.".format(word))
                break
        else:
            print("Correct!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You guessed the word '{}'!".format(word))
            break

if __name__ == "__main__":
    hangman()