import time
import gui_controler
import threading
from PIL import Image
from ultralytics import YOLO
import keyboard


number = "81996387392"
instituition_name = "Escola Estadual de Ensino Fundamental e Médio Professora Maria José de Vasconcelos"
msg = f"Olá, {instituition_name}, tudo bem? Eu sou o Esdras Albino.\n\nFelipe Baldi, fundador da Tangram Educação Financeira, me passou seu contato.\nEle me disse que vocês poderiam se interessar em participar da Olimpíada Tangram, a maior Olimpíada de Educação Financeira do Brasil.\n\nA Tangram foi nomeada, pelo Instituto XP, a melhor solução de Educação Financeira do Brasil para escolas, no ano passado.\n\nTenho um material aqui explicando sobre a Olimpíada. Você tem interesse em saber como vai funcionar?"

time.sleep(2)
model = YOLO('weights/whatsapp.pt')
stop_event = threading.Event()


gui_control = gui_controler.GUI_CONTROLLER(model, stop_event)

screenshot_thread = threading.Thread(
    target=gui_control.take_screenshot)
screenshot_thread.start()
input("Press Enter to continue...")
stop_event.set()
screenshot_thread.join()
# exist_number = gui_control.add_contact_ai(number=number)
# gui_control.search_contact(number)
# if exist_number:
#   gui_control.send_message_desktop(msg)
# gui_control.send_message_mobile(number)
# else:
#   print("Número não existe, não foi possível enviar a mensagem")
