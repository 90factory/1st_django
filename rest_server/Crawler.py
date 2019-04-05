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

            period = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_date light'}).text.strip('span 청원 종료일')

            people = li.find('div', {'class': 'bl_wrap'}).find('div', {'class': 'bl_agree cs'}).text.strip('span 참여인원')

            if int(people.replace(",", "").strip('명')) >= 200000:
                pass
            else:
                temp_dict[str(num)] = {'번호': number, '분류': category, '제목': title, '링크': chungwadaelink + link, '청원만료일': period, '참여인원': people}
                num += 1

        return temp_dict
#============================================================================================================================================================================================
    def makejson(cheongwadae_list):
        with open('crawling_data.json', 'w', encoding='utf-8') as file:  # json을 만들어준다
            json.dump(cheongwadae_list, file, ensure_ascii=False, indent='\t')

