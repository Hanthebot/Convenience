import time
while True:
    print("Time now: "+time.strftime("%H:%M:%S"), end="\r")
    time.sleep(1)
