import time
while True:
    print("현재시간: "+time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)