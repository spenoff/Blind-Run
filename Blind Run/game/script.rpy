# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define narrator = Character("Narrator")
define witch_voice = Character("???", what_color="#41d846")
define witch = Character("Witch", what_color="#41d846")
define treasure_chest = Character()
define max_time = 120
define show_blindness_time = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Forest Entrance


    python:
        #variables
        blind = False
        entered_poison = False
        cub_found = False
        treasure_chest_discovered = False
        treasure_key_obtained = False
        #spaces_entered = -1
        blindness_time = 130
        poison_direction = -1 #0 if entered from one_three, 1 if entered from two_four
        sub_time = 10

        #methods
        def bindness_time_overlay():
            if show_blindness_time:
                ui.frame()
                ui.vbox()
                ui.text("Time until blindness")
                ui.bar(max_time, blindness_time, xmaximum=120)
                ui.close()


        config.overlay_functions.append(bindness_time_overlay)


    narrator "You approach the forrest."
    witch_voice "Hehehe"
    show witch at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    witch "So you are here in search of the treasure!"
    witch "I will tell you, it is not very far from here."
    witch "However, if you wish the retrieve the treasure, you must know your way around the forest."
    witch "You must therefore pass my test."
    narrator "The witch casted a spell on you"
    witch "In two minutes, starting from when you enter the forest, you will become blind!"
    witch "Good luck!"
    witch "Hehehe"
    scene Forest
    $ show_blindness_time=True
    narrator "You have entered the forest. The journey begins!"

    jump one_two

label one_one:
    python:
        blindness_time -= sub_time
        treasure_chest_discovered = True

    if not blind:
        $ show_blindness_time=True


    show treasure_chest

    if blind:
        narrator "You can feel the treasure chest."
    else:
        narrator "You found the treasure chest!"

    narrator "You try to open it."

    if treasure_key_obtained:
        narrator "But wait! You have the key!"
        narrator "You unlock the treasure chest and open it"
        narrator "Congratulations! You found the treasure"
        narrator "Thank you so much for playing our game!"
        return
    else:
        narrator "But it is locked!"
        narrator "You must find the key!"
        narrator "Where will you go?"

    if not blind:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump two_one

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump one_two

label one_two:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump two_two

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump one_one

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump one_three

label one_three:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump two_three

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump one_two

            "right":
                python:
                    poison_direction = 0

                narrator "You move rightward. 10 seconds pass."
                jump one_four

label one_four:
    python:
        blindness_time -= sub_time

    if not entered_poison:

        if poison_direction == 0:
            narrator "This area is filled with poison gas! Did you not read the sign?"
            narrator "You barely escape alive."

            python:
                entered_poison = True

            jump one_three

        elif poison_direction == 1:
            narrator "This area is filled with poison gas!"
            narrator "You barely escape alive."

            python:
                entered_poison = True

            jump two_four

    else:
        narrator "This area is filled with poison gas!"
        narrator "You did not survive this time."
        narrator "GAME OVER"
        return

label two_one:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_one

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_two

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_one

label two_two:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_two

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump two_one

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_three

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_two

label two_three:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_three

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump two_two

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_four

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_three

label two_four:
    python:
        blindness_time -= sub_time

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump two_three

            "downward":
                python:
                    poison_direction = 1

                narrator "You move downward. 10 seconds pass."
                jump one_four
