import random

print("=====================================")
print("     GUESS THE NUMBER GAME")
print("=====================================")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0

print("I have selected a number between 1 and 100.")
print("Can you guess  it?")

while True:
    try:
        guess = int(input("Enter your  guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low! Try Again.\n")

        elif guess > secret_number:
            print("Too High! Try Again.\n")

        else:
            print("\n🎉  Congratulations!")
            print(f"You guessed the correct number: {secret_number}")
            print(f"You took {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number!")

print("\nThank you for playing!")
