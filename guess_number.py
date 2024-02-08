number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != "q":
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    elif int(guess) > number:
        print(f"Sorry! You were too high, please try again.")
        guess = input("What number am I thinking of? ")
    else: 
        print(f"Sorry! You were too low, please try again.")
        guess = input("What number am I thinking of? ")

if guess == "q":
    print(f"Sorry! The number was {number}.")