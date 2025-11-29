init:
    # Time between recieved messages (don't set it to 0, it will break)
    default auto_speak_timer = 2

    # True will mean all messages will be sent with the above timer
    # False will vary the delay based on the message length (better imo)
    # Raising or lowering the auto_speak_timer will still effect the time between messages even if this is set to False 
    # For anyone interested the math is message_timer_delay = max(min_speak_timer, min(len(list(character_info['current_dialogue'][true_current_index + 1].values())[0]) * (auto_speak_timer*0.025), max_speak_timer))
    default static_speak_timer = False

    # REMEMBER THESE CAN BE SET MID CONVERSATION USING {'code':'auto_speak_timer = 999'} IF YOU WANT TO SLOW DOWN/SPEED UP AT CERTAIN POINTS.

    # Minimum amount of time between messages, or short ones send REAL fast
    default min_speak_timer = 1

    # min_speak_timer gets set to 0 when skipping so we need a way to store what it started as, dont touch :)
    default original_min_speak_timer = min_speak_timer

    # Max speak timer between messages, to stop long ones... yk... taking too long
    default max_speak_timer = 5

    # Just adds or removes the skip button entirely
    default show_skip_button = True

    # How fast the messages send when the skip messages button is pressed (again, dont set to 0)
    default skip_speed_timer = 0.1

    # This is how many columns there are for your images in the gallery. Rows is done automatically
    default image_columns = 2

    # Shows the typing indicator so you can see if the person is sending a message. 
    default is_typing_indicator = True

    # The message that shows on the typing indicator before the '...'
    default is_typing_message = "User is typing"

    # If set to true gallery unlocks will be persistant accross saves
    default persistent_gallery = False

    # You CAN set the image size with every image you send, but if they are all the same size.. thats a pain
    # So set this and you can just pass images in as {"image":"imagepath.png"}
    # This is just for the image preview sizes as they are seen inside the chat 
    default chat_image_size = [216, 384]
    
    # The message that replaces a deleted message
    default deleted_message_replacement = "This message was deleted"
 
    # Enable or disable the settings scree
    default settings_screen_shown = True

    # Enable or disable allowing message speed adjust
    default allow_speed_adjust = True

    # Enable or disable message animations
    default message_animations = True
    
init python:
    # UI CUSTOMISATION?! WOW I OUTDID MYSELF! (Did I mention I suck at UI?)
    speaker_colors = {
        # Define non standard text colours for text messages per character so {"me":colourhere}, {"sarah":othercolour}
    }

    




########### DONT CHANGE ANYTHING PAST THIS LINE ###########

default is_typing = False
default persistent.persistent_gallery = []
default phone_data = {}
default persistent.seen_message_threads = {}
default current_contact = None
default click_to_send = True