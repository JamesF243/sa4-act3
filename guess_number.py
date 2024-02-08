number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? ")

while guess != "q":
    if int(guess) == number:
        print("Congratulations! You guessed the right number.")
        break
    else:
        print(f"Sorry! Please try again.")
        guess = input("\nWhat number am I thinking of? ")

if guess == "q":
    print(f"Sorry! The number was {number}.")