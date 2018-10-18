from django.contrib import admin
from django.conf.urls import url
from . import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^addbook$',views.addbook,name="addbook"),
    url(r'^addbook/result/', views.indexresult, name="indexresult"),
    url(r'^search$',views.search,name="search"),
    url(r'^search/result/',views.searchresult,name="searchResult"),
    url(r'^(\d{1,4})', views.theBook, name="theBook"),
    url(r'^book/result/', views.theBookResult, name="search"),
    url(r'^keepers/$',views.keepersList,name='keepers'),
    url(r'^keepers/(\d{1,5})', views.keeperPage, name='keepersPage'),
    url(r'^keepers/keeperPageResult', views.keeperPageResult, name='keepersPageResult'),

]