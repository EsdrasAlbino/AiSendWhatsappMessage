import time
import gspread
import threading
from ultralytics import YOLO
import gui_controler


def check_number(number):
    try:
        print(number)

        if (len(number[6:15]) >= 9):
            return True
        return False
    except:
        return False


def main():
    gc = gspread.service_account()
    sh = gc.open("Controle_Escolas")
    worksheet = sh.get_worksheet(0)
    model = YOLO('weights/best.pt')
    stop_event = threading.Event()

    gui_control = gui_controler.GUI_CONTROLLER(model, stop_event)

    idx = 1320

    while True:
        try:
            values_list = worksheet.row_values(idx)
            time.sleep(2)
            print(values_list)

            if not values_list[9] and values_list[13] == "Esdras":
                print(f"enviado para: {values_list[1]}")

                number = values_list[4].replace(" ", "").replace(
                    "(", "").replace(")", "").replace("-", "")
                number_valid = check_number(values_list[4])
                instituition_name = values_list[1]
                print(f"number_valid: {number_valid}")

                if (number_valid):

                    msg = f"Olá, {instituition_name}, tudo bem? Eu sou o Esdras Albino.\n\nFelipe Baldi, fundador da Tangram Educação Financeira, me passou seu contato.\nEle me disse que vocês poderiam se interessar em participar da Olimpíada Tangram, a maior Olimpíada de Educação Financeira do Brasil.\n\nA Tangram foi nomeada, pelo Instituto XP, a melhor solução de Educação Financeira do Brasil para escolas, no ano passado.\n\nTenho um material aqui explicando sobre a Olimpíada. Você tem interesse em saber como vai funcionar?"

                    number_valid = gui_control.add_contact(number)

                    if (number_valid):
                        # gui_control.search_contact(number)
                        gui_control.send_message_desktop(msg)
                        gui_control.send_message_mobile(number)

                        time.sleep(5)
                        worksheet.update_cell(
                            idx, 11, "Não viu")
                    else:
                        print("Número não existe numero")
                        worksheet.update_cell(idx, 11, "Número não existe")
                        time.sleep(5)

                    time.sleep(5)
                    worksheet.update_cell(
                        idx, 10, "1.1 - Prospecção e Qualificação")
                    time.sleep(5)
                    worksheet.update_cell(
                        idx, 13, "2")

            idx += 1

        except:
            time.sleep(5)
            print("error")
            idx += 1
            continue


main()
