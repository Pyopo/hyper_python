# HANGMAN
from random import *

print("H A N G M A N\n")

words = 'python', 'java', 'kotlin', 'javascript'  # list of words to guess
word = list(words[randint(0, 3)])  # picking random word to guess

container = []
container1 = ''
used_letters = []
decision = ''

for letter in word:  # generating '-' for each letter in word
    container.append('-')
chances = 8  # chances

while decision != 'play' and decision != 'exit':  # if decision not play or exit, repeat
    decision = input('Type "play" to play the game, "exit" to quit:')

    if decision == 'play':  # reaction to play
        while chances > 0:
            container1 = ''  # restarting string container1

            for letter in container:  # picking guessed and not guessed characters and changing into string
                container1 += letter
            print(container1)

            guess = input('Input a letter: ')  # input of letter

            if len(guess) == 1:  # checking if input is a single character
                if ord(guess) in range(97, 123):  # checking if guess is a lowercase latin letter

                    if guess in word and guess not in used_letters:  # correct letter in guess
                        for i in range(0, len(word)):  # comparing character to word and changing container
                            if word[i] == guess:
                                container[i] = guess

                    elif guess not in word and guess not in used_letters:  # wrong and letter not used before
                        print('No such letter in the word')
                        chances = chances - 1

                    elif guess in used_letters:  # letter used before
                        print('You already typed this letter')

                    used_letters += guess  # adding letter to list of used letters
                else:  # input not a lowercase letter
                    print('It is not an ASCII lowercase letter')
            else:  # reacting if input not a single character
                print('You should input a single letter')

            if container == word:  # checking if player won
                chances = 0
                print('You survived!')

            if chances == 0 and container != word:  # checking if player lose
                print('You are hanged!')
            print('')
    if decision == 'exit':  # reaction to exit
        break
