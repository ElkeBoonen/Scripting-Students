# uitleg 
from itertools import count
from typing import final
from bs4 import BeautifulSoup
import requests
import threading

# Excercise 4: --> Collin
# Get the winner of ultratop singles top 50
# 1st place - 50 points
# 2th place - 49 points
# ..

def Functie(year):
    url = "https://www.ultratop.be/nl/ultratop50/" + str(year) + "/"
    request = requests.get(url)
    weeksBS= BeautifulSoup(request.text, "html.parser")
    dates = weeksBS.find("select", { "id" : "chartdate"}).find_all("option")

    weeks = []
    for week in dates:
        weeks.append(week.get("value"))

    scoreboard = {}

    for week in weeks:
        url = "https://www.ultratop.be/nl/ultratop50/" + str(year) + "/" + week
        print("Call naar", year, " --> week", week)
        request = requests.get(url)

        latestSongBS = BeautifulSoup(request.text, "html.parser")
        charts = latestSongBS.find_all("div", { "class" : "chart_title"})

        chartIndex = 0

        for chart in charts:
            artistName = chart.find("a").find("b").get_text()
            track = chart.find("a").get_text().replace(artistName, "")

            fulltrack = artistName + " - " + track

            if fulltrack in scoreboard.keys():
                scoreboard[fulltrack] = scoreboard[fulltrack] + (50 - chartIndex)
            else:
                scoreboard[fulltrack] = 50 - chartIndex

            chartIndex+=1

    winner = max(scoreboard, key=scoreboard.get)
    print("WINNER in jaar", year, "is",winner)

for i in range(2018,2022):
    thread = threading.Thread(target=Functie, args=(i,))
    thread.start()