from django.http import HttpResponse
from . import models
import json, Crawler
# Create your views here.
class Controller:

    def entirecontroller(request):

        with open('crawling_data.json', 'r', encoding='utf-8') as file: # json을 읽어준다(수정) <- 전체를 가져와서 전체를 줌으로 수정할 필요가없다.
            crawlerdata = json.load(file)

        return HttpResponse(json.dumps(crawlerdata), content_type='application/json')


    def top5controller(request):

        with open('crawling_data.json', 'r', encoding='utf-8') as file:  # json을 읽어준다(수정) <- 전체를 가져와서 top5 자료만 가져오도록 수정한다.
            crawlerdata = json.load(file)

        top5list = []
        top5dict = {}
        i = 0

        for key,value in crawlerdata[i].items():
            top5dict[key] = value
            if len(top5dict) == 5:
                break
        top5list.append(top5dict)

        return HttpResponse(json.dumps(top5list), content_type='application/json')


    def keywordcontroller(request):

         with open('crawling_data.json', 'r', encoding='utf-8') as file:  # json을 읽어준다(수정) <- 전체를 가져와서 request에서 요청하는 키워드에 일치하는 자료만 가져오도록 수정한다.
             crawlerdata = json.load(file)

         keyword_dict = {}
         newnum = 1
         i = 0
         #protocalquerystringkeyword = '다'
         protocalquerystringkeyword = request.GET.get('keyward')
         print(protocalquerystringkeyword)

         while i < Crawler.Crawler.endpage - Crawler.Crawler.startpage:
             for key,value in crawlerdata[i].items():
                 if protocalquerystringkeyword in value['제목']:
                     keyword_dict[str(newnum)] = value
                     newnum += 1
             i += 1

         keyworddata = keyword_dict

         return HttpResponse(json.dumps(keyworddata), content_type='application/json')

    def historycontroller(request):

        with open('crawling_data.json', 'r', encoding='utf-8') as file:  # json을 읽어준다(수정) <- 전체를 가져와서 request에서 요청하는 히스토리에 일치하는 자료만 가져오도록 수정한다.
            crawlerdata = json.load(file)

        protocalquerystringhistory = request.GET
        #protocalquerystringhistory ={'0': ['214435'], '1': ['314212'], '2': ['19313'], '3': ['531647'], '4': ['294032']}
        print(protocalquerystringhistory)

        temp_list = []

        for i in range(len(protocalquerystringhistory)):
            temp_list.append(protocalquerystringhistory.get(str(i)))
        print(temp_list)
        #historylist = [y for x in temp_list for y in x]
        #print(historylist)

        temp_dict = {}
        newnum = 1

        i = 0
        while i < Crawler.Crawler.endpage - Crawler.Crawler.startpage:
            for key,value in crawlerdata[i].items():
                for j in range(len(protocalquerystringhistory)):
                    if temp_list[j] in value['링크'][39:]:
                        temp_dict[str(newnum)] = value
                        newnum += 1
            i += 1

        history_dict = {}

        for key,value in temp_dict.items():
            for k in range(len(temp_list)):
                if temp_list[k] == value['링크'][39:]:

                    history_dict[str(k+1)] = value


        changeindex = sorted(history_dict.items())

        for l in range(len(changeindex)):
            history_dict[str(changeindex[l][0])] = changeindex[l][1]

        historydata = history_dict
        print(historydata)

        #try:
        return HttpResponse(json.dumps(historydata), content_type='application/json')
        #except PendingDeprecationWarning:
            #return HttpResponse('404 Not Found', content_type='applecation/json')
