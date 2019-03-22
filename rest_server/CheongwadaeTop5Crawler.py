def cheongwadaetop5_crawling(html):
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

        if len(temp_dict) == 5:
            break

    return temp_dict
