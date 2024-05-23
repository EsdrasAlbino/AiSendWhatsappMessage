import os
import random
import shutil


class LabelUtils:

    def create_shuffled_images_folder(self):
        if not os.path.exists("shuffled_images"):
            os.mkdir("shuffled_images")

        image_files = [f for f in os.listdir("images") if f.endswith(".jpg")]
        random.shuffle(image_files)

        for img in image_files:
            os.rename(
                f"images/{img}", f"shuffled_images/img_{len(os.listdir('shuffled_images'))}.jpg")

    def create_labeled_images_zip_file(self):
        if not os.path.exists("obj"):
            os.mkdir("obj")

        file_prefixes = [f.split('.')[0] for f in os.listdir(
            "shuffled_images") if f.endswith(".txt")]

        for prefix in file_prefixes:
            os.rename(f"shuffled_images/{prefix}.txt", f"obj/{prefix}.txt")
            os.rename(f"shuffled_images/{prefix}.jpg", f"obj/{prefix}.jpg")

        shutil.make_archive('yolov4-tiny/obj', 'zip', '.', 'obj')

    def update_config_files(self, classes):
        with open("./yolov4-tiny/obj.names", "w") as file:
            file.write("\n".join(classes))

        with open("./yolov4-tiny/yolov4-tiny-custom_template.cfg", 'r') as file:
            cfg_content = file.read()

        updated_cfg_content = cfg_content.replace(
            '_CLASS_NUMBER_', str(len(classes)))
        updated_cfg_content = updated_cfg_content.replace(
            '_NUMBER_OF_FILTERS_', str((len(classes) + 5) * 3))
        updated_cfg_content = updated_cfg_content.replace(
            '_MAX_BATCHES_', str(max(6000, len(classes) * 2000)))

        with open("./yolov4-tiny/yolov4-tiny-custom.cfg", 'w') as file:
            file.write(updated_cfg_content)


# After creating the dataset (and shuffling the images), the next step is to label the images.
# (I recommend using https://www.makesense.ai/).
# After labeling the images, extract the content of the zip file from the makesense.ai webside and
# copy the .txt yolo label files into the "shuffled_images" folder and execute the following command
# to generate a zip file with the images and labels inside the yolov4-tiny folder.

lbUtils = LabelUtils()
lbUtils.create_labeled_images_zip_file()

# Now, fill this list with the classes you used in the makesense.ai.

# ***************************************************************************
# Make sure that you enter the exact same classes and in the exact same order!!!
# ***************************************************************************

# if you insert a different number than was used in the makesense.ai website the model wont work!

classes = ["WhatsappApp", "AddContact", "Search", "NewContact", "SaveNewContact", "ExistNumber", "NoExistNumber",
           "WidgetOpenGallery", "GalleryButton", "OptionsGallery", "GaleriaButton", "FolderOlimpic", "InputToSendMessage", "SendMessage"]

lbUtils = LabelUtils()
lbUtils.update_config_files(classes)
