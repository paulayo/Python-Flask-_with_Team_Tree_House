import random
# generate a random number between 1 and 10
# safely make an int
# limit guesses
# too high message
# too low message

def game():
    secret_num = random.randint(1, 10)
    guesses = []

    while len(guesses) < 5:
        try:
            # get a number guess from the player
            guess = int(input('Guess a number between 1 to 10  '))
        except ValueError:
            print("{} isn't a number ".format(guess))
        else:
            # compare guess to secret number
            if guess == secret_num:
                print(f"You go it! My number was {secret_num}")
                break
            elif guess < secret_num:
                print("My number is higher than {}".format(guess))
            # print hit/miss
            else:
                print("My number is lower than {}".format(guess))
        guesses.append(guess)
    else:
        print("You didn't get it! My number was {}".format(secret_num))

    play_again = input("Do you  want to play again?  Y/n")
    if play_again != "n":
        game()
    else:
        print('BYE!!!')
game()
