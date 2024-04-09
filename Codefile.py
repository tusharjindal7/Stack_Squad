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

def display_hangman(attempts):
    hangman_pics = [
        '''
         _______
        |       |
        |
        |
        |
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |
        |
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |       |
        |
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |      /|
        |
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |      /|\\
        |
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |      /|\\
        |      /
        |
      __|__
      |    |______
      |___________| 
        ''',
        '''
         _______
        |       |
        |       O
        |      /|\\
        |      / \\
        |
      __|__
      |    |______
      |___________| 
        '''
    ]
    print(hangman_pics[max(attempts, -1)])

def hangman():
    while True:
        word = choose_word()
        guessed_letters = []
        attempts = 6

        print("Welcome to Hangman!")
        print("The word has {} letters.".format(len(word)))

        while True:
            print("\nAttempts left:", attempts)
            display_hangman(6-attempts)
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
                    print(display_hangman(6))
                    print("You're out of attempts! The word was '{}'.".format(word))
                    break
            else:
                print("Correct!")

            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You guessed the word '{}'!".format(word))
                break
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == "__main__":
    hangman()
