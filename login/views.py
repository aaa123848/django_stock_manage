from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from . import form

# Create your views here.


def index(request):
    return render(request,'login/index.html')  #尋找templates  連結到底下的login/index.html

def login(request):

    if request.session.get('is_login', None):
        return redirect('/base/')

    if request.method == 'POST':
        login_form = form.UserForm(request.POST)
        message = '請輸入完整用戶密碼'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
        
            try : 
                user = models.User.objects.get(name123 = username)
            except:
                message = '用戶不存在'
                return render(request, 'login/login.html', locals())
            
            if password == user.password:
                request.session['is_login'] = True
                request.session['user.id'] = user.id
                request.session['this_is_mother_fuck'] = user.name123
                request.session['is_admin'] = None
                print('before_is_admin')
                if user.name123 == 'admin01':
                    request.session['is_admin'] = user.name123
                    print('is_admin')
                return redirect('/base/')
            else :
                message = '密碼錯誤'
                return render(request, 'login/login.html', locals())
        else :#白打得 前端就擋下來了
            return render(request, 'login/login.html', locals())


    login_form = form.UserForm()
    return render(request,'login/login.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    else :
        request.session.flush()
        #或是 del request.session['is_login']


    return render(request,'login/index.html')