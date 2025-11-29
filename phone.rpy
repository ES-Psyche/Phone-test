# ╔════════════════════════════════════════════════════════════════════╗
# ║                    © 2025 Kesash                                   ║
# ║             All Rights Reserved. Forever.                          ║
# ║                                                                    ║
# ║  This code is mine. You may not copy, modify, steal, borrow,       ║
# ║  whisper sweet nothings to, or upload it to a shady mod site.      ║
# ║                                                                    ║
# ║          There is NO license. There is NO permission.              ║
# ║      Not open source. Not closed source. It’s my source.           ║
# ║                                                                    ║
# ║     If you're reading this and you're not me, close the file,      ║
# ║      back away slowly, and reflect on your life choices.           ║
# ║                                                                    ║
# ║  ...Unless you paid me and I agreed, preferably in writing,        ║
# ║              or over drinks. I'm flexible.                         ║
# ║                                                                    ║
# ║    Violators will be subject to legal action and possibly a        ║
# ║         13-episode redemption arc—if you’re lucky.                 ║
# ║                                                                    ║
# ║     This warning is legally binding and magically cursed.          ║
# ║                                                                    ║
# ║              Respect the code. Pet the Fox.                        ║
# ║                                                                    ║   
# ║                      /\   /\                                       ║   
# ║                     //\\_//\\     ____                             ║        
# ║                     \_     _/    /   /                             ║        
# ║                      / * * \    /^^^]                              ║       
# ║                      \_\O/_/    [   ]                              ║       
# ║                       /   \_    [   /                              ║       
# ║                       \     \_  /  /                               ║      
# ║                        [ [ /  \/ _/                                ║     
# ║                       _[ [ \  /_/                                  ║     
# ╠════════════════════════════════════════════════════════════════════╣
# ║  You MAY use this code freely for **non-commercial** projects,     ║
# ║  as long as you keep this copyright notice AND this entire block   ║
# ║                      intact and visible.                           ║
# ║                                                                    ║
# ║  TL;DR: If you're not making money, you're good. If you are,       ║
# ║  don’t be a gremlin. Ask nicely. I'll probably  want               ║
# ║                 a copy of the game ;)                              ║
# ║                                                                    ║
# ║  Reach out via Discord:   kesa_   (tag me in the Ren'Py server     ║
# ║  or add me directly).                                              ║
# ╠════════════════════════════════════════════════════════════════════╣
# ║  Want help coding your game? Reach out!                            ║
# ╚════════════════════════════════════════════════════════════════════╝

####################################################
#### 900 lines of stress. AKA the phone system #####
####################################################

default typing_dot_cycle = ["", ".", "..", "..."]
default typing_dots = "" 
 
init python:

    import math # YAY MATH :D

    # Look..... i tried... okay? I cant do styling :')

    style.rounded_button = Style("text_button")
    style.rounded_button.background = Frame(Solid("#eeeeee"), 12, 12)  
    style.rounded_button.hover_background = Frame(Solid("#aaaaff"), 12, 12)  
    style.rounded_button.padding = (8, 8)
    style.rounded_button.xminimum = 140
    style.rounded_button.yminimum = 40

    def complete_conversation(contact):
        index_var_name = contact['current_index']
        while len(contact['current_dialogue']) > getattr(store, index_var_name):
            current_index = getattr(store, index_var_name)
            print("appending - ", contact['current_dialogue'][current_index])
            contact['all_dialogue'].append(contact['current_dialogue'][current_index])
            setattr(store, index_var_name, current_index + 1)



    import renpy.store as store
 
    def send_message_now(contact_map, message):
        contact_map['all_dialogue'].append({contact_map['name']:message, 'seen':True})

    def add_next_line(character_info):
        dialogue_name = character_info["current_dialogue"]
        if isinstance(dialogue_name, str):
            dialogue_list = getattr(store, dialogue_name)
        else:
            dialogue_list = dialogue_name
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        if idx < len(dialogue_list):
            entry = dialogue_list[idx]
            character_info["all_dialogue"].append(entry)
            setattr(store, index_name, idx + 1)
            character_info["scroll_to_bottom"] = True



    def conditional_add_line(character_info):
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        dialogue_name = character_info["current_dialogue"]
        dialogue_list = getattr(store, dialogue_name) if isinstance(dialogue_name, str) else dialogue_name
        if idx >= len(dialogue_list):
            return
        entry = dialogue_list[idx]
        if isinstance(entry, dict):
            add_next_line(character_info)
        elif isinstance(entry, list):
            renpy.show_screen('dynamic_scrollable_text', character_info, True)


    def handle_choice(choice_var_name, character_info):
        choice_list = getattr(store, choice_var_name)
        character_info["all_dialogue"].append(choice_list[0])
        character_info["scroll_to_bottom"] = True
        character_info_name = get_store_name_of(character_info)
        update_current_convo(character_info_name, {
            "current_dialogue": choice_list,
            "current_index": f"{choice_var_name}_index",
            "scroll_to_bottom": True
        })

    renpy.restart_interaction()


    def auto_advance_to_player(character_info, name = "me"):
        index_name = character_info["current_index"]
        idx = getattr(store, index_name)
        dialogue_list = character_info["current_dialogue"]
        if isinstance(dialogue_list, str):
            dialogue_list = getattr(store, dialogue_list)
        if idx < len(dialogue_list):
            entry = dialogue_list[idx]
            if isinstance(entry, dict) and list(entry.keys())[0] == name:
                return
            if isinstance(entry, list):
                return
            character_info["all_dialogue"].append(entry)
            character_info["scroll_to_bottom"] = True
            setattr(store, index_name, idx + 1)
            renpy.restart_interaction()
    
    def show_choices_now(character_info):
        return [Hide("dynamic_scrollable_text"), Show("dynamic_scrollable_text", character_info=character_info, continue_list=True)]
    
    def unlock_image(filename):
        for data in gallery_data.values():
            for path in data["images"]:
                if path.endswith(filename):
                    if path not in unlocked_images:
                        if persistent_gallery:
                            persistent.persistent_gallery.append(path)
                            renpy.save_persistent()
                        else:
                            unlocked_images.append(path)


    def soft_delete_by_value(character_info, value):
        try:
            index = next(i for i, d in enumerate(character_info["all_dialogue"]) if value in d.values())
            if character_info["all_dialogue"][index]:
                for key, item in character_info["all_dialogue"][index].items():
                    if item == value:
                        character_info["all_dialogue"][index] = {"system":deleted_message_replacement}
                        character_info["all_dialogue"].pop()
        except (StopIteration, IndexError):
            pass

    # If you want to handle more message types you can add them in here, this is just what it does based on the key entered
    # Remember to .pop() it if its a message that shouldnt be seen :)
    def handle_message_type(entry, character_info):
        key, value = list(entry.items())[0]
        def handle_delete(character_info, value):
            soft_delete_by_value(character_info, value)
        def handle_image(character_info, value):
            unlock_image(value)
        def handle_code(character_info, value):
            character_info["all_dialogue"].pop()
            exec(value, globals())
        def handle_nothing(character_info, value):
            pass
        handle_map = {
            "delete": handle_delete,
            "image": handle_image,
            "code": handle_code
        }
        handle_map.get(key, handle_nothing)(character_info, value)
            
            
    # Why is this defined here and not at the top? Well, thats because...... yep.....
    # Why did i write that instead of just moving it with the rest?
    # Why am I still adding comments?!?!?!?!?? AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
    skipping_messages_enabled = False

    # WHYYY DID THIS TAKE 3 HOURSSSS WHEN ADDING THE SKIP FEATUREEEEE
    def calculate_message_delay(persistant_message_index, true_current_index, current_character_name):
        global skipping_messages_enabled
        message_timer_delay = skip_speed_timer
        if current_character_name != current_contact:
            return message_timer_delay
        if persistant_message_index <= true_current_index:
            skipping_messages_enabled = False
            min_speak_timer = original_min_speak_timer
        if not static_speak_timer and not skipping_messages_enabled:
            try:
                message_timer_delay = max(min_speak_timer, min(len(list(character_info_for_dialogue['current_dialogue'][true_current_index + 1].values())[0]) * (auto_speak_timer * 0.025), max_speak_timer))
            except Exception:
                # It doesnt like it when the next chat is a choice (so list of lists), this just stops it breaking
                message_timer_delay = auto_speak_timer
        elif not skipping_messages_enabled:
            message_timer_delay = auto_speak_timer
        return message_timer_delay


    # SOOOOOOOOOOOO ive added this because... i realised that updating mirrored convos needs to be done.... manually
    # as long as you named things CORRECTLY this will update it all, both peoples perspectives.
    def update_current_convo(main_name, update_dict):
        # Update the main one
        if hasattr(store, main_name):
            getattr(store, main_name).update(update_dict)

        # Try the reversed name
        parts = main_name.replace("_full_info", "").split("_")
        if len(parts) == 2:
            reversed_name = f"{parts[1]}_{parts[0]}_full_info"
            if hasattr(store, reversed_name):
                getattr(store, reversed_name).update(update_dict)               
        
    # Yayyy turning variable names into strings to use as variable names BECAUSE WHY NOT!
    def get_store_name_of(obj):
        for k, v in store.__dict__.items():
            if v is obj:
                return k
        return None

transform slide_in_right:
    xoffset 300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0

transform slide_in_left:
    xoffset -300
    alpha 0.0
    linear 0.3 xoffset 0 alpha 1.0



# ----------------------------------------#
#          Dialogue Screen                #
# ----------------------------------------#
screen dynamic_scrollable_text(character_info_for_dialogue, continue_list=False):
    
    # Going to leave this here and I hope someone will see this and explain it to me
    # If you uncomment this print statement it will show you that this is running over characters that you did not click
    # on character select. It is itterating over the info of every single contact, and I have absolutely no idea why????
    # I've added code so that this doesn't actually matter, but still, WHY?!
    #python:
    #    print(character_info_for_dialogue)



    # I dont even know if these are needed anymore... I changed so many things I lost track.....
    python:
        if 'skipping_messages_enabled' not in globals():
            skipping_messages_enabled = False
        try:
            message_timer_delay = message_timer_delay or auto_speak_timer
        except NameError:
            message_timer_delay = auto_speak_timer

    default yadj = renpy.display.behavior.Adjustment()

    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7

    python:
        if isinstance(character_info_for_dialogue["current_dialogue"], str):
            character_info_for_dialogue["current_dialogue"] = getattr(store, character_info_for_dialogue["current_dialogue"])
    

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    $ jump_to_choices = False
    $ full_list = character_info_for_dialogue["current_dialogue"]
    $ work_list_name = character_info_for_dialogue["all_dialogue"]
    $ index_name = character_info_for_dialogue["current_index"]
    $ end_of_dialogue = False


    python:
        # Logging seen messages to persistant for the skip function
        if index_name not in persistent.seen_message_threads:
            persistent.seen_message_threads[index_name] = 0
        true_current_index = getattr(store, character_info_for_dialogue["current_index"])
        persistant_message_index = persistent.seen_message_threads[index_name]
        message_time_delay = calculate_message_delay(persistant_message_index, true_current_index, character_info_for_dialogue['name'])
        persistent.seen_message_threads[index_name] = max(true_current_index, persistent.seen_message_threads.get(index_name, true_current_index))

        for entry in work_list_name:
            key, value = list(entry.items())[0]
            handle_message_type(entry, character_info_for_dialogue)
    
        full_list = globals().get(full_list) if isinstance(full_list, str) else full_list

    zorder 100
    

    frame:
        background None
        xalign 0.5 yalign 0.5
        xsize 410 ysize 800
        
        has viewport yadjustment yadj id "my_viewport":
            draggable True
            mousewheel True
            vbox:
                xsize 380  
                spacing 5
                for entry in work_list_name:
                    $ key, value = list(entry.items())[0]

                    if key == "image":
                        if 'scale' in entry:
                            $ imgwidth = entry['scale'][0]
                            $ imgheight = entry['scale'][1]
                        else:
                            $ imgwidth, imgheight = chat_image_size[0], chat_image_size[1]
                        button:
                            action Show("fullscreen_image", image_path=value)
                            background None
                            add Image(value) size (imgwidth, imgheight)
                    

                    # Completely untested currently, should work?
                    elif key == "video" and not entry.get('seen', False):
                        $ video_path = value["file"]
                        $ thumbnail = value.get("thumbnail", "gui/video_thumbnail.png")
                        button:
                            action Show("fullscreen_video", video_path=video_path)
                            background None
                            add Image(thumbnail) size (216, 384)

                    else:
                        $ speaker = key
                        $ line = value
                        $ color = speaker_colors.get(speaker, "#333333")
                        if speaker == phone_data['name']:
                            if not entry.get('seen', False) and message_animations:
                                frame at slide_in_right:
                                    background Frame("gui/bubble_sent.png", 4, 4)
                                    padding (20, 20)
                                    xalign 1.0
                                    xmaximum 300

                                    has vbox
                                    text line color color size 20 substitute False
                            else:
                                frame:
                                    background Frame("gui/bubble_sent.png", 4, 4)
                                    padding (20, 20)
                                    xalign 1.0
                                    xmaximum 300
                                    has vbox
                                    text line color color size 20 substitute False
                        elif speaker == "system":
                            frame:
                                text line color "#797979ff" size 15
                                background None
                                xalign 0.5
                        
                        

                        else:
                            if not entry.get('seen', False) and message_animations:
                                frame at slide_in_left:
                                    background Frame("gui/bubble_recieved.png", 4, 4)
                                    padding (20, 20)
                                    xalign 0
                                    xmaximum 300

                                    has vbox
                                    text line color color size 20 
                            else:
                                frame:
                                    background Frame("gui/bubble_recieved.png", 4, 4)
                                    padding (20, 20)
                                    xalign 0
                                    xmaximum 300

                                    has vbox
                                    text line color color size 20 
        
    python:
        for entry in work_list_name:
            if not entry.get('seen', False):
                entry['seen'] = True
    
    if continue_list == False:

        python:
            auto_continue = True
            idx = getattr(store, character_info_for_dialogue["current_index"])
            if idx < len(full_list):
                next_entry = full_list[idx]
                if isinstance(next_entry, dict) and list(next_entry.keys())[0] == phone_data['name'] and click_to_send:
                    is_typing = False
                    auto_continue = False
                elif isinstance(next_entry, list):
                    jump_to_choices = True
                
    
        if jump_to_choices:
            timer 0.01 action [
            SetDict(character_info_for_dialogue, "scroll_to_bottom", True),
            Hide("dynamic_scrollable_text"),
            Show("dynamic_scrollable_text", character_info_for_dialogue=character_info_for_dialogue, continue_list=True)
            ]
        if auto_continue:
 
            if idx < len(full_list) and character_info_for_dialogue['name'] == current_contact:
                $ is_typing = True
            else:
                $ is_typing = False
            if phone_data.get("name") == character_info_for_dialogue.get("owner") and character_info_for_dialogue.get("enable_messaging", True):
                timer message_time_delay repeat True action Function(auto_advance_to_player, character_info_for_dialogue)
        
        else:
            fixed:
                button:
                    action Function(conditional_add_line, character_info_for_dialogue)
                    background None
                    xpos 1200
                    ypos 850
                    xsize 60
                    ysize 60
                    add "gui/message_icon.png" xysize (60, 60) at truecenter
                    hover_background "#666666"

    else: 
        $ choice_list = full_list[-1]
        vbox:
            xalign 0.5
            yalign 0.5
            xoffset 500
            spacing 10
            for choice in choice_list:
                textbutton choice[0] style "rounded_button":
                    text_color "#000000"
                    action [Function(handle_choice, choice[1], character_info_for_dialogue), Show("dynamic_scrollable_text", character_info_for_dialogue = character_info_for_dialogue, continue_list=False)]


    python:
        if character_info_for_dialogue.get("scroll_to_bottom", False):
            yadj.value = float('inf')
            character_info_for_dialogue["scroll_to_bottom"] = False  


            

    if is_typing and is_typing_indicator:    
        timer 0.4 repeat True action  Function(lambda: setattr(store, "typing_dots", typing_dot_cycle[(typing_dot_cycle.index(typing_dots) + 1) % len(typing_dot_cycle)])) 
        frame:
            xmaximum 300
            xalign 0.48
            yalign 0.88
            padding (10, 5)
            background None
            vbox:
                xfill True
                text is_typing_message + typing_dots size 15 color "#000000" xanchor 0 italic True
    

    # Skip button show logic
    # Adding this... was pain... true pain.... renpy screens are STUPID 

    if persistent.seen_message_threads[index_name] > true_current_index and show_skip_button:
        if not skipping_messages_enabled:
            button:
                action [SetVariable("message_timer_delay", skip_speed_timer), 
                SetVariable("skipping_messages_enabled", True), 
                SetVariable("min_speak_timer", 0)
                ]
                background None
                xpos 0.7
                ypos 0.3
                add "gui/skip_button.png" xysize(50,50)
        else:
            button:
                action [SetVariable("message_timer_delay", auto_speak_timer), 
                SetVariable("skipping_messages_enabled", False), 
                SetVariable("min_speak_timer", original_min_speak_timer)
                ]
                background None
                xpos 0.7
                ypos 0.3
                add "gui/skip_button_selected.png" xysize(50,50)



    button:
        action [Hide("dynamic_scrollable_text"), Show("character_select")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)


# ----------------------------------------#
#          Fullscreen Videos              #
# ----------------------------------------#


screen fullscreen_video(video_path):
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]
    tag fullscreen_video
    modal True
    zorder 200

    add Movie(size=(1280, 720), play=video_path) xalign 0.5 yalign 0.5

    key "dismiss" action Hide("fullscreen_video")
    button:
        action Hide("fullscreen_video")
        background None
        xfill True
        yfill True

# ----------------------------------------#
#          Fullscreen images              #
# ----------------------------------------#
 

screen fullscreen_image(image_path, background = False):
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]
    tag fullscreen_image  
    modal True
    zorder 200  

    add image_path:
        xalign 0.5
        yalign 0.5
        fit "contain"  

    

    key "dismiss" action Hide("fullscreen_image")  
    button:
        action Hide("fullscreen_image")
        background None
        xfill True
        yfill True

    if background:
        button:
            background None
            xpos 1200
            ypos 850
            xsize 60
            ysize 60
            add "gui/confirm_tick.png" xysize (60, 60) at truecenter
            action [Function(lambda path=image_path: phone_data['background'].__setitem__(0, path)), Hide("fullscreen_image")]


# ----------------------------------------#
#          Character Select               #
# ----------------------------------------#
screen character_select():
    
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]
    tag character_select
    modal True
    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7

    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 800
        padding (30, 30)
        background None

        has viewport:
            mousewheel True
            draggable True

            vbox:
                spacing 30
                xalign 0.5

                text "Contact List":
                    size 36
                    color "#000000"
                    xalign 0.5

                $ unlocked_contacts = [char for char in phone_data["contacts"] if char["unlocked"]]

                for char in unlocked_contacts:
                    $ profile = char["profile"]
                    $ name = char["name"]

                    button:
                        action [
                            Hide("dynamic_scrollable_text"),
                            Function(lambda char=char: char.__setitem__("scroll_to_bottom", True)),
                            SetVariable("current_contact", char["name"]),
                            Show("dynamic_scrollable_text", character_info_for_dialogue=char)
                        ]
                        background None
                        has hbox:
                            spacing 20
                            xalign 0.5

                            fixed:
                                xysize (100, 100)

                                add profile size (100, 100)

                                $ char_current_index = getattr(store, char['current_index'])
                                $ char_current_dialogue = char['current_dialogue']
                                if isinstance(char_current_dialogue, str):
                                    $ char_current_dialogue = getattr(store, char_current_dialogue)
                                if char_current_index < len(char_current_dialogue):
                                    add "gui/unread.png":
                                        size (60, 60)
                                        xpos 60
                                        ypos 0

                            text name:
                                size 28
                                color "#000000"
                                yalign 0.5



    button:
        action [Hide("character_select"), Show("phone_home")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)

# ----------------------------------------#
#             Gallery Screen              #
# ----------------------------------------#

screen gallery_character_select():
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    $ rows = math.ceil(len(character_names_to_scan)/image_columns)

    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7
    tag gallery
    modal True
    zorder 100

    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 800
        padding (30, 30)
        background None

        has viewport:
            mousewheel True
            draggable True
            
            grid image_columns rows spacing 30:

                for char_name, data in phone_data['gallery'].items():
                    $ profile = data["gallery image"]

                    button:
                        action Show("gallery_view_screen", character=char_name)
                        add profile size (100, 100)

    button:
        action [Hide("gallery_character_select"), Show("phone_home")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)

# ----------------------------------------#
#          Gallery View Screen            #
# ----------------------------------------#

screen gallery_view_screen(character):
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]
    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7
    tag gallery_view
    modal True
    zorder 100

    $ images = gallery_data[character]["images"]

    $ rows = math.ceil(len(images)/image_columns)

    $ all_unlocked = list(set(unlocked_images + (persistent.persistent_gallery or [])))

    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 800
        background None

        has viewport:
            mousewheel True
            draggable True

            vbox:
                xalign 0.5
                yalign 0.5
                xsize 350
                ysize 800
                grid image_columns rows spacing 20:
                    for img_path in images:
                        if img_path in all_unlocked:
                            vbox:
                                xsize 155
                                ysize 276
                                button:
                                    xsize 155
                                    ysize 276
                                    action Show("fullscreen_image", image_path=img_path)
                                    add img_path size (155, 276)  
                        else:
                            vbox:
                                xsize 155
                                ysize 276
                                fixed:
                                    xsize 155
                                    ysize 276
                                    add img_path size (155, 276)  
                                    add Solid("#000000e9") xysize (155, 276)

    button:
        action [Hide("gallery_view_screen"), Show("gallery_character_select")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)

# ----------------------------------------#
#        Background select screen         #
# ----------------------------------------#

screen background_select:

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7    

    $ images = phone_backgrounds

    $ rows = math.ceil(len(phone_backgrounds)/image_columns)

    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 800
        background None

        has viewport:
            mousewheel True
            draggable True
            
            vbox:
                xalign 0.5
                yalign 0.5
                xsize 350
                ysize 800
                grid image_columns rows spacing 20:
                    for img_path in images:
                        button:
                            xsize 155
                            ysize 276
                            action Show("fullscreen_image", image_path=img_path, background = True)
                            add img_path size (155, 276)  

    button:
        action [Hide("background_select"), Show("phone_home")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)

# ----------------------------------------#
#            Settings Screen              #
# ----------------------------------------#

screen phone_settings_screen():
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7

    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]

    tag settings
    modal True
    zorder 100
    if allow_speed_adjust:
        frame:
            xalign 0.5
            yalign 0.5
            xsize 400
            ysize 800
            padding (30, 30)
            background None
            vbox:
                spacing 5
                xalign 0.5

                text "Average Message Delay" size 24 xalign 0.5 
                text "[auto_speak_timer:.2f] seconds" size 18 xalign 0.5

                bar:
                    value VariableValue("auto_speak_timer", min=1.0, max=5.0, step=0.1)
                    xmaximum 300
                    ymaximum 12
                    left_bar Solid("#aaaaff")
                    right_bar Solid("#dddddd")
                    thumb Solid("#444")

  




    button:
        action [Hide("phone_settings_screen"), Show("phone_home")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)


# ----------------------------------------#
#              Home Screen                #
# ----------------------------------------#


screen phone_home():
    on "show" action [
        SetVariable("_save_enabled", False),
        SetVariable("_game_menu_screen", None),
        SetVariable("_rollback", False),
    ]

    on "hide" action [
        SetVariable("_save_enabled", True),
        SetVariable("_game_menu_screen", "save_screen"),
        SetVariable("_rollback", True),
    ]
    add "images/gui/phone_boarder.png" xpos 600 ypos 0 zoom 0.7
    add phone_data['background'][0] xpos 600 ypos 0 zoom 0.7
    python:
        renpy.hide("phone_icon_overlay")
    tag phone_home
    modal True
    frame:
        xalign 0.5
        yalign 0.5
        xsize 400
        ysize 800
        background None


        vbox:
            spacing 20
            xalign 0.5
            yalign 0.3

            hbox:
                spacing 40
                xalign 0.5

                button:
                    xysize (100, 100)
                    background Frame("gui/message_icon.png", 10, 10)
                    action [Show("character_select"), Hide("phone_home")]

                button:
                    xysize (100, 100)
                    background Frame("gui/gallery_icon.png", 10, 10)
                    action Show("gallery_character_select")
                if settings_screen_shown:
                    button:
                        xysize (100, 100)
                        background Frame("gui/settings_icon.png", 10, 10)
                        action Show("phone_settings_screen")
                else:
                    button:
                        xysize (100, 100)

            hbox:
                spacing 40
                xalign 0.5

                button:
                    xysize (100, 100)
                    background Frame("gui/background_icon.png", 10, 10)
                    action Show("background_select")

                button:
                    xysize (100, 100)

                button:
                    xysize (100, 100)


    button:
        action [Show("phone_icon_overlay"), Hide("phone_home")]
        background None
        xpos 0.7
        ypos 0.9
        add "gui/back_button.png" xysize(50,50)









