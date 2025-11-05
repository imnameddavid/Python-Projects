#5

import time
import random

points = 0
qanswered = 0

questions = [
    {"qnumber": 1, "question": "What is 7x8?", "answer": "56", "answered?": False},
    {"qnumber": 2, "question": "What is 42+25?", "answer": "67", "answered?": False},
    {"qnumber": 3, "question": "When did WW2 end?", "answer": "1945", "answered?": False},
    {"qnumber": 4, "question": "What is the name of the animal that meows?", "answer": "cat", "answered?": False},
    {"qnumber": 5, "question": "What is the capital of England?", "answer": "london", "answered?": False},
    {"qnumber": 6, "question": "What is 'bonjour' from French to English?", "answer": "hello", "answered?": False},
    {"qnumber": 7, "question": "What coding language is this game made in?", "answer": "python", "answered?": False},
    {"qnumber": 8, "question": "Is a microphone an input or output device?", "answer": "input", "answered?": False},
    {"qnumber": 9, "question": "You have one bucket has 2 litres and another bucket with 7.5 litres. How many buckets do you have?", "answer": "2", "answered?": False},
    {"qnumber": 10, "question": "How many FINGERS do you have?", "answer": "8", "answered?": False},
]

print("Welcome to dave's ultimate quiz game!")
time.sleep(1)

print("You will get 5 out of 10 random questions.")
time.sleep(1)

print("Let's see how much you get.")
print(" ")
time.sleep(3)

while qanswered != 5:
    
    qnumber = random.randint(1, 10)

    for q in questions:
        if qnumber == q['qnumber']:
            if q["answered?"] == False:
                qanswered = qanswered + 1
                print(f"Question {qanswered}/5")
                answer = input(f"{q['question']} ").lower()
                if answer == q['answer']:
                    print(f"Correct! You have entered {answer!r}.")
                    points = points + 1
                    q["answered?"] = True
                else:
                    print(f"Wrong. You have entered {answer!r}. The answer is {q['answer']}.")
                    q["answered?"] = True
                print(" ")
            else:
                pass

if qanswered == 5:
    print(" ")
    time.sleep(0.5)
    print(f"You got {points}/5!")
    time.sleep(1)
    if points >= 3:
        print("Good job!")
    else:
        print("Get smarter.")
