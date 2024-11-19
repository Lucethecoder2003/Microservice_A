Microservice_A
This repository contains my teammate's microservice.

Microservice Communication Contract
This microservice reads equations from HISTORY.txt, processes them, and writes formatted results with a random greeting to HISTORYv2.txt.

To Request Data:
Ensure HISTORY.txt exists in the same directory.
Write equations (one per line) into HISTORY.txt.

To Receive Data:
Wait for the microservice to process HISTORY.txt.
Open and read the generated HISTORYv2.txt.
For example, if HISTORY.txt contains:
2 + 2 = 4  
3 * 3 = 9  
10 / 2 = 5  

The resulting HISTORYv2.txt might contain:
Hello! Ready to solve problems? Let's get started!  
1. 2 + 2 = 4  
2. 3 * 3 = 9  
3. 10 / 2 = 5  

To request data:
python
Copy code
with open("HISTORY.txt", "w") as file:  
    file.write("2 + 2 = 4\n3 * 3 = 9\n10 / 2 = 5\n")
To receive data:
import time, os  
while not os.path.exists("HISTORYv2.txt"):  
    time.sleep(1)  
with open("HISTORYv2.txt", "r") as file:  
    print(file.read())  
