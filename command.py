import dndchar

user_input = input("Please Enter A Command:\n").lower()

if user_input == "create character":
    name_input = input("Player's Name?").title()
    char_input = input("Characters's Name?").title()
    dndchar.create_char(name_input, char_input)
else:
    print("Please Enter Valid Command")

