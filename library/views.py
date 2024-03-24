from django.shortcuts import render,HttpResponse,redirect,reverse
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


def User_index(request):
    userid = request.COOKIES.get('userid', 0)
    user = UserModel.objects.filter(id=userid).first()
    return render(request, 'User_index.html',{'user':user})
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname = request.POST.get('uname')
        if(UserModel.objects.filter(username=uname).exists()):
            return HttpResponse("用户名已存在，请返回页面重新注册！")
        passwd = request.POST.get('passwd')
        age = request.POST.get('age')
        UserModel.objects.create(username=uname,password=passwd,age=age)
        print(uname, passwd)
        return redirect(reverse('index'))


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = UserModel.objects.filter(username=uname,password=passwd)
        if user.exists():
            user = user.first()
            response = redirect(reverse('index'))
            # 设置cookie
            #         a.cookie存储在浏览器本地
            #         b.cookie不能跨域，不能跨浏览器
            #         c.cookie存储的内容是字符串，不能为中文，一般存储大小不要超过4KB
            #         d.cookie由后端创建，返回给前端保存
            # response.set_cookie('userid',user.id)
            # 设置过期时间
            response.set_cookie('userid',user.id,max_age=4*24*3600)
            return response
        else:
            return HttpResponse('用户名密码不匹配')

# 删除cookie（注销）
def logout(request):
    response = redirect(reverse('User_index'))
    # 删除cookie
    response.delete_cookie('userid')
    return response


