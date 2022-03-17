import time

def format(a):
    return str(a).zfill(2)

def formatDecimal(a):
    return "{0:.2f}".format(a).zfill(4)

def returnTime(seconds):
    return f"{format(int(seconds%(24*60*60)/(60*60)))}:{format(int(seconds%(60*60)/60))}:{formatDecimal(seconds%60)}"

input()
began=time.time()
while True:
    print(returnTime(time.time()-began), end="\r")
    if msvcrt.kbhit():
	    if ord(msvcrt.getch()) == 10:
	        break
