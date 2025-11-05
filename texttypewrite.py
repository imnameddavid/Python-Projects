#4

import time

lyrics = [
    {"text": "These are cool lyrics", "speed": 0.05, "delay": 1},
    {"text": "You can enter your own lyrics", "speed": 0.1, "delay": 2},
    {"text": "And even set the speed and delay", "speed": 0.04, "delay": 0.6},
    {"text": "What will you put here?", "speed": 0.09, "delay": 1.5},
    {"text": "Fin", "speed": 0.1, "delay": 0}
]

for lyric in lyrics:
    for char in lyric["text"]:
        print(char, end="", flush=True)
        time.sleep(lyric["speed"])
    print(" ")
    time.sleep(lyric["delay"])
