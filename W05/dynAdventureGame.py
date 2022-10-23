"""
    filname:  dynAdventureGame.py
        Requirements:
            1)  You need to have at least three levels of scenarios with possible choices.
            2)  At least one of your scenarios must have more than two possible choices.
            3)  In each prompt, write the choices in ALL CAPS, so that the user knows which words are possible responses to choose.
            4)  When checking the users responses, you should match on the keyword, regardless of the uppercase/lowercase used in
                the response (e.g., "match", "MATCH", "Match" should all work).
            5)  Making different choices should take you to different scenarios. (You shouldn't have the same result for different
                choices.)
            6)  Choices should only work for the correct question.
                In other words, if one scenario resulted in choices of Run/Hide, but another resulted in choices Follow/Look, you
                should not be able to respond with "Follow" to the question that asked for Run/Hide.
                A good way to accomplish this is to have a series of nested if statements. (That is, the print and then the next
                if statement will be within the body/block of the first if statement.)
            9)  For each question, you should provide an "else" clause to handle the case that the user tries to type something
                other than the possible choices. It is up to you how to handle this case.
        Showing Creativity and Exceeding Requirements
            1)  Obviously, you'll show creativity by customizing the prompts and choices. To achieve the grade category of "Shows
                creativity and exceeds requirements" for this one, you need to add something additional to the framework of the
                game. For example, you might add even more levels or you might have more choices at each level. You might add hidden
                choices or trick questions. Have fun with this and see what you can do!
            2)  If you've already learned other programming concepts (for example, loops, lists, etc.) you are welcome to use those
                concepts here as a way to make show creativity and exceed requirements.
        Extra credit
            1)  For this assignment, you can earn +5 extra credit points by showing your program to at least two other people to
                have them play it. After they play it, briefly show them your code and explain how it works.
            *** Presented and explained to my co-workers Mark Brewer and CLint Lambert.
                    Mark Brewer commented that he liked the input validation and handling.
                    Clint Lambert commented that he liked the modulus used in the bad response exit check
        Milestone Requirements
            At the end of Lesson 05, to help make sure you are on track to finish the assignment, you need to complete the following:
            1)  The program is working for the first question and possible choices, and displays a follow-up response to each
                choice (including an else condition).
                For the milestone, you do not need to implement any additional scenarios/questions, you only need the first one.
            2)  Create a design for your complete game.
                Prepare for the rest of your game by deciding on all the possible prompts, choices, and responses that the user
                might see. You should design the complete game, including else conditions. Then, to finish up the assignment for
                the next lesson, you'll just need to code up all of these options.
    author:  Tracy Mann
    version:  1.0
    date:  10/8/2022
    class:  CSE110
    teacher:  Brother Wilson
    section:  27
        inputs:  a string to represent the response to the current senarios question as retrieved from the display_key element
        process:  validate without case sensativity the response is a valid response as in the list of keys in the response_key element.
            in the event that the response is invalid, increment the invalid response counter and re-present the same senario question to be answered,
            unless the invalid response is a multiple of 3.  For the case of mulitples of 3 invalid responses in a row, offer the option to exit the game.
            exit if accepted.  in the event that the response for current senario question is valid, then retrieve the name of the next senerio
            by using the response as a key in the response_key element.  if the next senario is has a response_key of exit_result then do not input a
            new answer, only print the display_key result and exit the loop.  any valid resonse will reset the invalid response counter to 0.  the senarios
            will be stored in and retrieved from a dictionary variable that is setup prior to starting the exceution loop to initiate using the init_senario.

    submission comment:  I believe this submission has earned a Made it my own.  I have met every requirement in the ruberic.  I have also incorporated the use of a dictionary list to hold senarios and a while loop to traverse the data in the dictionary.  I have ensured for the ruberic that the data points do not allow the same responses in any other senario and all senario paths are distict and do not cross or go backward.  due to this being a loop, i have also added an option to breaking out of the game after reaching any multiple of 3 invalid responses.

"""
import os

init_senario = "init"
senario = init_senario
display_key = "display"
results_key = "results"
exit_result = "exit"
exit = False
senarios = {
    init_senario : {
        display_key : "You are walking in a field.\
  To the (N)ORTH is a road,\
 to the (S)OUTH is the shore,\
 and to the (W)EST is a river.\n\
Which direction do you want to go? ",
        results_key : {
            "NORTH" : "road",
            "SOUTH" : "shore",
            "WEST" : "river",
            "N" : "road",
            "S" : "shore",
            "W" : "river"
        }
    },
    "road" : {
        display_key : "You reach the road.\
  If you continue (F)ORWARD you will cross the road to another field,\
 if you turn (L)EFT you will reach a bridge,\
 and if you turn (R)IGHT the road continues to some mountains.\n\
Which direction do you want to go? ",
        results_key : {
            "FORWARD" : "field",
            "LEFT" : "bridge",
            "RIGHT" : "mountains",
            "F" : "field",
            "L" : "bridge",
            "R" : "mountains"
        }
    },
    "field" : {
        display_key : "You reach another field.\
  It is bordered on the left by a (H)EDGE,\
 on the right by a (C)LIFF,\
 and a (F)OREST on the remaining side.\n\
Which do you walk to? ",
        results_key : {
            "HEDGE" : "hedge",
            "CLIFF" : "cliff",
            "FOREST" : "forest",
            "H" : "hedge",
            "C" : "cliff",
            "F" : "forest"
        }
    },
    "hedge" : {
        display_key : "You discover the river on the other side of the hedge and can go no further!\n",
        results_key : exit_result
    },
    "cliff" : {
        display_key : "The cliff is impassable and you can go no further!\n",
        results_key : exit_result
    },
    "forest" : {
        display_key : "The forest is to thick to pass through and you can go no further!\n",
        results_key : exit_result
    },
    "bridge" : {
        display_key : "You reach the bridge.\
  If you cross the bridge you can enter a familiar looking (H)OUSE,\
 if you go to the shore of the river you could get into a (B)OAT,\
 or you could stand on the B(R)IDGE to look down the river.\n\
Which do you wish to go to? ",
        results_key : {
            "HOUSE" : "house",
            "BOAT" : "boat",
            "BRIDGE" : "bridge_view",
            "H" : "house",
            "B" : "boat",
            "R" : "bridge_view"
        }
    },
    "house" : {
        display_key : "You have done it, you have arrived at Home!\n",
        results_key : exit_result
    },
    "boat" : {
        display_key : "The boat has a huge hole in it and you can go no further!\n",
        results_key : exit_result
    },
    "bridge_view" : {
        display_key : "The river flows from the thick forest, under the bridge and into the sea.  This is such a beautiful view you can go no further!\n",
        results_key : exit_result
    },
    "mountains" : {
        display_key : "You reach the mountains.\
  The road continues (T)HROUGH the mountain in a tunnel,\
 there is also a path that winds (U)P the side of the mountain,\
 and there is a mine opening visible that goes (D)OWN into the mountain.\n\
Which direction do you want to go? ",
        results_key : {
            "THROUGH" : "tunnel",
            "UP" : "mountain_side",
            "DOWN" : "mine",
            "T" : "tunnel",
            "U" : "mountain_side",
            "D" : "mine"
        }
    },
    "tunnel" : {
        display_key : "That tunnel is not lit, it is too dark and you can go no further!\n",
        results_key : exit_result
    },
    "mountain_side" : {
        display_key : "That path is too steep, you are not able to climb it so you can go no further!\n",
        results_key : exit_result
    },
    "mine" : {
        display_key : "That mine is not stable, it will fall in so you can go no further!\n",
        results_key : exit_result
    },
    "shore" : {
        display_key : "You reached the shore.\
  There is a (B)EACH, a (C)OVE and a B(R)EAKWATER.\n\
Where do you go?  ",
        results_key : {
            "BEACH" : "beach",
            "COVE" : "cove",
            "BREAKWATER" : "breakwater",
            "B" : "beach",
            "C" : "cove",
            "R" : "breakwater"
        }
    },
    "beach" : {
        display_key : "You reach the beach.\
  There is a sea ahead you could (S)WIM in,\
 a towel that you could (L)AY out on,\
 and a sand castle you could (P)LAY with.\n\
What do you do? ",
        results_key : {
            "SWIM" : "sea",
            "LAY" : "towel",
            "PLAY" : "sand_castle",
            "S" : "sea",
            "L" : "towel",
            "P" : "sand_castle"
        }
    },
    "sea" : {
        display_key : "You swim for hours, exiting the water you are exhausted and you can go no further!\n",
        results_key : exit_result
    },
    "towel" : {
        display_key : "You lay out and get a very nice tan, but you go no further!\n",
        results_key : exit_result
    },
    "sand_castle" : {
        display_key : "You play for hours and enjoy the sand castle and go no further!\n",
        results_key : exit_result
    },
    "cove" : {
        display_key : "You reach the Cove.\
  You may go (F)ISHING,\
 (W)ADE in the water,\
 or (S)KIP rocks across the cove.\
What do you do? ",
        results_key : {
            "FISHING" : "fishing",
            "WADE" : "wade",
            "SKIP" : "skip_rocks",
            "F" : "cove_fishing",
            "W" : "wade",
            "S" : "skip_rocks"
        }
    },
    "fishing" : {
        display_key : "You fish for hours and catch nothing but bait fish and now you can go no further!\n",
        results_key : exit_result
    },
    "wade" : {
        display_key : "You start to wade into the water, find it is too cold and now you can go no further!\n",
        results_key : exit_result
    },
    "skip_rocks" : {
        display_key : "Tou skip rocks out across the cove for the rest of the night, and can go no further!\n",
        results_key : exit_result
    },
    "breakwater" : {
        display_key : "You reach the Breakwater.\
  You may go (C)LIMB the breakwater,\
 (P)ICK flowers,\
 or (D)IG into the breakwater.\
What do you do? ",
        results_key : {
            "CLIMB" : "climb",
            "PICK" : "pick",
            "DIG" : "dig",
            "C" : "climb",
            "P" : "pick",
            "D" : "dig"
        }
    },
    "climb" : {
        display_key : "You climb the breakwater and walk the coast all night, and can go no further!\n",
        results_key : exit_result
    },
    "pick" : {
        display_key : "You send the rest of the day picking flowers, and can go no further!\n",
        results_key : exit_result
    },
    "dig" : {
        display_key : "You decide digging into the breakwater is not a good idea, so you can go no further!\n",
        results_key : exit_result
    },
    "river" : {
        display_key : "You reached the river.\
  You may walk up to the (F)ORD,\
 stay on the (B)ANK,\
 or go over to the F(E)RRY.\
What do you do? ",
        results_key : {
            "FORD" : "ford",
            "BANK" : "bank",
            "FERRY" : "ferry",
            "F" : "ford",
            "B" : "bank",
            "E" : "ferry"
        }
    },
    "ford" : {
        display_key : "You reached the ford.\
  You may (C)ROSS the ford,\
 (L)OOK into the water,\
 or (G)RAB some of the crayfish that are pooling in front of you.\
What do you do? ",
        results_key : {
            "CROSS" : "cross",
            "LOOK" : "look",
            "GRAB" : "grab",
            "C" : "cross",
            "L" : "look",
            "G" : "grab"
        }
    },
    "cross" : {
        display_key : "As you begin to cross the ford, you find the water is too fast.  You are stuck and can go no further!\n",
        results_key : exit_result
    },
    "look" : {
        display_key : "As you look ino the water you get lost in your thoughts and find it is too late in the day to go any further!\n",
        results_key : exit_result
    },
    "grab" : {
        display_key : "You grab a handful of crayfish and they pinch your hand making you drop them all.  As you wonder about what happened you can go no further!\n",
        results_key : exit_result
    },
    "bank" : {
        display_key : "You reached the bank.\
  You may (M)AKE some mud pies,\
 (C)OLLECT some pretty stones and shells,\
 or (S)EARCH for burried treasure.\
What do you do? ",
        results_key : {
            "MAKE" : "make",
            "COLLECT" : "collect",
            "SEARCH" : "search",
            "M" : "make",
            "C" : "collect",
            "S" : "search"
        }
    },
    "make" : {
        display_key : "You spend the day making mud pies, having a lot of un, but you can go no further!\n",
        results_key : exit_result
    },
    "collect" : {
        display_key : "You collect many stones and shells to remind you of your trip, but you can go no further!\n",
        results_key : exit_result
    },
    "search" : {
        display_key : "You search all afternoon for buried treasure, finding nothing, and you can go no further!\n",
        results_key : exit_result
    },
    "ferry" : {
        display_key : "You reached the ferry.\
  You may (R)IDE the ferry across,\
 (W)ATCH the ferryman cross the deep water,\
 or (T)ALK to the ferryman about the weather.\
What do you do? ",
        results_key : {
            "RIDE" : "ride",
            "WATCH" : "watch",
            "TALK" : "talk",
            "R" : "ride",
            "W" : "watch",
            "T" : "talk"
        }
    },
    "ride" : {
        display_key : "As you go to ride the ferry, you find you do not have enough to pay the toll, so you can go no further!\n",
        results_key : exit_result
    },
    "watch" : {
        display_key : "You spend the afternoon watching the ferryman take teh ferry back and forth, then you find it is too late and can go no further!\n",
        results_key : exit_result
    },
    "talk" : {
        display_key : "You call out to talk with the ferryman, but he does not hear you and goes across the river.  You find yourself alone and can go no further!\n",
        results_key : exit_result
    }
}

# ref https://www.geeksforgeeks.org/clear-screen-python/ for clear screen
os.system('cls')
print()
# ref https://www.w3schools.com/python/python_while_loops.asp for while loop
bad_count = 0
while not exit:
    if senarios[senario][results_key] == exit_result:
        print(senarios[senario][display_key])
        exit = True
    else:
        responce = input(senarios[senario][display_key])
        if responce.upper() in senarios[senario][results_key].keys():
            senario = senarios[senario][results_key][responce.upper()]
            bad_count = 0
        else:
            bad_count = bad_count + 1
            if (bad_count > 1) and ((bad_count % 3) == 0) :
                responce = input("You have had "+str(bad_count)+ " invalid responces, do you wish to quit((Y)ES/(N)O)? ")
                if responce.upper() in ["Y", "YES"]:
                    print("Quitting!")
                    exit = True
            if not exit:
                print("Invalid responce, please try again...\n")
