#---- HELLO, AND WELCOME TO MY FIRST EVER RENPY PROJECT. ----#

###########################################################
## THIS DEMO COMES AS A PLAYABLE VERSION, NOT JUST CODE. ## 
##    YOU CAN CLICK PLAY AND SEE EVERYTING WORKING       ##
###########################################################

# This a completely dynamic phone system allowing for as many phones as you want, conversation mirroring when opening other phones, gallery with autounlocking images
# text messages (obviously), sending images and videos, messages deleting (mid conversation or out of it), code execution mid text conversation, dynamically loading in new 
# messages or full conversations with the phone open or closed. Persistant chat history. Changable backgrounds.... Ummmmm.... I mean it works just like a real phone I guess?
# You can close a conversation at any time, even when you're at a choice and continue with the game, open the phone again and just keep talking
# You CAN pause the game until a conversation is finished but you dont NEED to, nothing in this entire phone system ever touches a jump label
# and it all works off a single Call until the phone is closed, so it will never break game flow. You can let players open and close the phone whenever they want
# even have conversations with branching dialouge, gallery unlocks and code ececution and it doesn't touch the game flow. Ever. 



# The money thing is just to show the mid conversation code execution

default money = 0

# Set the phones background

default phone_background = "gui/phone_backgrounds/2.png"

# All available backgrounds in background selection. These dont auto scale to the phone so.... I just threw an image into paint.net, threw the phone outline over the top and 
# deleted everything outside, guarantees correct size!! (Have I mentioned I suck at UI yet?)

default phone_backgrounds = ["gui/phone_backgrounds/1.png", "gui/phone_backgrounds/2.png", "gui/phone_backgrounds/3.png"]

# Each phone has its own gallery, only the mc_phone autoloads the gallery info, other peoples need to be set manually.

default sarah_gallery_data = {}

default iris_gallery_data = {}

# Just hides the two other phones at the start of the game, variable used in my_gui.rpy

default sarah_phone_show = False

default iris_phone_show = False

define kesash = Character("Kesash", color="#ff0000")

label start:
    ### DO ALLL YOUR PHONE DEFINITIONS HERE ####

    # When opening the phone it takes a map like below, opening it using the GUI loads in mc_phone automatically
    # It doesnt HAVE to be done in the start label specifically, just make sure its done before they have access to the phones

    $ mc_phone = {
        # These are just the contacts that are defined in test_char.rpy and iris_dialogue.rpy 
        "contacts":[mc_test_full_info, mc_iris_full_info],
        # This is the gallery that is auto created in gallery_system.rpy, this isnt used YET
        # all phones share a background. Working on it.
        "gallery": gallery_data,
        "name": "mc",
        "background": ["gui/phone_backgrounds/2.png"]
        }

    # You can create multiple phones :D

    $ iris_phone = {
        "contacts":[iris_sarah_full_info, iris_mc_full_info],
        "gallery": iris_gallery_data,
        "name": "iris",
        "background": ["gui/phone_backgrounds/2.png"]
        }

    $ sarah_phone = {
        "contacts":[sarah_iris_full_info, test_mc_full_info],
        "gallery": sarah_gallery_data,
        "name": "sarah",
        "background": ["gui/phone_backgrounds/2.png"] 
        }

    kesash "Hey, and welcome to my phone system demo"

    kesash "It's just here to show off some of the things it can do"

    kesash "You can open and close any conversation or even the whole phone whenever you want, nothing will break"

    kesash "If something DOES break please let me know. Leave a comment or message me on discord at Kesa_"

    kesash "If you play through the whole thing youll even see multiple phones being used at once with mirrored conversations"

    kesash "Sarah is the one who gives you the whole walkthough, Iris is just there as a way to show two galleries 2 contacts etc"

    kesash "And give Sarah somone to message when you get your hands on her phone :)"

    jump start_1

label start_1:
    call show_all_gui from _call_show_all_gui  

    
    "These messages will loop"
    "Just to show you"
    "That no matter where you open the phone"
    "And no matter what you do in it"
    "They will always continue where they left off!"

    # after_choices_list is the final conversation in the initial messages. This causes the game to loop until its finished.
    # You can easily check if any conversation is finished with 'if len(convo_list) > convo_list_index'
    if len(after_choices_list) > after_choices_list_index:
        jump start_1
    else:
        jump start_2

label start_2:

    show bg walking_1 with fade

    "Going for a walk now"

    show bg walking_2 with fade

    "and after this text box Sarah will message again"

    jump start_3

label start_3:

    # This adds a message sent to MC by sarah with the phone still closed, once open it will be there
    $ mc_test_full_info['all_dialogue'].extend([{"sarah":"I'm BACK!"}])
    # This loads a new conversation into the phone, ready to start once that contact is opened
    $ mc_test_full_info['current_dialogue'] = sarah_final_convo
    # MAKE SURE TO SET THE INDEX. STRING OF THE VARIABLE NAME.
    $ mc_test_full_info['current_index'] = "sarah_final_convo_index"

    "feel free to keep walking and swapping labels though, ive done this just to show that you dont need to set a conversation and have it used in the same label"

    "the phone system exists completely outside the RenPy jump label system. They dont interact at all, unless you make them."

    jump start_4


label start_4:
    show bg walking_1 with fade

    pause

    jump start_5

label start_5:
    show bg walking_2 with fade

    pause

    jump start_4


# THAT IS EVERYTHING NEEDED IN THE ACTAUL SCRIPT FOR THIS ENTIRE DEMO. EVERYTHING ELSE IS JUST DEFINING
# THE CONVERSATION LISTS AND CONTACT DICTS. DONE IN OTHER FILES.

###############################
######## MORE EXAMPLES ########
###############################


label examples:

    # loading a new conversation into the phone at any point is easy. as long as its defined
    # just assign the conversation to the values in the full info map! 
    # So, there is an example covo created in iris_dialogue 
    # to load it into the phone just do 

    $ mc_iris_full_info['current_dialogue'] = iris_chat_example
    $ mc_iris_full_info['current_index'] = "iris_chat_example_index"

    # Make sure you pass in current dialogue AND the matching current index
    # And I know it seems REALLY WEIRD but pass in a string containing the variable name to the index value

    # IF a partner phone exists then make sure to use the function to update both phones and keep them in sync
    # You can use this even if no partner phone exists if you find it easier, it will still work
    # (by partner phone i mean iris's phone exists in this demo, updating using this will update the mc contact on her phone too)

    $ update_current_convo('mc_iris_full_info', {'current_dialogue': iris_chat_example, 'current_index': 'iris_chat_example_index'})

    # You can even just make them send a message with the phone still closed
    # Just extend the full conversation with a message dict

    $ mc_iris_full_info['all_dialogue'].extend([{"iris":"This message has now been sent"}])

    # That message will now be in the chat log when you open the phone. Already sent :)

    # This is actaully really useful for preloading a message in if youre replying
    # So the message list you define would start with the mc reply, and the message they are replying to would be pre loaded in like above

    # Now lets clear the conversation stack! This wont delete the history, it will just remove any 'waiting' conversations that havent happened yet

    $ mc_iris_full_info['current_dialogue'] = []
    $ mc_iris_full_info['current_index'] = "iris_reusable_index"

    # This is why we create a reusable index , because it MUST BE A STRING that is the name of a variable
    # You cant just set it to 9999999, it WILL break
    # I know... I know... stupid.....
    # Make sure to update the partner phone too if it exists, you can use the function to do this too ^

    # If, for some reason, you want to clear the message history, you can
    # Make sure to update partner phone too if it exists, no function for this currently...

    $ mc_iris_full_info['all_dialogue'].clear()
    $ mc_iris_total_index = 0

    # Want to lock them so they dissapear off the contact list

    $ mc_iris_full_info['unlocked'] = False 

    # DONE!

    # And the same in reverse, want to unlock a locked character so they show up?

    $ iris_full_info['unlocked'] = True

    # EASY

    pass






            