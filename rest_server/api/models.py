from django.db import models
import Crawler
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#Create your models here.

# class CheongwadaeCrawler:
#
#     cheongwadae_list = []
#
#     for page in range(9,12):
#         driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
#         driver.get('https://www1.president.go.kr/petitions/category?c=0&only=2&page={}&order=2'.format(page))
#         soup = BeautifulSoup(driver.page_source, 'html.parser')
#         crawlingdata = Crawler.cheongwadae_crawling(soup)
#         cheongwadae_list.append(crawlingdata)
#
#     with open('crawling_data.json', 'w', encoding='utf-8') as file:  # json을 만들어준다
#         json.dump(cheongwadae_list, file, ensure_ascii=False, indent='\t')
