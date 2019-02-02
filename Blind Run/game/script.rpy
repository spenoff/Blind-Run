# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#define e = Character("Eileen")
define narrator = Character("Narrator")
define witch_voice = Character("???", what_color="#41d846")
define witch = Character("Witch", what_color="#41d846")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Forest Entrance

    #variables
    python:
        blind = False
        entered_poison = False
        cub_found = False
        spaces_entered = -1
        poison_direction = -1 #0 if entered from one_three, 1 if entered from two_four

    # These display lines of dialogue.
    narrator "You approach the forrest."
    witch_voice "Hehehe"
    show witch at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
    witch "So you are here in search of the treasure!"
    witch "I will tell you, it is not very far from here."
    witch "However, if you wish the retrieve the treasure, you must know your way around the forest."
    witch "You must therefore pass my test."
    narrator "The witch casted a spell on you"
    witch "In three minutes, starting from when you enter the forest, you will become blind!"
    witch "Good luck!"
    witch "Hehehe"
    scene Forest
    narrator "You have entered the forest. The journey begins!"

    jump one_two

label one_one:
    python:
        spaces_entered += 1

label one_two:
    narrator "Where will you go?"
    python:
        spaces_entered += 1
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
    narrator "Where will you go?"
    python:
        spaces_entered += 1

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
    if not entered_poison:
        if poison_direction == 0:
            narrator "This area is filled with poison gas! Did you not read the sign?"
            narrator "You barely escape alive."

            python:
                entered_poison = True

            jump one_three

        elif poison_direction = 1:
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

label two_two:
    python:
        spaces_entered += 1
