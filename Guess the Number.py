import random

def guess(x):
    random_number = random.randint(1, x)
    guess_no = 0
    while guess_no != random_number:
        guess_no = int(input(f"Guess a number btw 1 and {x}: "))
        if guess_no < random_number:
            print("sorry guess again too low!")
        elif guess_no > random_number:
            print("sorry, guess again too high.")
    print("Congratulations, you have guessed the correct number!")



guess(10)
