# Gui for the phones

init python:
    def check_phone_alert(phone_data):
        for character in phone_data["contacts"]:
            current_index = getattr(store, character["current_index"])
            current_dialogue = character["current_dialogue"]

            if isinstance(current_dialogue, str):
                current_dialogue = getattr(store, current_dialogue)

            if current_index < len(current_dialogue):
                return True  # Alert needed
        return False


screen phone_icon_overlay: 
    zorder 200
    
    imagebutton:
        idle "gui/phone_small.png"
        hover "gui/phone_small_hover.png"
        action [
            Hide("phone_icon_overlay"),
            ## EVERYTHING IN HERE NEEDS TO BE SET BEFORE A PHONE IS OPENED, IF YOURE NOT USING THIS GUI AS A TEMPLATE DO IT MANUALLY ##
            ## IF YOU'RE ONLY USING 1 PHONE JUST DO IT ONCE AT THE START OF THE GAME, THATS FINE TOO ##
            # This is what loads in the phone you click, change 'mc_phone' and it will load in another phone
            Function(lambda: phone_data.clear() or phone_data.update(mc_phone)),
            # Sets if this phones messages are click to send, or just send
            Function(lambda: setattr(store, "click_to_send", True)),
            Show("phone_home")
            ]
        xalign 0.99
        yalign 0.01
        at Transform(size=(154, 230))

    # Just hides the phone at the start of the game
    if sarah_phone_show:
        imagebutton:
            idle "gui/sarah_phone_small.png"
            hover "gui/sarah_phone_small_hover.png"
            action [
                Hide("phone_icon_overlay"),
                # only differences here are that we are updating phone_data with sarah_phone not MC phone, so it opens hers.
                # None of this needs to be some in a screen. You can just set it manually and call phone_home. Will still work.
                Function(lambda: phone_data.clear() or phone_data.update(sarah_phone)),
                # and then disabling click to send for this phone (well technically were disabling it globally...
                # But when you open a phone that does have it, like mc_phone, it sets to true)
                Function(lambda: setattr(store, "click_to_send", False)),
                Show("phone_home")
                ]
            xalign 0.95
            yalign 0.01
            at Transform(size=(154, 230))

    if iris_phone_show:
        imagebutton:
            idle "gui/iris_phone_small_x.png"
            hover "gui/iris_phone_small_hover_x.png"
            action [
                Hide("phone_icon_overlay"),
                Function(lambda: phone_data.clear() or phone_data.update(iris_phone)),
                Function(lambda: setattr(store, "click_to_send", True)),
                Show("phone_home")
                ]
            xalign 0.91
            yalign 0.01
            at Transform(size=(154, 230))

    if check_phone_alert(mc_phone):
        add "gui/unread.png" xpos 0.95 ypos 0.06 at Transform(anchor=(0.5, 0.0), size=(100, 100))
    if check_phone_alert(sarah_phone) and sarah_phone_show:
        add "gui/unread.png" xpos 0.915 ypos 0.06 at Transform(anchor=(0.5, 0.0), size=(100, 100))
    if check_phone_alert(iris_phone) and iris_phone_show:
        add "gui/unread.png" xpos 0.875 ypos 0.06 at Transform(anchor=(0.5, 0.0), size=(100, 100))


# Just here to show the variable change while the phone is opened
screen money_display:
    frame:
        xalign 0.0
        yalign 0.0
        padding (10, 10)
        text "Money: [money]"


label hide_all_gui:
    hide screen phone_icon_overlay
    $ renpy.hide_screen("phone_icon_overlay")
    $ renpy.restart_interaction()
    return 

label show_all_gui:
    show screen phone_icon_overlay
    show screen money_display
    $ renpy.restart_interaction()
    return 