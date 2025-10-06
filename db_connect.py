import random

print(" Welcome to the Number Guessing Game!")
print("you have upto five attempts to guess the number")
# The program picks a random number between 1 and 20
correct_number = random.randint(1, 10)
maximum_attempts = 3
attempts = 0

while True:
    guess = int(input('\n'"Guess a number between 1 and 20: "))
    attempts += 1

    if guess == correct_number:
        print(f"🎉 Correct! You guessed the number in {attempts} attempts.")
        score = max(100 - (attempts - 1) * 10, 0)  # simple scoring system
        print(f"Your score: {score}")
        break
    elif guess < correct_number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    if attempts == maximum_attempts:
        print(f"too many attempts! the correct number is, {correct_number}")
