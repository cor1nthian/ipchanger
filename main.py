import time
from stem.control import Controller
from stem import Signal

def change_ip():
    with Controller.from_port(port=9051) as controller:
        controller. authenticate()
        controller.signal(Signal .NEWNYM)

interval = 60
count = 0
i=0

while count == 0 or i < count:
    change_ip()
    print(f"IP changed {interval} cex.")
    time.sleep(interval)
    i += 1