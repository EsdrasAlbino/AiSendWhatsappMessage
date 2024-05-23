from ultralytics import YOLO

model = YOLO('weights/best.pt')

# return a list of Results objects
results = model(['img_140.jpg'], conf=.50, save=True)
boxes = results[0].boxes.xyxy.tolist()
classes = results[0].boxes.cls.tolist()
names = results[0].names
confidences = results[0].boxes.conf.tolist()

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


# Process results list
for box, cls, conf in zip(boxes, classes, confidences):
    x1, y1, x2, y2 = box

    center_x = (x1+x2) / 2
    center_y = (y1+y2) / 2

    confidence = conf
    detected_class = cls
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
