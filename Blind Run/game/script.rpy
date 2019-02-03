# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character("Narrator")
define witch_voice = Character("???", what_color="#41d846")
define witch = Character("Witch", what_color="#41d846")
define lion = Character("Lion")
define cub = Character("Cub")
define cub_voice = Character("???")
define treasure_chest = Character("treasure_chest.png", image=True)
define max_time = 120
define show_blindness_time = False
define blind = False
define said_no_to_cub = False

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    scene bg forest

    python:
        #variables
        has_become_blind = False
        entered_poison = False
        cub_found = False
        cub_returned = False
        treasure_chest_discovered = False
        treasure_key_obtained = False
        spoken_to_lion = False
        blindness_time = 130
        poison_direction = -1 #0 if entered from one_three, 1 if entered from two_four
        lion_direction = -1 #0 if entered from two_one, 1 if entered from four_one, 2 if entered from three_two
        sub_time = 10

        #methods
        def blindness_time_overlay():
            if show_blindness_time:
                ui.frame()
                ui.vbox()
                ui.text("Time until blindness")
                ui.bar(max_time, blindness_time, xmaximum=120)
                ui.close()


        config.overlay_functions.append(blindness_time_overlay)

        def time_is_up(time):
            if time == 0 and not has_become_blind:
                return True
            else:
                return False


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
    hide witch
    #scene Forest
    $ show_blindness_time=True
    narrator "You have entered the forest. The journey begins!"

    jump one_two

label one_one:
    python:
        blindness_time -= sub_time
        treasure_chest_discovered = True

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if blind:
        narrator "You can feel the treasure chest."
    else:
        show treasure_chest at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
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
                hide treasure_chest
                narrator "You move forward. 10 seconds pass."
                jump two_one

            "right":
                hide treasure_chest
                narrator "You move rightward. 10 seconds pass."
                jump one_two
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump two_one

            "right":
                narrator "You move rightward."
                jump one_two

            "left":
                narrator "You move leftward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump one_one

            "downward":
                narrator "You move downward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump one_one

label one_two:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    narrator "Where will you go?"

    if not blind:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump two_two

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump one_three

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump one_one
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump two_two

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump one_three

            "left":
                narrator "You move leftward."
                jump one_one

            "downward":
                narrator "You move downward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump one_two

label one_three:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump two_three

            "right":
                python:
                    poison_direction = 0
                narrator "You move rightward. 10 seconds pass."
                jump one_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump one_two
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump two_three

            "right":
                python:
                    poison_direction = 0
                narrator "You move rightward."
                jump one_four

            "left":
                narrator "You move leftward."
                jump one_two

            "downward":
                narrator "You move downward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump one_three

label one_four:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not entered_poison:

        if poison_direction == 0:
            narrator "This area is filled with poison gas! Did you not read the sign?"
            if blind:
                narrator "You have died from poison gas."
                narrator "GAME OVER"
                return
            narrator "You barely escape alive."

            python:
                entered_poison = True

            jump one_three

        elif poison_direction == 1:
            narrator "This area is filled with poison gas!"
            if blind:
                narrator "You have died from poison gas."
                narrator "GAME OVER"
                return
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

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                python:
                    lion_direction = 0
                narrator "You move forward. 10 seconds pass."
                jump three_one

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_two

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_one
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                python:
                    lion_direction = 0
                narrator "You move forward."
                jump three_one

            "right":
                narrator "You move rightward."
                jump two_two

            "left":
                narrator "You move leftward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump two_one

            "downward":
                narrator "You move downward."
                jump one_one

label two_two:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_two

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_three

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump two_one

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_two
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump three_two

            "right":
                narrator "You move rightward."
                jump two_three

            "left":
                narrator "You move leftward."
                jump two_one

            "downward":
                narrator "You move downward."
                jump one_two

label two_three:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    narrator "Where will you go?"

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump three_three

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump two_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump two_two

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump one_three
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump three_three

            "right":
                narrator "You move rightward."
                jump two_four

            "left":
                narrator "You move leftward."
                jump two_two

            "downward":
                narrator "You move downward."
                jump one_three

label two_four:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

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
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump three_four

            "right":
                narrator "You move rightward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump two_four

            "left":
                narrator "You move leftward."
                jump two_three

            "downward":
                python:
                    poison_direction = 1

                narrator "You move downward."
                jump one_four

label three_one:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if blind:
        narrator "You bump into a lion."
    else:
        narrator "You find a lion."
        show lion at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

    if not treasure_chest_discovered and not cub_found:
        narrator "You run away safely."
        hide lion
        if lion_direction == 0:
            jump two_one
        elif lion_direction == 1:
            jump four_one
        elif lion_direction == 2:
            jump three_two
        else:
            narrator "uhhh you go down"
            jump two_one
    elif not spoken_to_lion:
        narrator "He doesn't seem dangerous. Maybe he can help you find the key."
        menu:
            narrator "What should you do?"

            "Ask him about the key":
                lion "What do you want?"
                menu:
                    lion "What do you want?"

                    "I'm looking for the key to the treasure":
                        lion "Well, you have come to the right place."
                        lion "I am the keeper of the key to the treasure."
                        lion "I normally would fight those who came for the key."
                        lion "But unfortunately, I'm not in the mood today, for I have lost my son"
                        lion "Not to long ago, he disappeared into the cave, not far from here."
                        lion "There has never been a soul to return from this cave."
                        lion "He told me he would be back in two minutes."
                        narrator "Oh no! You will be blind at this point!"
                        lion "I would give anything, even this key, to anyone who would find my son."
                        python:
                            spoken_to_lion = True
                        menu:
                            "I will help you find your son.":
                                lion "You have no idea how much that means to me!"
                                lion "From here, to get to the cave, you must go forward once and twice right in either order."
                                lion "I beg of you to please make sure he doesn't run away, he must come back here."
                                lion "Best of luck!"

                            "I hope you find him":
                                lion "*sobs*"
                        hide lion
                        if not blind:

                            menu:

                                narrator "Where will you go?"

                                "forward":
                                    narrator "You move forward. 10 seconds pass."
                                    jump four_one

                                "right":
                                    narrator "You move rightward. 10 seconds pass."
                                    jump three_two

                                "downward":
                                    narrator "You move downward. 10 seconds pass."
                                    jump two_one
                        else:
                            menu:

                                narrator "Where will you go?"

                                "forward":
                                    narrator "You move forward. 10 seconds pass."
                                    jump four_one

                                "right":
                                    narrator "You move rightward. 10 seconds pass."
                                    jump three_two

                                "left":
                                    narrator "You move leftward."
                                    witch "Ha ha! You're leaving the forest!"
                                    witch "can't let that happen!"
                                    narrator "You were teleported back to the forest."
                                    jump three_one

                                "downward":
                                    narrator "You move downward. 10 seconds pass."
                                    jump two_one

                    "Nevermind":
                        narrator "You run away safely."
                        hide lion
                        if lion_direction == 0:
                            jump two_one
                        elif lion_direction == 1:
                            jump four_one
                        elif lion_direction == 2:
                            jump three_two
                        else:
                            narrator "uhhh you go down"
                            jump two_one


            "Go back.":
                narrator "You run away safely."
                hide lion
                if lion_direction == 0:
                    jump two_one
                elif lion_direction == 1:
                    jump four_one
                elif lion_direction == 2:
                    jump three_two
                else:
                    narrator "uhhh you go down"
                    jump two_one
    elif cub_found and not cub_returned:
        cub "Daddy!!!"
        lion "Junior!!!"
        lion "Don't ever leave your father again! What would your mother say?"
        cub "I'm sorry."
        if not blind:
            show lion at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
        lion "Thank you for finding my son. Here is the key to the treasure."
        narrator "You have obtained the key to the treasure!"

        python:
            treasure_key_obtained = True
            cub_returned = True

        lion "Best of luck!"
        if not blind:

            menu:

                narrator "Where will you go?"

                "forward":
                    narrator "You move forward. 10 seconds pass."
                    jump four_one

                "right":
                    narrator "You move rightward. 10 seconds pass."
                    jump three_two

                "downward":
                    narrator "You move downward. 10 seconds pass."
                    jump two_one
        else:
            menu:

                narrator "Where will you go?"

                "forward":
                    narrator "You move forward. 10 seconds pass."
                    jump four_one

                "right":
                    narrator "You move rightward. 10 seconds pass."
                    jump three_two

                "left":
                    narrator "You start moving leftward."
                    lion "Hey! You're going the wrong way!"
                    narrator "You stop moving."
                    lion "that way leads outside the forest!"
                    jump three_one

                "downward":
                    narrator "You move downward. 10 seconds pass."
                    jump two_one
    else:
        if not cub_returned:
            lion "*sobs*"
        else:
            lion "I gave you the key! Go find that treasure! It is yours!"

        if not blind:
            show lion at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)
            if treasure_key_obtained:
                show cub behind lion

            menu:

                narrator "Where will you go?"

                "forward":
                    narrator "You move forward. 10 seconds pass."
                    jump four_one

                "right":
                    narrator "You move rightward. 10 seconds pass."
                    jump three_two

                "downward":
                    narrator "You move downward. 10 seconds pass."
                    jump two_one
        else:
            menu:

                narrator "Where will you go?"

                "forward":
                    narrator "You move forward."
                    jump four_one

                "right":
                    narrator "You move rightward."
                    jump three_two

                "left":
                    if cub_returned:
                        narrator "You start moving leftward."
                        lion "Hey! You're going the wrong way!"
                        narrator "You stop moving."
                        lion "that way leads outside the forest!"
                    else:
                        narrator "You move leftward."
                        witch "Ha ha! You're leaving the forest!"
                        witch "can't let that happen!"
                        narrator "You were teleported back to the forest."
                    jump three_one

                "downward":
                    narrator "You move downward."
                    jump two_one

label three_two:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump four_two

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump three_three

            "left":
                python:
                    lion_direction = 2

                narrator "You move leftward. 10 seconds pass."
                jump three_one

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump two_two
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump four_two

            "right":
                narrator "You move rightward."
                jump three_three

            "left":
                python:
                    lion_direction = 2

                narrator "You move leftward."
                jump three_one

            "downward":
                narrator "You move downward."
                jump two_two

label three_three:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump four_three

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump three_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump three_two

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump two_three
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump four_three

            "right":
                narrator "You move rightward."
                jump three_four

            "left":
                narrator "You move leftward."
                jump three_two

            "downward":
                narrator "You move downward."
                jump two_three

label three_four:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward. 10 seconds pass."
                jump four_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump three_three

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump two_four
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                jump four_four

            "right":
                narrator "You move rightward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump three_four

            "left":
                narrator "You move leftward."
                jump three_three

            "downward":
                narrator "You move downward."
                jump two_four

label four_one:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump four_two

            "downward":
                python:
                    lion_direction = 1
                narrator "You move downward. 10 seconds pass."
                jump three_one
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_one

            "right":
                narrator "You move rightward."
                jump four_two

            "left":
                narrator "You move leftward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_one

            "downward":
                narrator "You move downward."
                jump three_one


label four_two:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump four_three

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump four_one

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump three_two
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_two

            "right":
                narrator "You move rightward."
                jump four_three

            "left":
                narrator "You move leftward."
                jump four_one

            "downward":
                narrator "You move downward."
                jump three_two

label four_three:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not cub_found and not blind:
        narrator "You see a cave in the distance."

    if has_become_blind and not cub_found:
        cub_voice "Hello? Can you help me find my dad?"
        if not blind:
            show cub at Position(xpos = 0.5, xanchor=0.5, ypos=0.5, yanchor=0.5)

        cub_voice "He's a big lion. I left him to go find my roar."
        cub_voice "but I was too scared to go into the cave, so I hid behind the rocks."
        if spoken_to_lion:
            narrator "Yup, this is the lion's son"
        jump cub_convo

    if not blind:

        menu:

            narrator "Where will you go?"

            "right":
                narrator "You move rightward. 10 seconds pass."
                jump four_four

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump four_two

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump three_three
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward"
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_three

            "right":
                narrator "You move rightward."
                jump four_four

            "left":
                narrator "You move leftward."
                jump four_two

            "downward":
                narrator "You move downward."
                jump three_three

label four_four:
    python:
        blindness_time -= sub_time

    if time_is_up(blindness_time):
        narrator "Time is up! You can no longer see!"
        $ blind = True
        $ has_become_blind = True

    if not blind:

        menu:

            narrator "Where will you go?"

            "left":
                narrator "You move leftward. 10 seconds pass."
                jump four_three

            "downward":
                narrator "You move downward. 10 seconds pass."
                jump three_four
    else:
        menu:

            narrator "Where will you go?"

            "forward":
                narrator "You move forward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_four

            "right":
                narrator "You move rightward."
                witch "Ha ha! You're leaving the forest!"
                witch "can't let that happen!"
                narrator "You were teleported back to the forest."
                jump four_four

            "left":
                narrator "You move leftward."
                jump four_three

            "downward":
                narrator "You move downward."
                jump three_four

label cub_convo:
    if said_no_to_cub:
        cub "Please?"
    else:
        cub "Will you please help me find my dad?"

    menu:
        cub "Will you please help me find my dad?"

        "Yes":
            cub "Thank you Thank you Thank you!"
            narrator "The cub has joined you on your adventure."
            $ cub_found = True
            jump four_three

        "No":
            $ said_no_to_cub = True
            jump cub_convo
