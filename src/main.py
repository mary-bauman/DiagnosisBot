# userName = input("Welcome! What is your name?\n")
# goal = input("What would you like to do today?\n")

# """ allows you to break a string into multiple lines
welcome_prompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

name_prompt = "What is the patient's name?\n"
appearancePrompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eyePrompt = "How are the patient's eyes?\n - 1: Normal or slightly sunken\n - 2: Very sunken\n"

severeDehydration = "Severe dehydration"
someDehydration = "Some dehydration"
noDehydration = "No dehydration"
invalid = "Invalid response"

patientName = ""

patients = dict()

def list_patients():
    patients["test"] = "testing"
    for p in patients:
        print(f"{p}: {patients[p]}")

def assess_skin():
    print("Assessing skin")

def assess_eyes(patientAppearance):
    eyes = input(eyePrompt)
    if eyes == "1":
        return noDehydration
    elif eyes == "2":
        return severeDehydration
    else:
        print("Invalid response")
        return invalid


def asses_appearance():
    while(True):
        appearancePrompt = f"How is {patientName}'s general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
        patientAppearance = input(appearancePrompt)
        if patientAppearance == "1":
            print(f"{patientName} has normal appearance")
            return assess_eyes(patientAppearance)
        elif patientAppearance == "2":
            print(f"{patientName} is irritable or lethargic")
            return assess_skin()
        else:
            print("Invalid response")


def start_new_diagnosis():
    patientName = input(name_prompt)
    diagnosis = asses_appearance()
    patients[patientName] = diagnosis

def main():
    while(True):
        selection = input(welcome_prompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return
        else:
            print("invalid response")
main()