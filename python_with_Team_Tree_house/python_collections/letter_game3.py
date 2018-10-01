import os
import random
import sys


# make a list of words

WORDS = [
    'apple',
    'banana',
    'orange',
    'coconut',
    'strawberrry',
    'lime',
    'grapesfruit',
    'lemon',
    'kumquat',
    'blueberry',
    'melon'
]


def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(misses, correct, word):
    clear()
    print("Strikes: {}/7".format(len(misses)))
    print('\n')

    print("Missed letters:", end=" ")
    for letter in misses:
        if letter in correct:
            print(letter, end=' ')
            print("\n")

    for letter in word:
        if letter in correct:
            print(letter, end=' ')
        else:
            print('_ ', end='')

    print("\n\n")

def get_guess(guesses):

    while True:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("You can only guess a single letter!")
            continue
        elif guess in guesses:
            print("You've already guessed {}. Try again!".format(guess))
            continue
        elif not guess.isalpha():
            print("You can only guess letters!")
            continue
        else:
            return guess


def play(done):
    clear()
    word = random.choice(WORDS)
    misses = set()
    correct = set()
    word_set = set(word)

    while True:
        draw(misses, correct, word)
        guess = get_guess(misses | correct)

        if guess in word_set:
            correct.add(guess)


            if not word_set.symmetric_difference(correct):
                print("You Win!")
                print("The secret word was {}.".format(word.upper()))
                done = True

        else:
            misses.add(guess)
            if len(misses) == 7:
                draw(misses, correct, word)
                print("You Lost!")
                print("The secret word was {}.".format(word))
                done = True

        if done:
            if input("Play again? [Y/n] ").lower() != "n":
                return play(done=False)
            else:
                sys.exit()

def welcome():
    start = input("Press Enter/return to start or Q to quit. ").lower()
    if start == "q":
        print("Bye!")
        sys.exit()
    else:
        return True


print("Welcome to Letter Guess!")

done = False

while True:
    clear()
    welcome()
    play(done=done)
