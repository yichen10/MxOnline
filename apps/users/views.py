from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.views.generic import View
from django.db.models import Q
#生成密码;
from django.contrib.auth.hashers import make_password

from .models import UserProfile
from .forms import RegisterForm


# Create your views here.
# 自定义的登录
class CustoBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(username=username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 通过类实现登录
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        user_name = request.POST.get("user_name", "")
        pass_word = request.POST.get("user_name", "")
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {"msg": "用户名或密码错误"})


# 注册：
class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form':register_form})
    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get("username","")
            password = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            user_profile.password = make_password(password)
            user_profile.save()





def user_login(request):
    if request.POST == 'POST':
        user_name = request.POST.get("user_name", "")
        pass_word = request.POST.get("user_name", "")
        user = authenticate(user_name, pass_word)
        if user is not None:
            login(request, user)
    elif request.POST == 'GET':
        return render(request, 'login.html', {})
