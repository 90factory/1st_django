import schedule,time
# from selenium import webdriver
#
# driver = webdriver.Chrome('C:\\Users\\buggi\\Downloads\\chromedriver_win32\\chromedriver.exe')
# driver.close()

#a = {'번호': '402187', '분류': '인권/성평등', '제목': '포항 약국 칼부림 사건의 가해 남성을 제대로 처벌하라.', '링크': 'https://www1.president.go.kr/petitions/410261', '청원인': 'twitter - ***', '청원기간': '18.10.18 ~ 18.11.17', '참여인원': '197,343명'}+{'a' : '1'}
#print(a)

abc = {'a' : '1','b' : '2', 'c' : '3'}
del abc['a']
r = print(abc)

def job():
    print("i'm working......")
schedule.every(0).seconds.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
