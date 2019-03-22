from django.conf.urls import url
from . import views

urlpatterns = [
    url('entire',views.Controller.entirecontroller),
    url('top5',views.Controller.top5controller),
    url('keyword',views.Controller.keywordcontroller),
    url('history',views.Controller.historycontroller),
]
