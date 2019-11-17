import time
a=time.time()

def ii(a):
    return str(a).zfill(2)

def i(a):
    return "{0:.2f}".format(a).zfill(4)

def returntime(b):
    return f"{ii(int(b%86400/3600))}:{ii(int(b%3600/60))}:{i(b%60)}"

while True:
    print(returntime(time.time()-a), end="\r")