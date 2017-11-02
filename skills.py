import os
import csv
import dndchar

dir_path = os.path.dirname(os.path.realpath(__file__))

player_skills = {}

# Skills
skills = ['Acrobatics', 'Animal Handling', 'Athletics', 'Arcana',
          'Deception', 'History', 'Insight',
          'Intimidation', 'Investigation', 'Medicine',
          'Nature', 'Perception', 'Performance',
          'Persuasion', 'Religion', 'Slight of Hand',
          'Stealth', 'Survival']

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
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Bard":
        print("Choose any three to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        if choice1 and choice2 and choice3 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Cleric":
        print("Choose two from " + ', '.join(cleric_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Druid":
        print("Choose two from " + ', '.join(druid_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Fighter":
        print("Choose two from " + ', '.join(fighter_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Monk":
        print("Choose two from " + ', '.join(monk_skills) + " to be proficient in")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Paladin":
        print("Choose two from " + ', '.join(paladin_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Ranger":
        print("Choose three from " + ', '.join(ranger_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        if choice1 and choice2 and choice3 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Rogue":
        print("Choose four from " + ', '.join(rogue_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        choice3 = input("Third Choice?\n").title()
        choice4 = input("Fourth Choice?\n").title()
        if choice1 and choice2 and choice3 and choice4 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Sorcerer":
        print("Choose two from " + ', '.join(sorcerer_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Warlock":
        print("Choose two from " + ', '.join(warlock_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")
    elif clss == "Wizard":
        print("Choose two from " + ', '.join(wizard_skills) + " to be proficient in:")
        choice1 = input("First Choice?\n").title()
        choice2 = input("Second Choice?\n").title()
        if choice1 and choice2 in skills:
            skill_list = [choice1, choice2]
            dndchar.add_skills(skill_list)
        else:
            print("Please Enter Valid Skills")


'''
def save_playerdata(name):
    filename = str(name) + "_Skills.csv"
    if os.path.exists(dir_path + "/PlayerData/" + filename):
        print("File Already Exists")
        response = input("Would you like to overwrite it or save as a new copy?\nType 'overwrite' or 'new copy'\n").lower()
        if response == "overwrite":
            w = csv.writer(open(dir_path + "/PlayerData/" + filename, "w"))
            for key, val in player_skills.items():
                w.writerow([key, val])
            print("Player Data Saved")
        elif response == "new copy":
            w = csv.writer(open(dir_path + "/PlayerData/COPY_" + filename, "w"))
            for key, val in player_skills.items():
                w.writerow([key, val])
            print("Player Data Saved")
        else:
            print("Please Enter Valid Command")
    else:
        w = csv.writer(open(dir_path + "/PlayerData/" + filename, "w"))
        for key, val in player_skills.items():
            w.writerow([key, val])
        print("Player Data Saved")
'''