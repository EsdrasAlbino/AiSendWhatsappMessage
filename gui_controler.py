import time
import pyautogui
import pyperclip
from PIL import Image


def run_bot(decision):
    # Should we use lightning/met?

    if "buy_location" in decision:
        pyautogui.click(decision["buy_location"])
    elif "play_location" in decision:
        pyautogui.click(decision["play_location"])
        print("Pressing Play")
    elif "no_thanks_location" in decision:
        pyautogui.click(decision["no_thanks_location"])
        print("Pressing No Thanks")
    elif "continue_location" in decision:
        pyautogui.click(decision["continue_location"])
        print("Pressing Continue")
    elif "next_location" in decision:
        pyautogui.click(decision["next_location"])
    elif "fuel_location" in decision and decision["fuel_distance"] < 1000:
        pyautogui.moveTo(decision["fuel_location"])
    else:
        if decision["tree"] and decision["building"]:
            if decision["tree_distance"] + 300 < decision["building_distance"]:
                pyautogui.moveTo(decision["tree_location"])
                distance_target = decision["tree_distance"]
                print("Going to Tree: ", decision["tree_location"])
            else:
                pyautogui.moveTo(decision["building_location"])
                distance_target = decision["building_distance"]
                print("Going to Building: ", decision["building_location"])
        elif decision["tree"]:
            pyautogui.moveTo(decision["tree_location"])
            distance_target = decision["tree_distance"]
            print("Going to Tree: ", decision["tree_location"])
        elif decision["building"]:
            pyautogui.moveTo(decision["building_location"])
            distance_target = decision["building_distance"]
            print("Going to Building: ", decision["building_location"])

        # run_bot(decision)


class GUI_CONTROLLER:
    def __init__(self, model, stop_event):
        self.model = model
        self.stop_event = stop_event
        self.deslocation_left = 700
        self.deslocation_top = 50

        self.decision = {
            "WhatsappApp": False,
            "AddContact": False,
            "Search": False,
            "NewContact": False,
            "SaveNewContact": False,
            "ExistNumber": False,
            "NoExistNumber": False,
            "WidgetOpenGallery": False,
            "GalleryButton": False,
            "OptionsGallery": False,
            "GaleriaButton": False,
            "FolderOlimpic": False,
            "InputToSendMessage": False,
            "SendMessage": False,
        }
        self.ADD_CONTACT = False
        self.SEND_MESSAGE = False

    def back_button_mobile(self, times):
        for i in range(times):
            pyautogui.click(button='right')
            time.sleep(1)

    def add_contact_ai(self, decision, number):
        if "WhatsappApp_location" in decision:
            pyautogui.moveTo(decision["WhatsappApp_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
        elif "AddContact_location" in decision:
            pyautogui.moveTo(decision["AddContact_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
        elif "NewContact_location" in decision:
            pyautogui.moveTo(decision["NewContact_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
        elif "Input_location" in decision:
            pyautogui.moveTo(decision["Input_location"])
            time.sleep(1)
            pyautogui.click()
            pyautogui.write(number)
            time.sleep(2)
            pyautogui.moveTo(decision["InputNumber_location"])
            pyautogui.click()
            pyautogui.write(number)
            time.sleep(2)
        elif "SaveNewContact_location" in decision:
            if (self.decision["ExistNumber"] and not self.decision["NoExistNumber"]):
                pyautogui.click(
                    decision["SaveNewContact_location"], duration=1)
                time.sleep(2)
                self.back_button_mobile(1)
                self.ADD_CONTACT = True
                return True
            else:
                self.back_button_mobile(4)
                return False

    def send_message_ai(self, decision, number):
        if "Search_location" in decision:
            pyautogui.moveTo(decision["Search_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(1)
            pyautogui.write(number)
            time.sleep(5)
        elif "Contacts_location" in decision:
            # precision problem
            pyautogui.moveTo(decision["Contacts_location"])
            time.sleep(0.5)
            pyautogui.click()
        elif "WidgetOpenGallery_location" in decision:
            pyautogui.moveTo(decision["WidgetOpenGallery_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
        elif "GalleryButton_location" in decision:
            # precision problem
            pyautogui.moveTo(decision["GalleryButton_location"])
            time.sleep(0.5)
            pyautogui.click()
        elif "OptionsGallery_location" in decision:
            pyautogui.moveTo(decision["OptionsGallery_location"])
            time.sleep(0.5)
            pyautogui.click()
        elif "Options_location" in decision:
            pyautogui.moveTo(decision["Options_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(2)
        elif "GaleriaButton_location" in decision:
            pyautogui.moveTo(decision["GaleriaButton_location"])
            time.sleep(0.5)
            pyautogui.click()
            time.sleep(5)
        elif "FolderOlimpic_location" in decision:
            pyautogui.moveTo(decision["FolderOlimpic_location"])
            time.sleep(0.5)
            pyautogui.click()
        elif "ImageOlympic_location" in decision:
            pyautogui.moveTo(decision["ImageOlympic_location"])
            time.sleep(0.5)
            pyautogui.click()
        elif "InputToSendMessage_location" in decision:
            pyautogui.moveTo(decision["InputToSendMessage_location"])
            time.sleep(5)
            pyautogui.click()
            self.copy_message()
            time.sleep(2)
            # precision problem
            pyautogui.moveTo(decision["SendMessage_location"])
            time.sleep(2)
            pyautogui.click()
            self.SEND_MESSAGE = True

    def take_screenshot(self):

        pyautogui.FAILSAFE = False

        while not self.stop_event.is_set():

            self.decision = {
                "WhatsappApp": False,
                "AddContact": False,
                "Search": False,
                "NewContact": False,
                "SaveNewContact": False,
                "ExistNumber": False,
                "NoExistNumber": False,
                "WidgetOpenGallery": False,
                "GalleryButton": False,
                "Options": False,
                "GaleriaButton": False,
                "FolderOlimpic": False,
                "InputToSendMessage": False,
                "Input": False,
                "InputNumber": False,
                "Contacts": False,
                "ImageOlympic": False,
            }

            # Take screenshot
            screenshot = pyautogui.screenshot(
                region=(self.deslocation_left, self.deslocation_top, 500, 980))
            screenshot = Image.frombytes(
                'RGB', screenshot.size, screenshot.tobytes())

            # return a list of Results objects
            results = self.model([screenshot], conf=.10)
            boxes = results[0].boxes.xyxy.tolist()
            classes = results[0].boxes.cls.tolist()
            names = results[0].names
            confidences = results[0].boxes.conf.tolist()

            # Process results list
            for box, cls, conf in zip(boxes, classes, confidences):
                x1, y1, x2, y2 = box

                center_x = (x1+x2) / 2
                center_y = (y1+y2) / 2

                name = names[int(cls)]

                if name == "WhatsappApp":
                    self.decision["WhatsappApp"] = True
                    self.decision["WhatsappApp_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "AddContact":
                    self.decision["AddContact"] = True
                    self.decision["AddContact_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "Search":
                    self.decision["Search"] = True
                    self.decision["Search_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "NewContact":
                    self.decision["NewContact"] = True
                    self.decision["NewContact_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "SaveNewContact":
                    self.decision["SaveNewContact"] = True
                    self.decision["SaveNewContact_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "ExistNumber":
                    self.decision["ExistNumber"] = True
                    self.decision["ExistNumber_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "NoExistNumber":
                    self.decision["NoExistNumber"] = True
                    self.decision["NoExistNumber_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "WidgetOpenGallery":
                    self.decision["WidgetOpenGallery"] = True
                    self.decision["WidgetOpenGallery_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "GalleryButton":
                    self.decision["GalleryButton"] = True
                    self.decision["GalleryButton_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "OptionsGallery":
                    self.decision["OptionsGallery"] = True
                    self.decision["OptionsGallery_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "Options":
                    self.decision["Options"] = True
                    self.decision["Options_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "GaleriaButton":
                    self.decision["GaleriaButton"] = True
                    self.decision["GaleriaButton_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "FolderOlimpic":
                    self.decision["FolderOlimpic"] = True
                    self.decision["FolderOlimpic_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "InputToSendMessage":
                    self.decision["InputToSendMessage"] = True
                    self.decision["InputToSendMessage_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "SendMessage":
                    self.decision["SendMessage"] = True
                    self.decision["SendMessage_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "Contacts":
                    self.decision["Contacts"] = True
                    self.decision["Contacts_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "ImageOlympic":
                    self.decision["ImageOlympic"] = True
                    self.decision["ImageOlympic_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "Input":
                    self.decision["Input"] = True
                    self.decision["Input_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
                elif name == "InputNumber":
                    self.decision["InputNumber"] = True
                    self.decision["InputNumber_location"] = (
                        center_x+self.deslocation_left, center_y+self.deslocation_top)
            if not self.ADD_CONTACT and False:
                self.add_contact_ai(self.decision, "11999999999")
            if not self.SEND_MESSAGE:
                self.send_message_ai(self.decision, "81996387392")

    def copy_message(self):
        pyautogui.moveTo(900, 570, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(990, 570, 1)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.click(860, 520, duration=1)

    def add_contact(self, number):
        # Open WhatsApp Mobile
        pyautogui.click(1350, 1050, duration=1)

        # pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks,   interval=secs_between_clicks,     button='left')
        pyautogui.click(950, 580, duration=1)

        time.sleep(2)

        pyautogui.click(1150, 820, duration=2)

        time.sleep(1)

        pyautogui.click(1000, 280, duration=1)

        pyautogui.click(1000, 210, duration=1)

        pyautogui.write(number)

        time.sleep(2)

        pyautogui.click(1000, 350, duration=1)

        pyautogui.write(number)
        time.sleep(3)

        if (self.decision["ExistNumber"] and not self.decision["NoExistNumber"]):
            pyautogui.click(
                self.decision["SaveNewContact_location"], duration=1)
            time.sleep(2)
            pyautogui.click(button='right')
            return True
        else:
            self.back_button_mobile(4)
            return False

    def search_contact(self, number):
        time.sleep(1)
        pyautogui.click(1100, 150, duration=1)
        time.sleep(2)
        pyautogui.write(number)
        pyautogui.click(1000, 280, duration=1)

        self.back_button_mobile(2)

    def send_message_mobile(self, number):
        time.sleep(1)

        # Open WhatsApp Mobile
        pyautogui.click(1350, 1050, duration=1)

        # click in my contact to copy message
        pyautogui.click(870, 270, duration=1)
        time.sleep(1)
        pyautogui.moveTo(1050, 870, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(1080, 870, 1)
        pyautogui.mouseUp(button='left')
        time.sleep(1)
        pyautogui.moveTo(1150, 135, duration=1)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click(1050, 200, duration=1)
        time.sleep(1)
        pyautogui.click(button='right')
        time.sleep(1)

        # Search contact in WhatsApp
        pyautogui.click(1110, 140, duration=1)
        time.sleep(2)
        pyautogui.write(number)
        time.sleep(5)

        # Click in contact
        pyautogui.moveTo(940, 240, duration=1)
        pyautogui.click()
        time.sleep(5)

        # Move and click in wiget to open files
        pyautogui.moveTo(1000, 925, duration=1)
        pyautogui.click()

        time.sleep(2)

        # Open gallery view
        pyautogui.moveTo(1040, 630, duration=1)
        pyautogui.click()

        # Open gallery specific
        pyautogui.click(1157, 160, duration=1)
        pyautogui.click(1090, 220, duration=1)

        time.sleep(4)

        pyautogui.click(1050, 830, duration=1)

        time.sleep(2)

        pyautogui.click(800, 290, duration=1)

        time.sleep(4)

        # Click in input to write message
        pyautogui.click(900, 860, duration=1)
        time.sleep(2)

        # pressed input to copy text
        pyautogui.moveTo(900, 570, duration=1)
        pyautogui.mouseDown(button='left')
        pyautogui.moveTo(990, 570, 1)
        pyautogui.mouseUp(button='left')
        time.sleep(2)
        pyautogui.click(860, 520, duration=1)

        # send mensage
        pyautogui.moveTo(1150, 600, duration=1)
        pyautogui.doubleClick()

        self.back_button_mobile(3)

        # Close WhatsApp Mobile
        pyautogui.click(1350, 1050, duration=1)

    def send_message_desktop(self, msg):
        time.sleep(2)

        # Open WhatsApp Desktop
        pyautogui.click(1290, 1050, duration=1)

        # Search for the contact specified by the number
        # pyautogui.moveTo(610, 150, duration=1)
        # pyautogui.click()
        # time.sleep(2)
        # pyautogui.typewrite(number)

        # Click on the contact search
        pyautogui.click(570, 240, duration=1)

        # Click on widget to open files
        # pyautogui.moveTo(88819963873920, 970, duration=1)
        # pyautogui.click()
        # pyautogui.moveTo(880, 720, duration=1)
        # pyautogui.doubleClick()

        # Select image to send
        # pyautogui.moveTo(390, 250, duration=1)
        # pyautogui.click()
        # pyautogui.moveTo(1190, 200, duration=1)
        # pyautogui.doubleClick()

        # Write message and send message
        pyperclip.copy(msg)
        time.sleep(2)

        pyautogui.hotkey('ctrl', 'v')
        # pyautogui.write(msg)

        time.sleep(2)
        pyautogui.press('enter')
