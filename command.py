import dndchar

print("Welcome to DND Python Console")

while True:
    print("----------------------------------------------------------------------------------------------")
    user_input = input("Please Enter A Command:\n").lower()

    if user_input == "create character":
        name_input = input("Player's Name?\n").title()
        char_input = input("Characters's Name?\n").title()
        dndchar.create_char(name_input, char_input)
    elif user_input == "help":
        print("----------------------------------------------------------------------------------------------")
        print("Help\n-This command lists all usable commands")
        print("Create Character\n-This command creates a new character and asks for the characters information\n-Then it saves to a CSV file in the PlayerData folder")
        print("Exit\n-Exits the program")
    elif user_input == "exit":
        print("Goodbye")
        break
    else:
        print("Please Enter Valid Command")

