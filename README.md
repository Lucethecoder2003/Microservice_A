# Microservice_A
This is the repository for my teammates Microservice

Microservice Communication Contract
This microservice processes equations from a file and formats them into a new file with a random greeting. To request data from the microservice, ensure that the file HISTORY.txt exists in the same directory as the microservice. Write text, such as equations, into HISTORY.txt, with each line representing a separate equation or item. The microservice will monitor HISTORY.txt for changes, process its contents, and create an updated file, HISTORYv2.txt, containing a greeting and the formatted data.

To receive data from the microservice, wait for it to generate the file HISTORYv2.txt. This file will only be created after HISTORY.txt is detected and processed. Once the file is available, open and read from HISTORYv2.txt to retrieve the output. For example, if HISTORY.txt contains the equations 2 + 2 = 4, 3 * 3 = 9, and 10 / 2 = 5, the microservice will generate HISTORYv2.txt with content similar to:

Hello! Ready to solve problems? Let's get started! 
1. 2 + 2 = 4
2. 3 * 3 = 9
3. 10 / 2 = 5

   
Programmatically, you can request data by writing to HISTORY.txt. For instance, the following Python code can be used:

with open("HISTORY.txt", "w") as file:
    file.write("2 + 2 = 4\n")
    file.write("3 * 3 = 9\n")
    file.write("10 / 2 = 5\n")
    
To receive data, you can programmatically read from HISTORYv2.txt after the microservice processes the request. For example:

import time
# Wait for the microservice to process the request
output_file = "HISTORYv2.txt"
while not os.path.exists(output_file):
    time.sleep(1)
# Read the output
with open(output_file, "r") as file:
    content = file.read()
    print("Microservice Response:\n", content)
    
This microservice relies on the file system for communication. Ensure the required files, HISTORY.txt and HISTORYv2.txt, are in the working directory. It assumes only one request is processed at a time, so avoid overwriting HISTORY.txt during processing. Additionally, ensure HISTORY.txt is properly formatted before making a request to avoid unexpected results.
