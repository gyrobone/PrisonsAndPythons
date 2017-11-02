import csv
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

invalid_chars = "1234567890!@#$%^&*()_+-=[]{}\|;:'\",<.>/?"

player_data = {}

# These are the valid races and classes that can be specified
valid_races = ['Dragonborn', 'Dwarf', 'Elf', 'Gnome', 'Half Elf', 'Half Orc', 'Halfling', 'Human', 'Tiefling']
valid_classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']


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
    gen_stats(clss)
    save_playerdata(name)


# Generates random attribute scores, assigns to best spot
# based on race and class, and calculates modifiers
def gen_stats(clss):
    # Generates list of 6 numbers and sorts from low to high
    number_list = []
    i = 0
    while i <= 6:
        number = random.randint(8, 18)
        number_list.append(number)
        i += 1
    attrib_list = sorted(number_list)

    # Character optimization
    if clss == "Barbarian":
        str_attrib(attrib_list[5])
        dex_attrib(attrib_list[4])
        con_attrib(attrib_list[3])
        int_attrib(attrib_list[0])
        wis_attrib(attrib_list[2])
        cha_attrib(attrib_list[1])
    elif clss == "Rogue" or clss == "Ranger":
        str_attrib(attrib_list[0])
        dex_attrib(attrib_list[5])
        con_attrib(attrib_list[4])
        int_attrib(attrib_list[1])
        wis_attrib(attrib_list[3])
        cha_attrib(attrib_list[2])
    else:
        str_attrib(attrib_list[5])
        dex_attrib(attrib_list[4])
        con_attrib(attrib_list[3])
        int_attrib(attrib_list[2])
        wis_attrib(attrib_list[1])
        cha_attrib(attrib_list[0])

# These all assign abilities and their modifiers to the player_data list to be saved later
def str_attrib(str):
    if str == 10:
        str_mod = 0
    elif str > 10:
        str_mod = (str - 10) // 2
    elif str < 10:
        str_mod = -1

    player_data['str'] = str
    player_data['str_mod'] = str_mod


def dex_attrib(dex):
    if dex == 10:
        dex_mod = 0
    elif dex > 10:
        dex_mod = (dex - 10) // 2
    elif dex < 10:
        dex_mod = -1

    player_data['dex'] = dex
    player_data['dex_mod'] = dex_mod


def con_attrib(con):
    if con == 10:
        con_mod = 0
    elif con > 10:
        con_mod = (con - 10) // 2
    elif con < 10:
        con_mod = -1

    player_data['con'] = con
    player_data['con_mod'] = con_mod


def int_attrib(int):
    if int == 10:
        int_mod = 0
    elif int > 10:
        int_mod = (int - 10) // 2
    elif int < 10:
        int_mod = -1

    player_data['int'] = int
    player_data['int_mod'] = int_mod


def wis_attrib(wis):
    if wis == 10:
        wis_mod = 0
    elif wis > 10:
        wis_mod = (wis - 10) // 2
    elif wis < 10:
        wis_mod = -1

    player_data['wis'] = wis
    player_data['wis_mod'] = wis_mod


def cha_attrib(cha):
    if cha == 10:
        cha_mod = 0
    elif cha > 10:
        cha_mod = (cha - 10) // 2
    elif cha < 10:
        cha_mod = -1

    player_data['cha'] = cha
    player_data['cha_mod'] = cha_mod


# Saves player data to new file if it doesn't exist already
# If it does, it asks to player to overwrite it or save as a new copy ("COPY_Player_Data.csv")
def save_playerdata(name):
    filename = str(name) + "_Data.csv"
    if os.path.exists(dir_path + "/PlayerData/" + filename):
        print("File Already Exists")
        response = input("Would you like to overwrite it or save as a new copy?\nType 'overwrite' or 'new copy'\n").lower()
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

