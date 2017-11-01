import csv
import random
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
invalid_chars = "1234567890!@#$%^&*()_+-=[]{}\|;:'\",<.>/?"
player_data = {}


def create_char(name, char_name):
    # Check if character name as any invalid characters
    for i in range(0, len(invalid_chars)):
        if invalid_chars[i] in name:
            print("Invalid Name")
            return

    # Set player name
    player_data['name'] = name
    player_data['char_name'] = char_name
    gen_stats()
    save_playerdata(name)


# Generates random attribute scores, assigns to best spot
# based on race and class, and calculates modifiers
def gen_stats(race=1, cls=1):
    str_attrib()
    dex_attrib()
    con_attrib()
    int_attrib()
    wis_attrib()
    cha_attrib()


def str_attrib():
    str = random.randint(8,18)
    if str == 10:
        str_mod = 0
    elif str > 10:
        str_mod = (str - 10)//2
    elif str < 10:
        str_mod = -1

    player_data['str'] = str
    player_data['str_mod'] = str_mod


def dex_attrib():
    dex = random.randint(8, 18)
    if dex == 10:
        dex_mod = 0
    elif dex > 10:
        dex_mod = (dex - 10) // 2
    elif dex < 10:
        dex_mod = -1

    player_data['dex'] = dex
    player_data['dex_mod'] = dex_mod


def con_attrib():
    con = random.randint(8, 18)
    if con == 10:
        con_mod = 0
    elif con > 10:
        con_mod = (con - 10) // 2
    elif con < 10:
        con_mod = -1

    player_data['con'] = con
    player_data['con_mod'] = con_mod


def int_attrib():
    int = random.randint(8, 18)
    if int == 10:
        int_mod = 0
    elif int > 10:
        int_mod = (int - 10) // 2
    elif int < 10:
        int_mod = -1

    player_data['int'] = int
    player_data['int_mod'] = int_mod


def wis_attrib():
    wis = random.randint(8, 18)
    if wis == 10:
        wis_mod = 0
    elif wis > 10:
        wis_mod = (wis - 10) // 2
    elif wis < 10:
        wis_mod = -1

    player_data['wis'] = wis
    player_data['wis_mod'] = wis_mod


def cha_attrib():
    cha = random.randint(8, 18)
    if cha == 10:
        cha_mod = 0
    elif cha > 10:
        cha_mod = (cha - 10) // 2
    elif cha < 10:
        cha_mod = -1

    player_data['cha'] = cha
    player_data['cha_mod'] = cha_mod


def save_playerdata(name):
    # Check if CSV file exists, if not, save player data in CSV file
    filename = str(name) + "_Data.csv"
    w = csv.writer(open(dir_path + "/PlayerData/" + filename, "w"))
    for key, val in player_data.items():
        w.writerow([key, val])
    print("Player Data Saved")

