import time

startingnum = 0
interval = 0

while startingnum == 0:
    try:
        startingnum = int(input("Enter a starting number: "))
    except ValueError:
        pass

while interval == 0:
    try:
        interval = int(input("Enter an interval in milliseconds: "))
    except ValueError:
        pass

if startingnum < 0:
    startingnum = 0

if interval < 0:
    interval = 0

def check_odd_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

while True:
    startingnum = startingnum + 1
    print(f"Starting number: {startingnum}")
    num = startingnum
    while num != 1:
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
        print(f"{num} - {check_odd_even(num)}")
        time.sleep(interval / 1000)