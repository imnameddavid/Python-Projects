import random
import string

try:
    characters = int(input("How many characters would you like in your password? "))
except ValueError:
    print("Invalid! Using default of 16 characters.")
    characters = 16

passlist = random.choices(string.ascii_letters, k = characters)
print(passlist)

for i in range((characters // 4) - 1):
    passlist.insert((i * 5) + 4, '-')

password = "".join(passlist)
print(password)