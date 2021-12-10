from bs4 import BeautifulSoup
import colorama
import requests
from colorama import Fore, Style
import webbrowser
import vlc
from selenium import webdriver
import time

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

b=webdriver.Firefox(executable_path="./geckodriver")
b.get(soup.find("iframe")["src"])

time.sleep(6)

b.get(BeautifulSoup(b.page_source, "html.parser").find("video")["src"])

print(Fore.MAGENTA+"\nGood Movie! ;)\n")

#webbrowser.open_new(soup.find("iframe")["src"])


# # creating vlc media player object
# media = vlc.MediaPlayer(str(soup.find("iframe")["src"]))

# # start playing video
# media.play()

# while True:
#     pass
