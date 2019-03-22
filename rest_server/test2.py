from bs4 import BeautifulSoup
from selenium import webdriver
import json

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

def toJson(temp_data):
    with open('crawling_data_test.json', 'w', encoding='utf-8') as file:

        return json.dump(temp_data, file, ensure_ascii=False, indent='\t')

def toJson2(temp_data):
    with open('crawling_data_test.json', 'r', encoding='utf-8') as file:
        root = json.load(file)

    return print(root)
#==============================================================================================================================================================

crawling_list = []

for page in range(9,10):

    driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver.get('https://www1.president.go.kr/petitions/category?c=0&only=2&page={}&order=2'.format(page))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    crawling_dict = cheongwadae_crawling(soup)
    print(crawling_dict)
    crawling_list.append(crawling_dict)

toJson(temp_data=crawling_list)
toJson2(temp_data=crawling_list)