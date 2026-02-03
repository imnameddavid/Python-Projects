import csv
import pandas as pd
import matplotlib.pyplot as plt

startingnum = 0 # The value to begin with
endingnum = 0 # The value to end with
num = 0 # The current number being checked
steps = 0 # The steps for the current number to reach 1

while startingnum == 0:
    try:
        startingnum = int(input("Enter a starting number: "))
    except ValueError:
        pass

while endingnum <= startingnum:
    try:
        endingnum = int(input("Enter an ending number: "))
    except ValueError:
        pass

print("Generating values...")

with open('data1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["steps"])

    while startingnum != endingnum + 1:

        steps = 0

        num = startingnum

        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            steps = steps + 1

        writer.writerow([steps])

        print(f"Number: {startingnum} - Steps taken: {steps}")

        startingnum = startingnum + 1

print("Generated! Creating data representation...")

graph = pd.read_csv('data1.csv')
graph.plot(kind="line")
plt.show()