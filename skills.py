import os
import csv
import dndchar

dir_path = os.path.dirname(os.path.realpath(__file__))

# Default proficiency bonus
proficiency_bonus = 2

# List of all skills with empty modifiers by default
player_skills = {'Acrobatics': '', 'Animal Handling': '', 'Athletics': '', 'Arcana': '',
                 'Deception': '', 'History': '', 'Insight': '', 'Intimidation': '',
                 'Investigation': '', 'Medicine': '', 'Nature': '', 'Perception': '',
                 'Performance': '', 'Persuasion': '', 'Religion': '', 'Slight of Hand': '',
                 'Stealth': '', 'Survival': '', 'Strength Saving Throws': '', 'Dexterity Saving Throws': '',
                 'Constitution Saving Throws': '', 'Intelligence Saving Throws': '',
                 'Wisdom Saving Throws': '', 'Charisma Saving Throws': ''}
player_proficiencies = {}

# Ability Abbreviations
ability_mods = ['str_mod', 'dex_mod', 'con_mod', 'int_mod', 'wis_mod', 'cha_mod']

# Skills
skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'Arcana',
          'Deception', 'History', 'Insight',
          'Intimidation', 'Investigation', 'Medicine',
          'Nature', 'Perception', 'Performance',
          'Persuasion', 'Religion', 'Slight of Hand',
          'Stealth', 'Survival']

str_skills = ['Strength Saving Throws', 'Athletics']
dex_skills = ['Dexterity Saving Throws', 'Acrobatics', 'Slight of Hand', 'Stealth']
con_skills = ['Constitution Saving Throws']
int_skills = ['Intelligence Saving Throws', 'Arcana', 'History', 'Investigation', 'Nature', 'Religion']
wis_skills = ['Wisdom Saving Throws', 'Animal Handling', 'Insight', 'Medicine', 'Perception', 'Survival']
cha_skills = ['Charisma Saving Throws', 'Deception', 'Intimidation', 'Performance', 'Persuasion']

saves = ['Strength Saving Throws', 'Dexterity Saving Throws', 'Constitution Saving Throws',
         'Intelligence Saving Throws', 'Wisdom Saving Throws', 'Charisma Saving Throws']

# Skills that each class can choose from
barb_skills = ['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival']
cleric_skills = ['History', 'Insight', 'Medicine', 'Persuasion', 'Religion']
druid_skills = ['Arcana', 'Animal Handling', 'Insight', 'Medicine', 'Nature', 'Perception', 'Religion', 'Survival']
fighter_skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'History',
                  'Insight', 'Intimidation', 'Perception', 'Survival']
monk_skills = ['Acrobatics', 'Athletics', 'History', 'Insight', 'Religion', 'Stealth']
paladin_skills = ['Athletics', 'Insight', 'Intimidation', 'Medicine', 'Persuasion', 'Religion']
ranger_skills = ['Animal Handling', 'Athletics', 'Insight', 'Investigation',
                 'Nature', 'Perception', 'Stealth', 'Survival']
rogue_skills = ['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation',
                'Investigation', 'Perception', 'Performance', 'Persuasion', 'Sleight of Hand', 'Stealth']
sorcerer_skills = ['Arcana', 'Deception', 'Insight', 'Intimidation', 'Persuasion', 'Religion']
warlock_skills = ['Arcana', 'Deception', 'History', 'Intimidation', 'Investigation', 'Nature', 'Religion']
wizard_skills = ['Arcana', 'History', 'Insight', 'Investigation', 'Medicine', 'Religion']


# Let users choose proficient skills based on class
def gen_skills(clss):
    if clss == "Barbarian":
        print("Choose two from " + ', '.join(barb_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in barb_skills:
            skill_list = [saves[0], saves[2], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[0]
            player_proficiencies['proficient_skill2'] = saves[2]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Bard":
        print("Choose any three to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        if choice1 and choice2 and choice3 in skills:
            skill_list = [saves[1], saves[2], choice1, choice2, choice3]
            player_proficiencies['proficient_skill1'] = saves[1]
            player_proficiencies['proficient_skill2'] = saves[2]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
            player_proficiencies['proficient_skill5'] = choice3
        else:
            print("Please Enter Valid Skills")
    elif clss == "Cleric":
        print("Choose two from " + ', '.join(cleric_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in cleric_skills:
            skill_list = [saves[4], saves[5], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[4]
            player_proficiencies['proficient_skill2'] = saves[5]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Druid":
        print("Choose two from " + ', '.join(druid_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in druid_skills:
            skill_list = [saves[3], saves[4], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[3]
            player_proficiencies['proficient_skill2'] = saves[4]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Fighter":
        print("Choose two from " + ', '.join(fighter_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in fighter_skills:
            skill_list = [saves[0], saves[2], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[0]
            player_proficiencies['proficient_skill2'] = saves[2]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Monk":
        print("Choose two from " + ', '.join(monk_skills) + " to be proficient in")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in monk_skills:
            skill_list = [saves[0], saves[1], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[0]
            player_proficiencies['proficient_skill2'] = saves[1]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Paladin":
        print("Choose two from " + ', '.join(paladin_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in paladin_skills:
            skill_list = [saves[4], saves[5], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[4]
            player_proficiencies['proficient_skill2'] = saves[5]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Ranger":
        print("Choose three from " + ', '.join(ranger_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        if choice1 and choice2 and choice3 in ranger_skills:
            skill_list = [saves[0], saves[1], choice1, choice2, choice3]
            player_proficiencies['proficient_skill1'] = saves[0]
            player_proficiencies['proficient_skill2'] = saves[1]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
            player_proficiencies['proficient_skill5'] = choice3
        else:
            print("Please Enter Valid Skills")
    elif clss == "Rogue":
        print("Choose four from " + ', '.join(rogue_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        choice4 = input("Fourth Choice?\n").title()
        if choice1 and choice2 and choice3 and choice4 in rogue_skills:
            skill_list = [saves[1], saves[3], choice1, choice2, choice3, choice4]
            player_proficiencies['proficient_skill1'] = saves[1]
            player_proficiencies['proficient_skill2'] = saves[3]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
            player_proficiencies['proficient_skill5'] = choice3
            player_proficiencies['proficient_skill6'] = choice4
        else:
            print("Please Enter Valid Skills")
    elif clss == "Sorcerer":
        print("Choose two from " + ', '.join(sorcerer_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in sorcerer_skills:
            skill_list = [saves[2], saves[5], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[2]
            player_proficiencies['proficient_skill2'] = saves[5]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Warlock":
        print("Choose two from " + ', '.join(warlock_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in warlock_skills:
            skill_list = [saves[4], saves[5], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[4]
            player_proficiencies['proficient_skill2'] = saves[5]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")
    elif clss == "Wizard":
        print("Choose two from " + ', '.join(wizard_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in wizard_skills:
            skill_list = [saves[3], saves[4], choice1, choice2]
            player_proficiencies['proficient_skill1'] = saves[3]
            player_proficiencies['proficient_skill2'] = saves[4]
            player_proficiencies['proficient_skill3'] = choice1
            player_proficiencies['proficient_skill4'] = choice2
        else:
            print("Please Enter Valid Skills")


# Adds skill modifiers to CSV
def skill_mods(name, dict):
    for key in list(dict):
        if key in ability_mods:
            value = dict.get(key)
            if key == "str_mod":
                for skill in str_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
            elif key == "dex_mod":
                for skill in dex_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
            elif key == "con_mod":
                for skill in con_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
            elif key == "int_mod":
                for skill in int_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
            elif key == "wis_mod":
                for skill in wis_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
            elif key == "cha_mod":
                for skill in cha_skills:
                    if skill in player_proficiencies.values():
                        player_skills[skill] += str(value + proficiency_bonus)
                    else:
                        player_skills[skill] += str(value)
    save_playerdata(name)


# Saves data to CSV
def save_playerdata(name):
    filename = str(name) + "_Skills.csv"
    if os.path.exists(dir_path + "/PlayerData/" + filename):
        print("File Already Exists")
        response = input("Would you like to overwrite it or save as a new copy?\nType 'overwrite' or 'new copy'\n").lower()
        if response == "overwrite" or response == "ow":
            w = csv.writer(open(dir_path + "/PlayerData/" + name + "/" + filename, "w"))
            for key, val in player_skills.items():
                w.writerow([key, val])
            for key, val in player_proficiencies.items():
                w.writerow([key, val])
            print("Player Skills Saved")
        elif response == "new copy" or response == "nc":
            w = csv.writer(open(dir_path + "/PlayerData/" + name + "/COPY_" + filename, "w"))
            for key, val in player_skills.items():
                w.writerow([key, val])
            for key, val in player_proficiencies.items():
                w.writerow([key, val])
            print("Player Skills Saved")
        else:
            print("Please Enter Valid Command")
    else:
        w = csv.writer(open(dir_path + "/PlayerData/" + name + "/" + filename, "w"))
        for key, val in player_skills.items():
            w.writerow([key, val])
        for key, val in player_proficiencies.items():
            w.writerow([key, val])
        print("Player Skills Saved")
