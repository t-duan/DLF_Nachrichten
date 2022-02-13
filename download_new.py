from bs4 import BeautifulSoup
import urllib.request
import sys
import os
import os.path
from os import path
import re
from datetime import datetime, timedelta

while True:
	today = datetime.now()
	date = today.strftime("%Y-%m-%d")
	hour = today.strftime("%H")
	minute = today.strftime("%M")
	second = today.strftime("%S")
	#print(today.strftime("%Y-%m-%d %H-%M-%S"))
		
	if minute == "53" and second == "00": 
		print(today.strftime("%Y-%m-%d %H:%M:%S"))
		
		os.chdir("Nachrichten")
		if not os.path.exists(date):
			os.makedirs(date)
		os.chdir(date)
		if not os.path.exists(hour):
			os.makedirs(hour)
		os.chdir(hour)
		count = 0
		html_page = urllib.request.urlopen("https://www.deutschlandfunk.de/nachrichten/nachlesen")
		soup = BeautifulSoup(html_page, "html.parser")
		uptoday_list = soup.find(attrs={"data-day-identifier" : date})
		for news in uptoday_list.find_all('li'):
			news_link = news.find('a')['href']
			html_page = urllib.request.urlopen(news_link)
			print(news_link)
			count += 1
			os.system("wget -O "+news_link.split("/")[-1]+" "+news_link)
			print("HTML downloaded:",count)
		os.chdir("..")
		os.chdir("../..")


