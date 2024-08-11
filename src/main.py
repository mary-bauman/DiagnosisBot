# userName = input("Welcome! What is your name?\n")
# goal = input("What would you like to do today?\n")

# """ allows you to break a string into multiple lines
welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

def list_patients():
    print("Listing patients and diagnoses")

def start_new_diagnosis():
    print("Starting a new diagnosis")

def main():
    selection = input(welcome_prompt)
    # Using an if statement, we branch the code according to user selection:
    if selection == "1":
        # If 'selection' equals to 1, we're going to call the list_patients function
        list_patients()
    # Otherwise, if 'selection' equals to 2, we're going to call the start_new_diagnosis function
    elif selection == "2":
        start_new_diagnosis()
    # And if 'selection' equals to q, we're going to simply quit the program
    elif selection == "q":
        return

# Starts the program execution
main()