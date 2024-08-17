# """ allows you to break a string into multiple lines
welcomePrompt = """Welcome doctor, what would you like to do today?\n
- To list all patients, press 1\n
- To run a new diagnosis, press 2\n
- To quit, press q\n"""

namePrompt = "What is the patient's name?\n"
appearancePrompt = "How is the patient's general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
eyePrompt = "How are the patient's eyes?\n - 1: Normal or slightly sunken\n - 2: Very sunken\n"
skinPrompt = "How is the patient's skin when you pinch it?\n - 1: Normal skin pinch\n - 2: Slow skin pinch\n"

severeDehydration = "Severe dehydration"
someDehydration = "Some dehydration"
noDehydration = "No dehydration"

patientName = ""

patients = dict()

def list_patients():
    # for p in patients:
    #     print(f"{p}: {patients[p]}")
    f = open("patients.txt", "r")
    patients = f.readlines()
    for p in patients: print(p)

def assess_skin():
    while True:
        skin = input(skinPrompt)
        if skin == "1":
            return someDehydration
        elif skin == "2":
            return severeDehydration
        else:
            print("Invalid response")

def assess_eyes():
    while True:
        eyes = input(eyePrompt)
        if eyes == "1":
            return noDehydration
        elif eyes == "2":
            return severeDehydration
        else:
            print("Invalid response")


def asses_appearance():
    while(True):
        appearancePrompt = f"How is {patientName}'s general appearance?\n - 1: Normal appearance\n - 2: Irritable or lethargic\n"
        patientAppearance = input(appearancePrompt)
        if patientAppearance == "1":
            print(f"{patientName} has normal appearance")
            return assess_eyes()
        elif patientAppearance == "2":
            print(f"{patientName} is irritable or lethargic")
            return assess_skin()
        else:
            print("Invalid response")


def start_new_diagnosis():
    patientName = input(namePrompt)
    diagnosis = asses_appearance()
    patients[patientName] = diagnosis
    print(f"{patientName} has {diagnosis}")
    f = open("patients.txt", "a")
    f.write(f"\n{patientName}: {diagnosis}\n")
    f.close()

def main():
    while(True):
        selection = input(welcomePrompt)
        if selection == "1":
            list_patients()
        elif selection == "2":
            start_new_diagnosis()
        elif selection == "q":
            return
        else:
            print("invalid response")
main()