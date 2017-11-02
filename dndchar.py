import csv
import random
import os
import skills

dir_path = os.path.dirname(os.path.realpath(__file__))

invalid_chars = "1234567890!@#$%^&*()_+-=[]{}\|;:'\",<.>/?"

player_data = {}

# Races and Classes
valid_races = ['Dragonborn', 'Dwarf', 'Elf',
               'Gnome', 'Half Elf', 'Half Orc',
               'Halfling', 'Human', 'Tiefling']

valid_classes = ['Barbarian', 'Bard', 'Cleric',
                 'Druid', 'Fighter', 'Monk',
                 'Paladin', 'Ranger', 'Rogue',
                 'Sorcerer', 'Warlock', 'Wizard']

# Ability Abbreviations
abilities = ['str', 'dex', 'con', 'int', 'wis', 'cha']


# Main function that handles the character creation and data storage
def create_char(name, char_name, race, clss):
    # Check if character name as any invalid characters
    for i in range(0, len(invalid_chars)):
        if invalid_chars[i] in name:
            print("Invalid Name")
            return

    # Set player name
    player_data['name'] = name
    player_data['char_name'] = char_name

    # Check if selected race and class are valid options
    if race in valid_races:
        player_data['race'] = race
    else:
        print("Please Enter Valid Race")
        return
    if clss in valid_classes:
        player_data['class'] = clss
    else:
        print("Please Enter Valid Class")
        return

    # Generate stats based on class and saves player data to CSV
    gen_abilities(clss)
    add_race_mods(race)
    gen_ability_mods()

    print("Here is your character so far:")
    for key, value in player_data.items():
        print(key.title() + ":", value)
    print("\n")
    skill = input("Would you like to work on skills now? (Type yes or no)\n").lower()
    if skill == "yes":
        skills.gen_skills(clss)
    else:
        save_playerdata(name)


# Generates random attribute scores, assigns to best spot
# based on race and class, and calculates modifiers
def gen_abilities(clss):
    # Generates list of 6 numbers and sorts from low to high
    number_list = []
    i = 0
    while i <= 6:
        number = random.randint(8, 18)
        number_list.append(number)
        i += 1
    ability_list = sorted(number_list)

    # Character optimization
    if clss == "Barbarian":
        player_data['str'] = ability_list[5]
        player_data['dex'] = ability_list[4]
        player_data['con'] = ability_list[3]
        player_data['int'] = ability_list[0]
        player_data['wis'] = ability_list[2]
        player_data['cha'] = ability_list[1]
    elif clss == "Rogue" or clss == "Ranger":
        player_data['str'] = ability_list[0]
        player_data['dex'] = ability_list[5]
        player_data['con'] = ability_list[4]
        player_data['int'] = ability_list[1]
        player_data['wis'] = ability_list[3]
        player_data['cha'] = ability_list[2]
    elif clss == "Sorcerer" or clss == "Warlock" or clss == "Bard":
        player_data['str'] = ability_list[0]
        player_data['dex'] = ability_list[4]
        player_data['con'] = ability_list[3]
        player_data['int'] = ability_list[2]
        player_data['wis'] = ability_list[1]
        player_data['cha'] = ability_list[5]
    elif clss == "Wizard":
        player_data['str'] = ability_list[0]
        player_data['dex'] = ability_list[3]
        player_data['con'] = ability_list[4]
        player_data['int'] = ability_list[5]
        player_data['wis'] = ability_list[2]
        player_data['cha'] = ability_list[1]
    elif clss == "Paladin":
        player_data['str'] = ability_list[4]
        player_data['dex'] = ability_list[2]
        player_data['con'] = ability_list[3]
        player_data['int'] = ability_list[0]
        player_data['wis'] = ability_list[1]
        player_data['cha'] = ability_list[5]
    elif clss == "Monk":
        player_data['str'] = ability_list[2]
        player_data['dex'] = ability_list[5]
        player_data['con'] = ability_list[3]
        player_data['int'] = ability_list[1]
        player_data['wis'] = ability_list[4]
        player_data['cha'] = ability_list[0]
    elif clss == "Fighter":
        player_data['str'] = ability_list[5]
        player_data['dex'] = ability_list[2]
        player_data['con'] = ability_list[4]
        player_data['int'] = ability_list[1]
        player_data['wis'] = ability_list[3]
        player_data['cha'] = ability_list[0]
    elif clss == "Druid":
        player_data['str'] = ability_list[0]
        player_data['dex'] = ability_list[3]
        player_data['con'] = ability_list[4]
        player_data['int'] = ability_list[2]
        player_data['wis'] = ability_list[5]
        player_data['cha'] = ability_list[1]
    elif clss == "Cleric":
        player_data['str'] = ability_list[1]
        player_data['dex'] = ability_list[3]
        player_data['con'] = ability_list[4]
        player_data['int'] = ability_list[0]
        player_data['wis'] = ability_list[5]
        player_data['cha'] = ability_list[2]


# Generates and stores each ability modifier
def gen_ability_mods():
    for key in list(player_data):
        if key in abilities:
            value = player_data.get(key)
            if value == 10:
                ability_mod = 0
            elif value > 10:
                ability_mod = (value - 10) // 2
            elif value < 10:
                ability_mod = -1
            player_data[key + "_mod"] = ability_mod


def add_race_mods(race):
    if race == "Dragonborn":
        player_data['str'] += 2
        player_data['cha'] += 1
    elif race == "Dwarf":
        player_data['con'] += 2
    elif race == "Elf":
        player_data['dex'] += 2
    elif race == "Gnome":
        player_data['int'] += 2
    elif race == "Half Elf":
        player_data['cha'] += 2
        print("As a Half Elf, you can choose two abilities to increase by 1\n"
              "Or you can increase 1 ability by two\n"
              "Your current scores are: ")
        for key, value in player_data.items():
            if key in abilities:
                print(key + ":", value)
        input1 = input("What is your first pick? (Ex. str, dex, con...)\n").lower()
        input2 = input("What is your second pick?\n").lower()
        if input1 and input2 in abilities:
            player_data[input1] += 1
            player_data[input2] += 1
    elif race == "Half Orc":
        player_data['str'] += 2
        player_data['con'] += 1
    elif race == "Halfling":
        player_data['dex'] += 2
    elif race == "Human":
        player_data['str'] += 1
        player_data['dex'] += 1
        player_data['con'] += 1
        player_data['int'] += 1
        player_data['wis'] += 1
        player_data['cha'] += 1
    elif race == "Tiefling":
        player_data['cha'] += 2
        player_data['int'] += 1


def add_skills(skills_list):
    i = 0
    while i < len(skills_list):
        player_data['skill_prof' + str(i)] = skills_list[i]
        i += 1
    save_playerdata(player_data.get('name'))


# Saves player data to new file if it doesn't exist already
# If it does, it asks to player to overwrite it or save as a new copy ("COPY_Player_Data.csv")
def save_playerdata(name):
    filename = str(name) + "_Data.csv"
    if os.path.exists(dir_path + "/PlayerData/" + filename):
        print("File Already Exists")
        response = input("Would you like to overwrite it or save as a new copy?\n"
                         "Type 'overwrite' or 'new copy'\n").lower()
        if response == "overwrite":
            w = csv.writer(open(dir_path + "/PlayerData/" + filename, "w"))
            for key, val in player_data.items():
                w.writerow([key, val])
            print("Player Data Saved")
        elif response == "new copy":
            w = csv.writer(open(dir_path + "/PlayerData/COPY_" + filename, "w"))
            for key, val in player_data.items():
                w.writerow([key, val])
            print("Player Data Saved")
        else:
            print("Please Enter Valid Command")
    else:
        w = csv.writer(open(dir_path + "/PlayerData/" + filename, "w"))
        for key, val in player_data.items():
            w.writerow([key, val])
        print("Player Data Saved")

