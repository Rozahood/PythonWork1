import random

user_input = int(input("Enter a number: "))
generate_random_number = random.randint(0, 9)

print(generate_random_number)

if user_input == generate_random_number:
    print("you are on point")

else:
    print("Get on point")