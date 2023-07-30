from django.shortcuts import render,redirect
from user.form import RegisterForm,LoginForm
from django.contrib.auth.models import  User
from django.contrib.auth import   authenticate , login , logout
# Create your views here.
def register_view(request):
    if request.method == 'GET':
        context_data = {'form': RegisterForm}
        return render(request, 'user/register.html', context=context_data)
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('password1')== form.cleaned_data.get('password2'):
                user = User.objects.create_user(
                    username= form.cleaned_data.get('username'),
                    password= form.cleaned_data.get('password1')
                )
                return redirect('/user/login/')
            else:
                form.add_error('password1', "Пароль указан неправильно укажите верный пароль")
        return render(request, 'user/register.html',context={ 'form': form})


def login_view(request):
    if request.method == 'GET':
        context_data = {'form': login_view}
        return render(request,'user/login.html',context=context_data)
    if request.method == 'POST':
        form = LoginForm(data =request.POST)
        if form.is_valid():
            user = authenticate(username= form.cleaned_data.get('username'),
                    password= form.cleaned_data.get('password'))
            if user :
               login(request=request , user=user)
               return redirect('/shops/')
            else :
                form.add_error('username','try again')

        return render(request, 'user/login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('/shops/')
