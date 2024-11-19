import random
import time
import os

while True:
    if os.path.exists('HISTORY.txt') and os.path.getsize('HISTORY.txt') > 0:
        print("Moving to print")
        break
    else:
        time.sleep(1)

rand_num = random.randint(0, 2)

with open('HISTORY.txt', 'r') as history_file:
    print("Readin...")
    equations = history_file.readlines()
    while True:
        if not equations:
            print("doing nothing")
        else:
            break

    with open('HISTORYv2.txt', 'w') as updated_file:
        print("Writing...")

        updated_file.seek(0)
        updated_file.truncate()

        if (rand_num == 0):
            updated_file.write("Greetings! Let's make math less stressful and more fun! \n")
        elif (rand_num == 1):
            updated_file.write("Hello! Ready to solve problems? Let's get started! \n")
        else: 
            updated_file.write("Welcome! Let's do some math magic together! \n")
        index = 1
        for equation in equations:
            holder = f"{index}. {equation.strip()}"
            updated_file.write(f"{holder} \n")
            index+=1
        updated_file.flush()