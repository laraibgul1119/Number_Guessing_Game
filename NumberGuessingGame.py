# Importing library for getting the random number
import random
print("Welcome to Number Guessing Game!")
# Getting upper limit from user
upperBound=int(input("Enter your upper bound: "))

# Getting lower limit from user
lowerBound=int(input("Enter your lower bound: "))
attempts=7
# Getting a random number in the given limit
guess=random.randint(lowerBound,upperBound)
isGuessed=False

# This loop continues until the number is not guessed
while not isGuessed and attempts > 0:
    print("You have ",attempts," attempts left to guess the number.")
    num=int(input("Enter your guess: "))
    if num == guess:
        isGuessed=True
    elif num > guess:
        attempts -= 1
        print("Your guess is too high")
    elif num < guess:
        attempts -= 1
        print("Your guess is too low")

if isGuessed:
    print("Congratulations! You guessed the number.🥳")
else:
    print("The number was ",guess)
    print("Don't lose your heart you will guess it one day..👌")