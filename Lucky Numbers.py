from random import randint

print("")
print("Welcome to Lucky Numbers! 3 random numbers (0-100) will be generated.")
print("If one of them is your lucky number, you will win!")
print("")

how_many = input("How many winning numbers would you like to generate: ")
number = input("Please enter your lucky number: ")
lucky_numbers = []

if how_many.isnumeric() and number.isnumeric():
    while int(len(lucky_numbers)) < int(how_many):
        lucky_numbers.append(randint(0, 100))
        if int(len(lucky_numbers)) == int(how_many):
            break

    if int(number) in lucky_numbers:
        print("")
        print("Congratulations! You won!")
        print("")
    else:
        print("")
        print("Oh no! You lost!")
        print("")
else:
    print("")
    print("Are you sure you did not type in any letters? Please restart.")
    print("")