from bs4 import BeautifulSoup
from selenium import webdriver
import json

class Crawler:

    def cheongwadae_crawling(html):
        temp_dict = {}
        chungwadaelink = 'https://www1.president.go.kr'
        num = 1

        li_list =html.select('div.ct_list1 > div.board.text > div.b_list.category > div.bl_body > ul > li ')

        for li in li_list:

            number = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_no'}).text.strip('span 번호')

            category = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_category'}).text.strip('span 분류')

            title = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_subject'}).text.strip('span 제목')

            link = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_subject'}).find('a', {'class' : 'cb relpy_w'}).get('href')

            name = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_name'}).text.strip('span 청원인')

            period = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_date light'}).text.strip('span 청원기간')

            people = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_agree cs'}).text.strip('span 참여인원')

            temp_dict[str(num)] = {'번호' : number, '분류' : category, '제목' : title, '링크' : chungwadaelink+link, '청원인' : name, '청원기간' : period, '참여인원' : people}
            if int(people.replace(",", "").strip('명')) >= 200000:
                del temp_dict[str(num)]
            num += 1

        return temp_dict
#============================================================================================================================================================================================
    def makejson(cheongwadae_list):
        with open('crawling_data.json', 'w', encoding='utf-8') as file:  # json을 만들어준다
            json.dump(cheongwadae_list, file, ensure_ascii=False, indent='\t')
#==============================================================================  Main  ======================================================================================================
    startpage = 9
    endpage = 11
    cheongwadae_list = []

    for page in range(startpage,endpage):
        driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
        driver.get('https://www1.president.go.kr/petitions/category?c=0&only=2&page={}&order=2'.format(page))
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        crawlingdata = cheongwadae_crawling(soup)
        cheongwadae_list.append(crawlingdata)

    makejson(cheongwadae_list)
