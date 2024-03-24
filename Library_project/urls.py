from django.contrib import admin
from django.urls import path

from library.views import *

urlpatterns = [
    path("index/",index,name = 'index'),
    path("pdetail/<int:pid>/",publish_detail,name='pdetail'),
    path("BookDetail/<int:bid>/",book_detail,name='BookDetail'),
    path("AuthorDetail/<int:aid>/",Author_detail,name='AuthorDetail'),
    path("register/", register, name='register'),
    path("User_index/", User_index, name='User_index'),
    path("login/", login, name='login'),
    path("logout/", logout, name='logout'),

    path("admin/", admin.site.urls),
]
