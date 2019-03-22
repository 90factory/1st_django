from bs4 import BeautifulSoup
from selenium import webdriver

def cheongwadkeyword_Crawling(html,word):
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

    keylist = []
    valuelist = []
    finaldict = {}
    for key, value in temp_dict.items():
        keylist.append(key)
        valuelist.append(value)

    number = 1
    for i in range(0,len(valuelist)):
        if word in valuelist[i]['제목']:
            finaldict[str(number)] = valuelist[i]
            number += 1
    return finaldict
#====================================================================================================================================================================================================================================
cheongwadae_list = []

for page in range(9,11):
    driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
    driver.get('https://www1.president.go.kr/petitions/category?c=0&only=2&page={}&order=2'.format(page))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    #cheongwadkeyword_Crawling(soup,word='포항')
    print(cheongwadkeyword_Crawling(soup,word='다'))
    #cheongwadae_list.append(cheongwadkeyword_Crawling(soup))

