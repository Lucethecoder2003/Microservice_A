import os
import time

def main():
    # Step 1: Create and write sample equations to HISTORY.txt
    history_file = "HISTORY.txt"
    equations = ["2 + 2 = 4", "3 * 3 = 9", "10 / 2 = 5"]
    
    # Ensure the file does not exist before testing
    if os.path.exists(history_file):
        os.remove(history_file)

    print("Creating HISTORY.txt with sample equations...")
    with open(history_file, "w") as file:
        for eq in equations:
            file.write(eq + "\n")

    # Step 2: Run the microservice code
    print("Running microservice...")
    os.system("python microservice.py")  # Assuming the microservice is in a file named microservice.py
    
    # Step 3: Check and print the output from HISTORYv2.txt
    output_file = "HISTORYv2.txt"
    time.sleep(1)  # Give the microservice time to process
    if os.path.exists(output_file):
        print("\nContent of HISTORYv2.txt:")
        with open(output_file, "r") as file:
            print(file.read())
    else:
        print("\nHISTORYv2.txt was not created. Check the microservice for errors.")

if __name__ == "__main__":
    main()
