# Theres 1 note in this one, its near the bottom

default iris_list_dialogue = [
    {"mc":"Hey just got my new phone"},
    {"iris":"Wow, convenient"},
    {"mc":"What do you mean?"},
    {"iris":"I mean its a convenient way to exaplin the short message history when starting the game...."},
    {"mc":"Shhhhhhhh"},
    {"mc":"Youre only here to show multiple characters chatting in the phone you know"},
    {"iris":"Wow, rude much"}
]

default iris_chat_1 = [
    {"mc":"Send a picture :)"},
    {"iris":"Finee"},
    {"image":"iris/iris_image_1.png"}
]

default iris_chat_1_index = 0

default iris_chat_example = [
    {"iris":"Used for the example, explained in script"}
]

default iris_chat_example_index = 0

default iris_total_index = 0

default iris_reusable_index = 0

default iris_max_index = 999999999

default mc_iris_full_info = {
    "owner":"mc",
    "unlocked":True,
    "name":"Iris",
    "profile":"iris/iris_profile.png",
    "current_index":"iris_chat_1_index",
    "all_dialogue":iris_list_dialogue,
    "current_dialogue":iris_chat_1,
    "scroll_to_bottom": False
    }

default iris_mc_full_info = {
    "owner":"iris",
    "unlocked":True,
    "name":"MC",
    "profile":"mc/mc_profile.png",
    "current_index":"iris_max_index",
    "all_dialogue":iris_list_dialogue,
    "current_dialogue":iris_list_dialogue,
    "scroll_to_bottom": False
    }

default sarah_iris_list_dialogue_1 = [
    {"sarah":"Just waiting for the new player to come"},
    {"iris":"New player"},
    {"sarah":"Yeaaa so we need a chat to show off some stuff"},
    {"sarah":"Like if they open your phone or my phone they see it in reverse"},
    {"iris":"Ohhh yea thats pretty cool"},
    {"sarah":"It's a pain to set up though"},
    {"iris":"It isnt THAT hard right??"},
    {"sarah":"Okay no its not THAT hard but you need to make sure names are all correct"},
    {"sarah":"And you added both people to the other persons phone dict"},
    {"sarah":"And.... oh... wait... thats it?"},
    {"iris":"I said it wasnt that hard"},
    {"iris":"Wait... what happens if they closed the phone they are looking at now"},
    {"iris":"Like mid convo, and opened the other one??"},
    {"sarah":"Then the convo would carry on from the other persons perspective"},
    {"iris":"Thats... kinda cool"},
    {"sarah":"AND if they opened your phone the messages are click to send for yours"},
    {"sarah":"but if they opened my phone the messages will all just... send"},
    {"sarah":"It's something you can just decide by phone on, or by contact"},
    {"sarah":"Or just turn on and off mid conversaton"},
    {"iris":"Shall we talk a little longer to let them test that"},
    {"sarah":"I mean im TRYING to but idk what to say"},
    {"iris":"You and me both....."},
    {"iris":"Does all of this still work mid label? Without breaking game flow?"},
    {"sarah":"CERTAINLY DOES!!"},
    {"sarah":"you can have the phone gui available at all times"},
    {"sarah":"it can always be opened and played with"},
    {"sarah":"It will never break game flow"},
    {"sarah":"Oh each phone has its own gallery too!!!"},
    {"iris":"Okay... thats cool...."},
    {"sarah":"But only the MC gallery auto loads when the game starts"},
    {"sarah":"For ours its all manual.... (currently)"},
    {"sarah":"NOW, lets jump to a new convo and stay in sync"},
    # Passing the new dict values into update_current_convo  will update the partner phone too, if named correctly so this will update
    # the convo on both sarah AND iris's phone
    {"code":"update_current_convo('sarah_iris_full_info', {'current_index':'sarah_iris_list_dialogue_2_index','current_dialogue':'sarah_iris_list_dialogue_2'})"}   
]

default sarah_iris_list_dialogue_1_index = 0

default sarah_iris_list_dialogue_2 = [
    {"iris":"So, were on a new convo"},
    {"sarah":"yep, new convo thread loaded in just now"},
    {"iris":"and its still syncing correctly for both phones?"},
    {"sarah":"I really hope so...."},
    {"iris":"Same, im really out of ideas of what to say now"},
    {"sarah":"yep, Just dragging it on to allow people to swap phones"},
    {"iris":"Think thats enough?"},
    {"sarah":"YEP! CYA IRIS!"},
    {"iris":"bye sarah!"},
    {"system":"-- user has gone offline --"}
]



default sarah_iris_list_dialogue_2_index = 0


default sarah_iris_list_dialogue = []


default sarah_iris_full_info = {
    "owner":"sarah",
    "unlocked":True,
    "name":"Iris",
    "profile":"iris/iris_profile.png",
    "current_index":"sarah_iris_list_dialogue_1_index",
    "all_dialogue":sarah_iris_list_dialogue,
    "current_dialogue":sarah_iris_list_dialogue_1,
    "scroll_to_bottom": False
}

default iris_sarah_full_info = {
    "owner":"iris",
    "unlocked":True,
    "name":"Sarah",
    "profile":"test/test_profile.png",
    "current_index":"sarah_iris_list_dialogue_1_index",
    "all_dialogue":sarah_iris_list_dialogue,
    "current_dialogue":sarah_iris_list_dialogue_1,
    "scroll_to_bottom": False
}






#label next_day_list:
#python:
#    import random
#    wins_in_a_row = 0
#    def morning_check():
#        if jade_result_pending:
#            jade_result_pending = False 
#            result = random.randint(0, 1)
#            if result:
#                wins_in_a_row += 1
#                profit = investment_amount + random.randint(50, 200)
#                money += profit
#                mc_peanut_full_info['all_dialogue'].append({"jade": "Good news! The investment paid off."})
#                mc_peanut_full_info['all_dialogue'].append({"jade": f"You earned {profit} coins total."})
#                mc_peanut_full_info['all_dialogue'].append({"jade": "Told you I had a lucky streak."})
#                if wins_in_a_row >= 1:
#                    mc_peanut_full_info['all_dialogue'].append({"jade": "Thats {wins_in_a_row} days in a row!"})
#
#            else:
#                wins_in_a_row = 0
#                loss = random.randint(50, investment_amount)
#                money += (investment_amount - loss)
#                mc_peanut_full_info['all_dialogue'].append({"jade": "Ugh... it didn't go so well."})
#                mc_peanut_full_info['all_dialogue'].append({"jade": f"You lost {loss} coins."})
#                mc_peanut_full_info['all_dialogue'].append({"jade": "Next time, I'll be more careful. Promise."})
#
#
#define morning_dialogue = [
#    {"code":"morning_check()"}
#]