from django.conf.urls import url
from . import views
app_name = "main"
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^logout$', views.logout, name="logout"),
    url(r'^addCatPage$', views.addCatPage, name="addCatPage"),
    url(r'^add$', views.addCat, name="add"),
    url(r'^like/(?P<cat_id>\d+)$', views.addLike, name="like"),
    url(r'^catInfo/(?P<cat_id>\d+)$', views.catInfo, name="catInfo"),
    url(r'^delete(?P<cat_id>\d+)$', views.Delete, name="delete"),
    url(r'^updatePage/(?P<cat_id>\d+)$', views.updatePage, name="updatePage"),
    url(r'^updateInfo/(?P<cat_id>\d+)$', views.updateInfo, name="updateInfo"),
]