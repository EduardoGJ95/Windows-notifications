#Librerias
import time
import winsound
from win10toast import ToastNotifier

def timer(message,minutes):
    notificator = ToastNotifier()

    notificator.show_toast("FIDEV", f"Prepárate en {minutes} minutos.", duration = 2)

    time.sleep(2)
    winsound.Beep(frequency = 250, duration = 2)

    notificator.show_toast(f"!Alarma¡", message, duration = 2)

if __name__ == "__main__":

    message = "Hola, Eduardo!"
    minutes = 0.5
    timer(message, minutes) 