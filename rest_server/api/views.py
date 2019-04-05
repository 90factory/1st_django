from django.http import HttpResponse
from . import models
import json,schedule,time,CrawlerModule
from apscheduler.schedulers.background import BackgroundScheduler
# Create your views here.

class Controller:
    if models.Model.number_of_data == 0:
        CrawlerModule.CrawlerModule.setpage(6,16)
        models.Model.insertinitialdata()
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(models.Model.updatedata,'cron',hour = 00,minute =00,second=00)

    def entirecontroller(request):


        entiredata = models.Model.entirequery()

        return HttpResponse(json.dumps(entiredata), content_type='application/json')

    def top5controller(request):
        top5data = models.Model.top5query()

        return HttpResponse(json.dumps(top5data), content_type='application/json')

    def keywordcontroller(request):
        protocalquerystringkeyword = request.GET.get('keyward')
        #protocalquerystringkeyword = '다'

        if protocalquerystringkeyword == None:
            keyworddata = '404 Not Found'
        else:
            keyworddata = models.Model.keywordquery(protocalquerystringkeyword)

        return HttpResponse(json.dumps(keyworddata), content_type='application/json')

    def historycontroller(request):
        protocalquerydicthistory = request.GET.dict()
        #protocalquerydicthistory = {'0': '407079', '1': '314212', '2': '443174', '3': '347470', '4': '410261'}
        if len(protocalquerydicthistory) == 0:
            historydata = '404 Not Found'
        else:
            historydata = models.Model.historyquery(protocalquerydicthistory)

        return HttpResponse(json.dumps(historydata), content_type='application/json')

