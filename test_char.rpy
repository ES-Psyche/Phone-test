
# This is everything needed to create the entire conversaiton you have with Sarah. After the phone is defined (done at the bottom) it's littrally
# just a list containing dictionaries for each message. Every message has a 'key' that decides what it does. 

# 'image' - sends the image, use the full image path and extention
# 'system' - displays a system message
# 'delete' - searches for that exact string and replaces it with {'system':'this message was deleted'}, which will display that as a system message
# 'code' - will execute ANY code, even multi line code. Must be entered as a string. 

# To present a choice simply add a list instead of a dictonary. Each list in this list will be a choice. 
# [['hello','choice_1'],['goodbye','choice_2']] will present the player with 2 choices 'hello' and 'goodbye'. clicking hello
# will load in the conversation 'choice_1' and clicking goodbye will load in the conversation 'choice_2'

default test_dialogue_list = [
    {"sarah":"Youre here!"},
    {"sarah":"Click the little speech bubble at the bottom right to reply :)"},
    # Anything said by the owner of the phone is click to send, tolgglable
    {"mc":"this is a test"},
    # Use the character they are talking to's name for the dialogue they send, lowercase
    {"sarah":"yes it is"},
    {"sarah":"First, yes, the ui sucks, it looks ugly, its being worked on"},
    {"sarah":"Secondly if the messages are too fast or too slow"},
    {"sarah":"Just open config.rpy and change the timer"},
    {"mc":"Isn't that in the phone settings now?"},
    {"sarah":"WHAT?! WOW YOU'RE RIGHT!"},
    {"sarah":"Now, to the features!"},
    {"mc":"Okay!"},
    {"sarah":"There is a 'skip seen messages' button. Works cross save just like renpy skip"},
    {"sarah":"If this is your first time running this though it wont be there"},
    {"sarah":"Its togglable too, so you can skip then stop skipping at will"},
    {"sarah":"The speed of skip while clicked is also in the config.rpy"},
    {"mc":"Got it"},
    {"sarah":"now lets give you some money"},
    # You can use this to dynamically run any code you like, even multi line code if you want. 
    {"code":"money += 100"},
    {"sarah":"anything labeled code will run that code"},
    {"sarah":"The money should have just gone up!"},
    {"mc":"Yep, it did"},
    {"sarah":"System message now? Can be used for lots of things"},
    # Anything tagged system will show as a system message
    {"system":"you have been blocked"},
    {"system":"you have been unblocked"},
    {"system":"Friday"},
    {"system":"Three days later"},
    {"sarah":"You get the idea"},
    {"mc":"What else?"},
    # Emojis cos im old and they were cool at one point
    {"sarah":"Oh, these work too 😂🤣😃😘🥰🙄"},
    {"sarah":"I haven't tested EVERY emoji, so check before release"},
    {"mc":"😃"},
    {"sarah":"Now lets delete a message shall we?"},
    {"sarah":"This message will be deleted!"},
    {"sarah":"....."},
    # A delete tag will search for that message string and delete it. Dont try to delete a message if there is a 
    # duplicate that is exactly the same
    {"delete":"This message will be deleted!"},
    {"sarah":"poof, its gone!"},
    {"mc":"What next?!"},
    # The image tag will send that image in the chat. If its in the gallery it will auto unlock it. 
    {"image":"test/test_image.png"},
    {"mc":"That sent an image!"},
    {"sarah":"try clicking it!"},
    {"sarah":"and its now unlocked in the gallery!"},
    {"mc":"Clicking opens it full screen!"},
    {"sarah":"While theres a cofigurable default value for image sizes, you can pass in a custom one per image"},
    {"sarah":"So if you have a landscape photo"},
    # You can add a second key, value pair to an image to set its size in the chat. Key is 'scale'
    {"image":"testlandscape.png","scale":[384, 216]},
    {"sarah":"and it scales correctly!"},
    {"mc":"Okay"},
    {"sarah":"and you can delete images too"},
    {"image":"test/test_image_2.png"},
    {"delete":"test/test_image_2.png"},
    {"sarah":"works exactly the same way"},
    {"sarah":"Now time to make a choice!"},
    # A choice option is a list of lists, you can have as many choices as you want. The first item in each list is what the player sees
    # The second item in the list is where that choice jumps to. 
    [["choice_1","choice_1_list"],["choice_2","choice_2_list"],["choice_3","choice_3_list"]]
]

# any dialogue list you make MUST have and index assigned
# it MUST BE the same name with _index at the end
# the index directly after a choice should ALWAYS be 1. Otherwise, 0.
default test_dialogue_list_index = 0



# This is where picking option 1 will jump to
default choice_1_list = [
    {"sarah":"You picked option 1!"},
    {"sarah":"You're now on a separate conversation thread, it loaded into the phone the second you clicked"},
    {"sarah":"Now lets show off a little of that 'dynamic' feel!"},
    # This function updates the current conversation without needing a choice, and keeps the partner phone in sync too
    # the after choice update does the same thing if a partner phone exsits (it doesnt have to). So sarahs phone will always
    # be completely in sync with the MC phone
    {"code": "update_current_convo('mc_test_full_info', {'current_dialogue': after_choices_list, 'current_index': 'after_choices_list_index'})"}
]

# REMEMBER TO MAKE AN INDEX. THIS IS AFTER A CHOICE, SO SET IT TO 1!!!
default choice_1_list_index = 1

# This is where option 2 will take you to
default choice_2_list = [
    {"sarah":"You picked option 2!"},
    {"sarah":"Your'e now on a separate conversation thread, it loaded into the phone the second you clicked"},
    {"sarah":"Now lets show off a little of that 'dynamic' feel!"},
    # Same again here
    {"code": "update_current_convo('mc_test_full_info', {'current_dialogue': after_choices_list, 'current_index': 'after_choices_list_index'})"}
]

# REMEMBER TO MAKE AN INDEX
default choice_2_list_index = 1



# This is where option 3 will take you to
default choice_3_list = [
    {"sarah":"You picked option 3!"},
    {"sarah":"Your'e now on a separate conversation thread, it loaded into the phone the second you clicked"},
    {"sarah":"Now lets show off a little of that 'dynamic' feel!"},
    # and here, it just forced all three conversation paths back to the same one
    {"code": "update_current_convo('mc_test_full_info', {'current_dialogue': after_choices_list, 'current_index': 'after_choices_list_index'})"}
]

# REMEMBER TO MAKE AN INDEX
default choice_3_list_index = 1


# This is where the code above sends the conversation
default after_choices_list = [
    {"sarah":"No matter what choice you made I just forced all 3 conversations back onto the same path!!"},
    {"sarah":"Cool right?!"},
    {"mc":"Yea I guess"},
    {"sarah":"What next... How about we trigger a different character messaging you based on where we are in the conversation?"},
    # Here im adding a new message to the iris conversation list. You can use this same method to set the current 
    # conversation and current index too, so it will load in a new conversation
    {"code":"mc_iris_full_info['all_dialogue'].extend([{'iris':'Wow youre talking to that test girl alot arent you'}])"},
    {"sarah":"Iris just messaged you!"},
    {"sarah":"and not just single messages, entire message stacks can be loaded in using only the phone system, ready for you to go reply to"},
    {"sarah":"Although, it does get a little more complicated"},
    {"sarah":"You can also decide when a message is click to send"},
    {"mc":"What do you mean?"},
    {"code":"click_to_send = False"},
    # These messages are tagged as 'mc', the owner of the phone, so they will send from your pov, but wont be click to send
    {"mc":"You can just make me send messages without me clicking?"},
    {"mc":"Oh.... right"},
    {"code":"click_to_send = True"},
    {"sarah":"yep, and its as simple as assigning a variable"},
    # Im just running if True here, but its just to show how sending a message under conditions works within the same convo
    {"code": """
if True:
    test_mc_full_info['all_dialogue'].append({'sarah': "Did you know this message was sent under a conditional statement? That can be done too, check the code notes!"})
"""},
    # Exactly the same but if False, so it will never send
    {"code": """
if False:
    test_mc_full_info['all_dialogue'].append({'sarah': "And this message will never get shown :c"})
"""},
    {"sarah":"and not to brag...."},
    {"mc":"You're totally about to  brag"},
    {"sarah":"Maybe...."},
    {"sarah":"BUT. This ENTIRE system works without a single jump and 1 call"},
    {"sarah":"That means you can run it MID LABEL and it wont break anything!"},
    {"sarah":"Thats what the stupid repeating text is showing when the phone is closed...."},
    {"sarah":"Last few things"},
    {"mc":"Good cos this is getting long"},
    {"sarah":"You know the only reason you even HAVE replies is to pause the convo so you can read what im saying, so be nice!"},
    {"sarah":"So the menu is disabled while the phone is open, saving in here just..... ehhhh doesn't work well"},
    {"sarah":"But on the plus side, you can close and reopen a conversation at ANY TIME"},
    {"sarah":"Even when there is a choice available"},
    {"sarah":"Just reopen the phone and continue where you left off!"},
    {"mc":"Oh cool"},
    {"sarah":"Make sure to read the comments in gallery_system.rpy"},
    {"sarah":"It's an autofilling gallery sectioned by character"},
    {"sarah":"Like it littraly scans your game files for the images and creates galleries"},
    {"sarah":"And automates unlocking those images, like what happened when I sent two earlier"},
    {"mc":"Anything else?"},
    {"sarah":"So new features are coming, soon"},
    {"sarah":"Currently adding stat tracking and stuff"},
    {"sarah":"Oh and did you notice the little ! over the phone gui?"},
    {"sarah":"that shows automatically if there is an available conversation!"},
    {"sarah":"This system CAN handle multiple phones too"},
    {"sarah":"so if you wanted to say... pick someone elses phone up and have different convos?"},
    {"sarah":"You can!"},
    {"mc":"Thats pretty cool"},
    {"sarah":"Okay so now....."},
    {"sarah":"After i send my next message that repeating message wont repeat anymore"},
    {"sarah":"Go click past it and I'll show you a scene change with a new convo loaded in"}
]

default after_choices_list_index = 0

default sarah_final_convo =[
    {"mc":"Oh, you messaged when the phone was closed"},
    {"sarah":"Yep, thats how phones work"},
    {"sarah":"and if you had finished the convo with iris too that ! will have gone then reappeared when this convo became available"},
    {"mc":"Yep"},
    {"sarah":"almost done...."},
    {"sarah":"You can message me on discord with any questions"},
    {"sarah":"Username is kesa_"},
    {"sarah":"This system is free to use for any non profit games"},
    {"mc":"Okay :)"},
    {"sarah":"and just in case you didnt know-"},
    {"sarah":"You can scroll up to see previous messages ☝"},
    {"sarah":"Now lets add some more phones....."},
    {"code":"sarah_phone_show = True"},
    {"code":"iris_phone_show = True"},
    {"sarah":"When you close the phone now there will be THREE phones"},
    {"sarah":"Mine and Iris's have been added, you can open them and watch us talk"},
    {"sarah":"If you open this conversation on my phone I wont be able to reply... I mean you have my phone :c"},
    {"sarah":"I mean... obviously"},
    {"sarah":"You can change that though, if you want"},
    {"mc":"Got it"},
    {"sarah":"So this whole system works outside of normal game flow"},
    {"sarah":"You CAN pause the flow until a conversation is finished"},
    {"sarah":"Like i did with the loop at the start, didnt end till we spoke"},
    {"sarah":"But you dont HAVE to"},
    {"sarah":"You can just continue the game, messages waiting to be read and replied to"},
    {"sarah":"Well, think thats it. Enjoy!"},
    {"system":"--User has gone offline--"}
]

default sarah_final_convo_index = 0



########################################################################################

# Everything below here is needed as standard for any character the phone messages. 



# This is the list that tracks the complete conversation, you can preload messages in
default test_list_dialogue = [
    {"sarah":"Hello and welcome to my phone system demo!"}
]
# Just tracks how long the total conversation is, make sure to set it correctly if you preloaded messages
default test_total_index = 1
# If you want to disable messaging you can use this. Will exaplain how in another comment
default test_reusable_index = 999999999999

# You must create a profile for each character that the person using the phone is talking to. It must contain all these values.
# Think of this like a  contact on someones phone. Each one of these is 1 contact, you then add them to that persons
# contact list, on their phone dictionary (created in script.rpy)

# The naming convention is REALLY REALLY important here. It MUST start messagesfrom_messagesto_ after that it doesnt matter.
# So you could have mc_test_akhjsdbfalkswrnfawlrkn, thats fine too :D
# Why is it test? Cos her name was test when i first made this, then gave her a name later. CBA to change all the vars.

default mc_test_full_info = {
    # Just the name of the owner of the phone, same as when you defined the phone, its here bcause renpy does some REALLY
    # REALLY weird stuff with screens and it lets us filter out it loading in incorrect data
    "owner":"mc",
    #If set to False athe character will not show up in the contacts list. Use to add and remove them dynamically
    "unlocked":True,
    # The contacts name, pretty simple
    "name":"Sarah",
    # Profile picture for the contacts
    "profile":"test/test_profile.png",
    # This is the index of the chat that is initially loaded into the phone. If the game starts with no convo loaded set it to the reusable value
    # I KNOW WE ARE REFERENCING A VARIABLE HERE, BUT IT MUST BE A STRING OF THAT VARIABLE NAME. 
    "current_index":"test_dialogue_list_index",
    # This is the list that holds all dialogue, defined above. Just set it to that variable, it can be empty or start with chats in.
    "all_dialogue":test_list_dialogue,
    # This is the chat that's loded into the game when the game starts. If you want the game to start with no convo, make it an empty list.
    "current_dialogue":test_dialogue_list,
    # Set both these to false. They are used, altered and tracked automatically. 
    "scroll_to_bottom": False,
    "delay_next_message": False, 
    }

# Creating the exact same thing in reverse, so if you pick up their phone, the convo is there in reverse!
# THE NAME IS THE SAME WITH REVERSED ORDER FOR. A. REASON. NAMING CONVENTION IS SO SO SO SO IMPORTANT TO 
# USING THIS. LIKE REALLY REALLY IMPORTANT.
default test_mc_full_info = {
    "owner":"sarah",
    "unlocked":True,
    "name":"mc",
    "profile":"mc/mc_profile.png",
    "current_index":"test_dialogue_list_index",
    "all_dialogue":test_list_dialogue,
    "current_dialogue":test_dialogue_list,
    "scroll_to_bottom": False,
    "delay_next_message": False, 
    # Not REQUIRED but if you define as false will mean that while this phone is open on this conversation (so for this
    # You have sarahs phone and open convo with MC) messaging will be dissabled
    "enable_messaging": False
    }