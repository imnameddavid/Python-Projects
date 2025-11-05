#1

while True:
    age_input = input("Enter your age: ")

    if age_input.isdigit():
        age = int(age_input)
        break
    else:
        print("Invalid! Enter a number.")

if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")