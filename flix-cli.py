from bs4 import BeautifulSoup
import requests
from colorama import Fore, Style, Back
from selenium import webdriver
import time
# import vlc

q=input("\nEnter the movie name: ")

s=requests.Session()

url=f"https://superflixhd.net/list/filmes?s={q}"

r=s.get(url)

soup=BeautifulSoup(r.text, "html.parser")

Tags=soup.find_all("div", {"class": "item"})


movies=[]
for Tag in Tags:
    movies.append({
        "url": "https://superflixhd.net"+Tag.a["href"],
        "name": Tag.h2.text,
        "year": Tag.find("div", {"class": "fixyear"}).span.text
    })

print("\n")
count=0
for movie in movies:
    count+=1
    print(Style.BRIGHT+Fore.GREEN+f"[{count}] " + Fore.WHITE+f"{movie['name']} - {movie['year']}")

try:
    c=int(input("\nWhat number: "))-1
    movie=movies[c]
    print(Fore.GREEN+f"\nSELECTED {movie['name']}")
except:
    print("\nPlease select a valid option *")
    exit()

r=s.get(movie["url"])
soup=BeautifulSoup(r.text, "html.parser")

s=webdriver.firefox.service.Service("./geckodriver")
b=webdriver.Firefox(service=s)
b.get(soup.find("iframe")["src"])

time.sleep(5)

movieURL=BeautifulSoup(b.page_source, "html.parser").find("video")["src"]

b.get(movieURL)

b.fullscreen_window()

print(Fore.MAGENTA+"\nGood Movie! ;)\n")

# b.close()

# Instance = vlc.Instance()
# player = Instance.media_player_new()
# Media = Instance.media_new(movieURL)
# Media.get_mrl()
# player.set_media(Media)
# player.play()

# print(Fore.LIGHTYELLOW_EX+f"\nDownload URL: {movieURL}\n")
# print("\n"+str(player.get_length()/1000)+" Seconds")

# while True:
#     try:
#         command=input(">> ")
#         if command == "pause":
#             player.pause()
#             print(str(player.get_time()/1000)+" - "+str(player.get_length()/1000))
#         elif command == "play":
#             player.play()
#             print(str(player.get_time()/1000)+" - "+str(player.get_length()/1000))
#         elif command.split()[0] == "time":
#             player.set_time(int(command.split()[1])*1000)
#             print(str(player.get_time()/1000)+" - "+str(player.get_length()/1000))
#         elif command == "quit":
#             break
#     except:
#         pass


# print(Fore.CYAN+"\nBye!")