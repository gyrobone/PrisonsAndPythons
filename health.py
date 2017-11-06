import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

player_health = {}
player_ac = {}


# Sets players hit dice based on class
def set_hit_dice(name, clss, dict):
    for key in list(dict):
        if key == 'con_mod':
            con = dict.get(key)
        if key == 'dex_mod':
            dex = dict.get(key)

    if clss == "Barbarian":
        player_health['hit_dice'] = '1d12'
        player_health['initial_health'] = str(12 + int(con))
    elif clss == "Fighter" or clss == "Ranger" or clss == "Paladin":
        player_health['hit_dice'] = '1d10'
        player_health['initial_health'] = str(10 + int(con))
    elif clss == "Sorcerer" or clss == "Wizard":
        player_health['hit_dice'] = '1d6'
        player_health['initial_health'] = str(6 + int(con))
    elif clss == "Rogue" or clss == "Monk" or clss == "Druid" or clss == "Cleric" or clss == "Bard" or clss == "Warlock":
        player_health['hit_dice'] = '1d8'
        player_health['initial_health'] = str(8 + int(con))

    player_ac['unarmored_ac'] = 10 + int(dex)
    save_playerdata(name)


def set_ac():
    pass


def save_playerdata(name):
    filename = str(name) + "_Health.csv"
    if os.path.exists(dir_path + "/PlayerData/" + filename):
        print("File Already Exists")
        response = input("Would you like to overwrite it or save as a new copy?\nType 'overwrite' or 'new copy'\n").lower()
        if response == "overwrite":
            w = csv.writer(open(dir_path + "/PlayerData/" + name + "/" + filename, "w"))
            for key, val in player_health.items():
                w.writerow([key, val])
            for key, val in player_ac.items():
                w.writerow([key, val])
            print("Player Health Saved")
        elif response == "new copy":
            w = csv.writer(open(dir_path + "/PlayerData/" + name + "/COPY_" + filename, "w"))
            for key, val in player_health.items():
                w.writerow([key, val])
            for key, val in player_ac.items():
                w.writerow([key, val])
            print("Player Health Saved")
        else:
            print("Please Enter Valid Command")
    else:
        w = csv.writer(open(dir_path + "/PlayerData/" + name + "/" + filename, "w"))
        for key, val in player_health.items():
            w.writerow([key, val])
        for key, val in player_ac.items():
            w.writerow([key, val])
        print("Player Health Saved")
