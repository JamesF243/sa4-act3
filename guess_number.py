number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")
limited = 3

while guess != "q" and limited > 0:
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        limited -= 1
        print(f"Sorry! You have", limited, "guesses left.")
        if limited > 0:
            guess = input("\nWhat number am I thinking of? ")

if guess == "q":
    print(f"Sorry! The number was {number}.")