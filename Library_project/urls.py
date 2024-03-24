from django.contrib import admin
from django.urls import path

from library.views import *

urlpatterns = [
    path("index/",index,name = 'index'),
    path("pdetail/<int:pid>/",publish_detail,name='pdetail'),
    path("BookDetail/<int:bid>/",book_detail,name = 'BookDetail'),
    path("AuthorDetail/<int:aid>/",Author_detail,name = 'AuthorDetail'),
    path("admin/", admin.site.urls),
]
