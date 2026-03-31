import threading, time
import subprocess


def A():
    for i in range(0,10):
        print(i)

def B():
    for i in range(0,10):
        print("BEEP")
        time.sleep(1)
        subprocess.Popen(r"C:\WINDOWS\System32\calc.exe")

def C():
    time.sleep(3)
    print("opstaan!")

def D(variabele):
    for i in range(0,10):
        print(i, "thread in for-loop",variabele) 
        time.sleep(1)

print("start")
threadA = threading.Thread(target=A)
threadB = threading.Thread(target=B)
threadC = threading.Thread(target=C)
threadA.start()
threadB.start()
threadC.start()

# for i in range(0,5):
#    thread = threading.Thread(target=D(i))
#    thread.start()



print("stop")