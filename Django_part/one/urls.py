__author__ = 'например Андрей'
from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.index, name='index'),
    url(r'^$', views.index_view.as_view(), name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^predictions/about/$', views.about, name='about_from_predict'),
    url(r'^predict_search/$', views.predict_search, name='predictS'),#Перерделать, по возможности, на более гибкую ссылку
    url(r'^test/$', views.test, name='test'),
    url(r'^predictions/$', views.predict_view.as_view(), name='predict'),
    url(r'^strategy/$', views.strategy, name='strategy'),
    url(r'^variants/$', views.variants, name='variants'),
    #url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
