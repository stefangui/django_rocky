from django.conf.urls import url
from movie_search import views

app_name = 'movie_search'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^search_result/$', views.search_result, name='search_result'),
    url(r'^ajax_list/$', views.ajax_list, name='ajax-list'),
    url(r'^ajax_dict/$', views.ajax_dict, name='ajax-dict'),
    url(r'^ajax_test/$', views.ajax_test, name='ajax_test'),
    url(r'^home_page/$', views.search_result.as_view(), name='home_page'),
]