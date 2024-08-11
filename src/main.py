# userName = input("Welcome! What is your name?\n")
# goal = input("What would you like to do today?\n")

# """ allows you to break a string into multiple lines
welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"

appearance_prompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"

def list_patients():
    print("Listing patients and diagnoses")

def assess_skin():
    print("Assessing skin")

def assess_eyes():
    print("Assessing eyes")


def start_new_diagnosis():
    patientName = input(name_prompt)
    patientAppearance = input(appearance_prompt)

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            # Exits the program
            return
        else:
            print("invalid response")
main()