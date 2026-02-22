import random
import string
print("---- Password Generator ----")
while True:
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password:", password)
    again = input("\nGenerate another password? (yes/no): ").lower()
    if again != "yes":
        print("Thank you!")
        break