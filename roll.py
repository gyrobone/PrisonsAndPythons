import random


def roll_dice(dice_input):
    type_of_dice = dice_input[2:]
    mod = 0

    try:
        number_of_dice = int(dice_input[0])
    except ValueError:
        print("Please Enter Valid Number of Dice")

    if dice_input[1] == "d":
        if len(dice_input) > 3:
            if dice_input[3] == "+":
                mod = dice_input[4:]
                type_of_dice = dice_input[2]
        if len(dice_input) > 4:
            if dice_input[4] == "+":
                mod = dice_input[5:]
                type_of_dice = dice_input[2:4]
        if len(dice_input) > 5:
            if dice_input[5] == "+":
                mod = dice_input[6:]
                type_of_dice = dice_input[2:5]

        try:
            number = int(type_of_dice)
        except ValueError:
            print("Type of Dice Error")
            return
        try:
            modifier = int(mod)
        except ValueError:
            print("Modifier Error")
            return
    else:
        print("Not a Valid Dice")

    roll_sum = 0
    while number_of_dice > 0:
        roll = random.randint(1, number)
        roll_sum += roll
        number_of_dice -= 1

    output = roll_sum + modifier
    print(output)

