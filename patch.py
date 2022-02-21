from bs4 import BeautifulSoup
import urllib.request
import sys
import os
import os.path
from os import path
import re
from datetime import datetime, timedelta

hours = ["16","17","18","19","20","21","22","23"]#"00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15",
for hour in hours:
	tag = ["2022-02-15","2022-02-16","2022-02-17","2022-02-18","2022-02-19","2022-02-20","2022-02-21"]
	page = open("urls/"+hour+".html")
	soup = BeautifulSoup(page.read(), "html.parser")
	for t in tag:
		os.chdir("Nachrichten")
		if not os.path.exists(t):
			os.makedirs(t)
		os.chdir(t)
		if not os.path.exists(hour):
			os.makedirs(hour)
		os.chdir(hour)
		uptoday_list = soup.find(attrs={"data-day-identifier": t})
		for news in uptoday_list.find_all('li'):
			news_link = news.find('a')['href']
			html_page = urllib.request.urlopen(news_link)
			print(news_link)
			os.system("wget -O "+news_link.split("/")[-1]+" "+news_link)
		os.chdir("..")
		os.chdir("../..")
