import dndchar

print("Welcome to DND Python Console")

while True:
    print("----------------------------------------------------------------------------------------------")
    user_input = input("Please Enter A Command (Type 'help' for commands):\n").lower()

    if user_input == "create character":
        name_input = input("Player's Name?\n").title()
        char_input = input("Characters's Name?\n").title()
        race_input = input("Character's Race?\n").title()
        class_input = input("Character's Class?\n").title()
        dndchar.create_char(name_input, char_input, race_input, class_input)
    elif user_input == "help":
        print("----------------------------------------------------------------------------------------------")
        print("Help\n-This command lists all usable commands")
        print("Create Character\n-This command creates a new character and asks for the characters information\n-Then it saves to a CSV file in the PlayerData folder")
        print("Exit\n-Exits the program")
    elif user_input == "exit":
        print("Goodbye")
        break
    elif user_input == "test":
        dndchar.create_char('Test', 'Test', 'Half Orc', 'Barbarian')
    else:
        print("Please Enter Valid Command")

