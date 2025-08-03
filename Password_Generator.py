import random

letters = ["a","b","c","d","e","f","g","h","j","k","l","m","n","A","B","C","D","E","F","G","H","I","J"]
numbers = [0,1,2,3,4,5,6,7,8,9]
symbols = ["!","+","*","?","#","&","$","-"]

password = ""
print("Welcome to the Python Password Generator!")
print("****************************************")

letter_amount = int(input("How many letters would you like?:\n "))
for i in range(letter_amount):
    letter = random.choice(letters)
    password += letter
print(password)
number_amount = int(input("How many numbers would you like?:\n "))
for i in range(number_amount):
    number = random.choice(numbers)
    password += str(number)

print(password)
symbols_amount = int(input("How many symbols would you like?:\n "))
for i in range(symbols_amount):
    symbol = random.choice(symbols)
    password += symbol
print(password)

print("-----------------------")




new_password = list(password)
random.shuffle(new_password)

new = ""
for i in new_password:
    new += i

print(f"Your new Password is:\n{new}")

