import time
from win10toast import ToastNotifier
remTime= input("Input Time in 24hr format(HH:MM:SS) to set reminder\n>>>")
remMssg= input("Enter your message\n>>>")
while True:
    current_time=time.strftime("%H:%M:%S")
    if current_time == remTime:
        print(current_time)
        break
notify=ToastNotifier()
notify.show_toast("Notification",remMssg)