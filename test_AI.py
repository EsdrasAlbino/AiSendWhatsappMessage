import pyautogui
from PIL import Image
from ultralytics import YOLO
import threading


def run_bot(decision):

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


# Function to take screenshots
def take_screenshot(stop_event, model):
    pyautogui.FAILSAFE = False

    while not stop_event.is_set():

        decision = {
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

        # Take screenshot
        screenshot = pyautogui.screenshot(region=(700, 50, 500, 980))
        screenshot = Image.frombytes(
            'RGB', screenshot.size, screenshot.tobytes())
        # return a list of Results objects
        results = model([screenshot], conf=.30)
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
                decision["WhatsappApp"] = True
                decision["WhatsappApp_location"] = (center_x, center_y)
            elif name == "AddContact":
                decision["AddContact"] = True
                decision["AddContact_location"] = (center_x, center_y)
            elif name == "Search":
                decision["Search"] = True
                decision["Search_location"] = (center_x, center_y)
            elif name == "NewContact":
                decision["NewContact"] = True
                decision["NewContact_location"] = (center_x, center_y)
            elif name == "SaveNewContact":
                decision["SaveNewContact"] = True
                decision["SaveNewContact_location"] = (center_x, center_y)
            elif name == "ExistNumber":
                decision["ExistNumber"] = True
                decision["ExistNumber_location"] = (center_x, center_y)
            elif name == "NoExistNumber":
                decision["NoExistNumber"] = True
                decision["NoExistNumber_location"] = (center_x, center_y)
            elif name == "WidgetOpenGallery":
                decision["WidgetOpenGallery"] = True
                decision["WidgetOpenGallery_location"] = (center_x, center_y)
            elif name == "GalleryButton":
                decision["GalleryButton"] = True
                decision["GalleryButton_location"] = (center_x, center_y)
            elif name == "OptionsGallery":
                decision["OptionsGallery"] = True
                decision["OptionsGallery_location"] = (center_x, center_y)
            elif name == "GaleriaButton":
                decision["GaleriaButton"] = True
                decision["GaleriaButton_location"] = (center_x, center_y)
            elif name == "FolderOlimpic":
                decision["FolderOlimpic"] = True
                decision["FolderOlimpic_location"] = (center_x, center_y)
            elif name == "InputToSendMessage":
                decision["InputToSendMessage"] = True
                decision["InputToSendMessage_location"] = (center_x, center_y)
            elif name == "SendMessage":
                decision["SendMessage"] = True
                decision["SendMessage_location"] = (center_x, center_y)
        print(decision)
        # run_bot(decision)


# Main function
def main():
    # print(pyautogui.KEYBOARD_KEYS)
    model = YOLO('weights/best.pt')
    stop_event = threading.Event()

    # Create and start the screenshot thread
    screenshot_thread = threading.Thread(
        target=take_screenshot, args=(stop_event, model))
    screenshot_thread.start()

    # Listen for keyboard input to quit the program
    # keyboard.wait("q")

    # Set the stop event to end the screenshot thread
    stop_event.set()

    # Wait for the screenshot thread to finish
    screenshot_thread.join()

    print("Program ended.")


if __name__ == "__main__":
    main()
