import time
while True:
    print("한국시간: "+str((int(time.strftime("%H"))+2)%24)+time.strftime(":%M:%S"), end="\r")
    time.sleep(1)