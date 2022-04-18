import threading, time, requests, json

def Sleep():
    time.sleep(10)
    print("Wake Up")

def TikTok():
    for i in range(5):
        print("Tik")
        time.sleep(1)
        print("Tok")
        time.sleep(1)

def Tokyo():
    response = requests.get("http://worldtimeapi.org/api/timezone/Asia/Tokyo")
    if response.status_code == 200:
        jsondata = json.loads(response.text)
        print("Tijd in Tokyo is " + jsondata["datetime"])
    else:
        print("Oeps, niet gelukt!")

def NogEens(start, end):
    for i in (start, end,1):
        print(i, end=" ")

print("START SINGLE THREADING")
#1 thread = synchroon
#Sleep()
#TikTok()
#Tokyo()
print("STOP SINGLE THREADING")
print("-------------------------")

thread_sleep = threading.Thread(target=Sleep)
thread_tiktok = threading.Thread(target=TikTok)
thread_tokyo = threading.Thread(target=Tokyo)

start = 0
end = 10

thread_vier = threading.Thread(target=NogEens, args=(start, end))
start = 10
end = 20
thread_vijf = threading.Thread(target=NogEens, args=(start, end))

# we hebben nu 6 threads!!! 5 die zijn opgestart & onze hoofd thread!!

print("START MULTI THREADING")
thread_sleep.start()
thread_tiktok.start()
thread_tokyo.start()
thread_vier.start()
thread_vijf.start()
print("STOP MULTI THREADING")