###############################
####  AUTOFILLING GALLERY  ####
###############################

# This code will go through EVERY image in your game folder, check if they start with a given name, if they do it will
# dynamically create a gallery for that character within the phone. 

# In python 1 init (below this) there is a list called 'character_names_to_scan', just list all your characters in there and then
# it will take every image that starts with 'thatname_'. So for example if i created the list as ['sarah','nova']
# it will scan for every image thats name starts with 'sarah_' and add them to her own gallery, and then 
# create a seperate gallery for images that start 'nova_'. 

# There are two exceptions to this. Images that end _profile are used for profile pictures on the phone and will not 
# appear in the gallery. So 'sarah_profile.png' is a profile picture and wont be added.

# The second is any images ending '_x'. This is purely to allow you to easily exclude images from showing in the gallery
# so an image called 'sarah_bedroom_x.png' will not show, even through it starts with 'sarah_'

# All images in the gallery will start greyed out, 'just' visible and need to be unlocked. This happens automatically 
# if the image is shown throught the text system I created, no need to do anything. 

# If the image is outside of that system though simply use the function unlock_image(image.png)
# that will automatically find the correct file path for the image, check it isnt already added and then add it
# so running unlock_image("sarah_shopping.png") will search for and append "images/sarah/sarah_shopping.png"
# to the unlocked images, if it isnt there already. No need to find and type the full file path!

# You can enable persistant cross save gallry unlocks in the config.rpy file. Just set it to True. 

init python:
    import os
    def build_gallery_data_from_prefixes(character_names, image_root="images"):
        base_path = os.path.dirname(renpy.loader.transfn("gallery_system.rpy"))  
        images_path = os.path.join(base_path, image_root)

        gallery_data = {}

        for char_name in character_names:
            prefix = char_name.lower() + "_"
            profile_filename = f"{char_name.lower()}_profile.png"
            images = []

            for root, _, files in os.walk(images_path):
                for file in files:
                    if not file.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                        continue
                    if not file.lower().startswith(prefix):
                        continue
                    if file.lower() == profile_filename:
                        continue  
                    if os.path.splitext(file)[0].endswith("_x"):
                        continue  

                    full_path = os.path.join(root, file)
                    rel_path = os.path.relpath(full_path, base_path).replace("\\", "/")

                    images.append(rel_path)

            if images:
                gallery_data[char_name] = {
                    "gallery image": f"{char_name.lower()}/{profile_filename}",
                    "images": sorted(images)
                }

        return gallery_data




init 1 python:
    character_names_to_scan = ["test", "iris"]
    gallery_data = build_gallery_data_from_prefixes(character_names_to_scan)
    for char_data in gallery_data.values():
        char_data["images"] = sorted(list(set(char_data["images"])))
    try:
        max_gallery_length = max(len(data["images"]) for data in gallery_data.values())
        if max_gallery_length % 2 != 0:
            max_gallery_length += 1
    except ValueError: 
        # Gallery is empty :c
        pass
    
    if not hasattr(persistent, "persistent_gallery"):
        persistent.persistent_gallery = []


# Want to start with some images unlocked? Add them in here!
default unlocked_images = ['add_your_image_path_here.png']


