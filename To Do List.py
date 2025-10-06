print('Welcome to our guessing game')
print('You have upto 3 attempts to guess a number')
from time import sleep
import random
correct_guess = random.randint(1,5)
attempts = 0
max_attempts= 3

while True:
    guess = int(input('\nEnter your guess number: '))
    attempts +=1
    if guess == correct_guess:
        print(f"Correct guess after {attempts} attempts")
        score = max(100 - (attempts -1)*10, 0)
        print(f"your score is {score}")
        break
    elif guess < correct_guess:
        print('Too low! try again.')
    else:
        print('Too high! try again.')
    if attempts == max_attempts:
        print("Too many attempts! Please wait for two seconds.")
        sleep(2)