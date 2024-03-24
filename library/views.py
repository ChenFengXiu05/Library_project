from django.shortcuts import render,HttpResponse
from library.models import *

def index(request):
    Books = Book.objects.all()
    return render(request,'index.html',{'Books':Books})


def book_detail(request,bid):
    book = Book.objects.get(pk=bid)
    # publishers = book.publishers
    return render(request, 'book_detail.html',{'book':book},
                  # {'publishers':publishers}
                  )

def publish_detail(request,pid):
    publisher = Publisher.objects.get(pk=pid)
    return render(request,'publisher_detail.html',{'publisher':publisher})

def Author_detail(request,aid):
    author = Author.objects.get(pk=aid)
    return render(request,'author_detail.html',{'author':author})


# master分支合并冲突演示

# 热修分支hot-fix演示

# push操作演示

# pull远程修改拉取操作演示
