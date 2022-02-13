from bs4 import BeautifulSoup
import urllib.request
import sys
import os
import os.path
from os import path
import re
from datetime import datetime, timedelta
yesterday = datetime.now() - timedelta(1)
date = yesterday.strftime("%Y-%m-%d")
date4search = yesterday.strftime("%d.%m.%Y")
temp = input("Date ("+date+"): ")
if re.match("\d\d\d\d-\d\d-\d\d",temp):
	date = temp
	date4search = date.split("-")[2]+"."+date.split("-")[1]+"."+date.split("-")[0]
print(date)
print(date4search)
if input("Countinue? (yes/no): ") != "yes":
		sys.exit()

os.chdir("Nachrichten")
if not os.path.exists(date):
	os.makedirs(date)
os.chdir(date)
for uhr in range(0,24):
	time = f"{uhr:02d}"
	print(time)
	if not os.path.exists(time):
		os.makedirs(time)
	os.chdir(time)
	count = 0
	html_page = urllib.request.urlopen("https://www.deutschlandfunk.de/die-nachrichten-nachlesen.1794.de.html?drn:date="+date+"&drn:time="+time+":00#date-"+date)
	#https://www.deutschlandfunk.de/nachrichten/nachlesen
	soup = BeautifulSoup(html_page, "html.parser")
	for link in soup.findAll('h2', string=re.compile(".+"+date4search)):
		for sibling in link.find_next_siblings("ul"):
			for href in sibling.findAll('a'):
				count += 1
				os.system("wget -O "+href.get("href").split("=")[-1]+"_"+href.get("href").split("?")[0]+" https://www.deutschlandfunk.de/"+href.get("href"))
				#urllib.request.urlretrieve("https://www.deutschlandfunk.de/"+href.get("href"), href.get("href").split("=")[-1]+"_"+href.get("href").split("?")[0])
				print("HTML downloaded:",count)
	os.chdir("..")
os.chdir("../..")

# if not os.path.exists("nachhören"):
# 	os.makedirs("nachhören")
# os.chdir("nachhören")
# if not os.path.exists(date):
# 	os.makedirs(date)
# os.chdir(date)
# count = 0
# if path.exists(date+".list"):
# 	if input("List already exists. countinue? (yes/no): ") != "yes":
# 		sys.exit()

# with open(date+".list","w") as f:
# 	f.write("data-audio-src\tdata-audio-duration\tdata-audio-size\n")
# 	for page in range(1,11):
# 		html_mp3 = urllib.request.urlopen("https://www.deutschlandfunk.de/dlf-audio-archiv.2386.de.html?drau:broadcast_id=169&drau:from=&drau:searchterm=&drau:submit=1&drau:to=&drau:page="+str(page))
# 		soup = BeautifulSoup(html_mp3, "html.parser")
# 		for link in soup.find_all(attrs={"data-audio-delivery-mode": "download"}):
# 			tag = link.get("data-audio-src").split("/")[-4:-1]
# 			if '-'.join(tag) == date:
# 				count += 1
# 				f.write(link.get("data-audio-src")+"\t"+link.get("data-audio-duration")+"\t"+link.get("data-audio-size")+"\n")
# 				os.system("wget "+link.get("data-audio-src"))
# 				print("MP3 downloaded:",count)
# os.chdir("..")