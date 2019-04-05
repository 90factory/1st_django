from __future__ import unicode_literals
from django.db import models
import json,pymongo,CrawlerModule
from datetime import datetime

#Create your models here.

# class Entiredata(models.Model):
#
#     number = models.CharField(max_length=10, null=True)#번호
#     category = models.CharField(max_length=10, null=True)#분류
#     title = models.CharField(max_length=50, null=True)#제목
#     link = models.CharField(max_length=30, null=True)#링크
#     name = models.CharField(max_length=15, null=True)#청원인
#     period = models.CharField(max_length=19, null=True)#청원기간
#     people = models.CharField(max_length=10, null=True)#참여인원
#
#     def __str__(self):
#         return self.name

class Model:

    conn = pymongo.MongoClient('127.0.0.1', 27017)
    db = conn.get_database('mydb')
    collection = db.get_collection('Crawler')

    number_of_data = collection.find().count()

    def insertinitialdata():
        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        with open('crawling_data.json','r',encoding='utf-8') as file:
            crawlerdata = json.load(file)

        num = 1
        for j in range(len(crawlerdata)):
            for k in range(len(crawlerdata[j])):
                crawlerdata[j][str(k+1)]['_id'] = num
                collection.insert(crawlerdata[j][str(k+1)])
                num += 1

    def updatedata():
        CrawlerModule.CrawlerModule.setpage(6,16)
        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        with open('crawling_data.json', 'r', encoding='utf-8') as file:
            crawlerdata = json.load(file)

        num = 1
        for j in range(len(crawlerdata)):
            for k in range(len(crawlerdata[j])):
                collection.update({'_id':num},{'$set': crawlerdata[j][str(k + 1)]})
                num += 1
        print('업데이트완료!','->',datetime.now().year,'년',datetime.now().month,'월',datetime.now().day,'일',' ',datetime.now().hour,'시',datetime.now().minute,'분',datetime.now().second,'초')

    def entirequery():

        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        entireresult = collection.find()
        entirelist = []

        for r in entireresult:
            del r['_id']
            entirelist.append(r)

        return entirelist

    def top5query():

        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        top5result = collection.find().limit(5)

        top5list = []

        for r in top5result:
            del r['_id']
            top5list.append(r)

        return top5list

    def keywordquery(keyword):

        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        keywordresult = collection.find({'제목':{'$regex': keyword}})

        keywordlist = []

        for r in keywordresult:
            del r['_id']
            keywordlist.append(r)

        return keywordlist

    def historyquery(history):

        conn = pymongo.MongoClient('127.0.0.1', 27017)
        db = conn.get_database('mydb')
        collection = db.get_collection('Crawler')

        historylist = []

        for i in range(len(history)):
            historyresult = collection.find({'링크': {'$regex': history[str(i)]}})
            for r in historyresult:
                del r['_id']
                historylist.append(r)

        return historylist

# class Enitredata(Document):
#     connect('mydb',host = '127.0.0.1', port = 27017)
#
#     number = StringField(required=True)
#     category = StringField(max_length=10)
#     title = StringField(max_length=50)
#     link = StringField(max_length=30)
#     name = StringField(max_length=15)
#     period = StringField(max_length=19)
#     people = StringField(max_length=10)


