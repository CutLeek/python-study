#亲测可以成功，或许可以开发出更多的功能

from win10toast import ToastNotifier
import time
toaster = ToastNotifier()

header = input("What You Want Me To Remember\n")
text = input("Releated Message\n")
time_min=float(input("In how many minutes?\n"))

time_min = time_min * 60
print("Setting up reminder..")
time.sleep(2)
print("all set!")
time.sleep(time_min)
toaster.show_toast(f"{header}", f"{text}", duration=10, threaded=True)
while toaster.notification_active(): time.sleep(0.005)