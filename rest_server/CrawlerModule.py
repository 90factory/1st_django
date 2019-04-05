import Crawler
from bs4 import BeautifulSoup
from selenium import webdriver

class CrawlerModule:

    def setpage(startpage,endpage):

        cheongwadae_list = []

        for page in range(startpage, endpage):
            driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
            driver.get('https://www1.president.go.kr/petitions/category?c=0&only=2&page={}&order=2'.format(page))
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            crawlingdata = Crawler.Crawler.cheongwadae_crawling(soup)
            cheongwadae_list.append(crawlingdata)
            driver.close()

        Crawler.Crawler.makejson(cheongwadae_list)

