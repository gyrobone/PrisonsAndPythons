import dndchar
import roll
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
ascii_art = """\
                                       ..
                                     ,o"\"""o
                                  ,o$"     o
                               ,o$$$                                 
                             ,o$$$'
                           ,o$"o$'
                         ,o$$"$"'   
                      ,o$"$o"$"'    
                   ,oo$"$"$"$"$$`                      ,oooo$$$$$$$$oooooo.  
                ,o$$$"$"$"$"$"$"o$`..             ,$o$"$$"$"'            `oo.o
             ,oo$$$o"$"$"$"$  $"$$$"$`o        ,o$$"o$$$o$'                 `o
          ,o$"$"$o$"$"$"$  $"$$o$$o $$o`o   ,$$$$$o$"$$o'                    $
        ,o"$$"'  `$"$o$" o$o$o"  $$$o$o$oo"$$$o$"$$"$o"'                     $
     ,o$"'        `"$ "$$o$$" $"$o$o$$"$o$$o$o$o"$"$"`""o                   ' 
   ,o$'          o$ `"$"$o "$o$$o$$$"$$$o"$o$$o"$$$    `$$  
  ,o'           (     `" o$"$o"$o$$$"$o$"$"$o$"$$"$ooo|  `` 
 $"$             `    (   `"o$$"$o$o$$ "o$o"   $o$o"$"$    )
(  `                   `    `o$"$$o$" "o$$     "o /|"$o"
 `                           `$o$$$$"" o$      "o$\|"$o'
                              `$o"$"$ $ "       `"$"$o$
                               "$$"$$ "oo         ,$""$ 
                               $"$o$$""o"          ,o$"$
                               $$"$$"$ "o           `,",
                     ,oo$oo$$$$$$"$o$$$ ""o           
                  ,o$$"o"o$o$$o$$$"$o$$oo"oo
                ,$"oo"$$$$o$$$$"$$$o"o$o"o"$o o
               ,$$$""$$o$,      `$$$$"$$$o""$o $o               
               $o$o$"$,          `$o$"$o$o"$$o$ $$o             
              $$$o"o$$           ,$$$$o$$o"$"$$ $o$$oo      ,   
              "$o$$$ $`.        ,"$$o$"o$""$$$$ `"$o$$oo    `o
              `$o$o$"$o$o`.  ,.$$"$o$$"$$"o$$$$   `$o$$ooo    $$ooooooo
                `$o$"$o"$"$$"$$"$"$$o$$o"$$o"        `"$o$o            `"o
                   `$$"$"$o$$o$"$$"$ $$$  $ "           `$"$o            `o
                      `$$"o$o"$o"$o$ "  o $$$o            `$$"o          ,$
                         (" ""$""\"     o"" "o$o             `$$ooo     ,o$$
                              $$""\"o   (   "$o$$$"o            `$o$$$o$"$'
                                ) ) )           )  ) )            ` "'
 """
print(ascii_art)

while True:
    print("Welcome to the DND Python Console")
    print("----------------------------------------------------------------------------------------------")
    user_input = input("Please Enter A Command (Type 'help' for commands):\n").lower()
    split = user_input.split()

    if user_input == "create character":
        name_input = input("Player's Name?\n").title()
        char_input = input("Characters's Name?\n").title()
        race_input = input("Character's Race?\n").title()
        class_input = input("Character's Class?\n").title()
        dndchar.create_char(name_input, char_input, race_input, class_input)
    elif user_input == "path":
        print(dir_path)
    elif user_input == "help":
        print("----------------------------------------------------------------------------------------------")
        print("Help\n-This command lists all usable commands")
        print("Create Character\n-This command creates a new character and asks for the characters information\n-Then it saves to a CSV file in the PlayerData folder")
        print("Exit\n-Exits the program")
        print("Test\n-Creates a test Half Orc Barbarian character")
        print("Roll\n-Roll any number of dice and add modifiers\n-Ex: roll 1d12+4")
    elif user_input == "exit":
        print("Goodbye")
        break
    elif user_input == "test":
        dndchar.create_char('Test', 'Test', 'Half Orc', 'Barbarian')
    elif split[0] == "roll" or split[0] == "Roll":
        dice = split[1]
        roll.roll_dice(dice)
    else:
        print("Please Enter Valid Command")

