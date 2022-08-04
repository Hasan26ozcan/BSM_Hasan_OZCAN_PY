from email import message
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth,messages
def login(request):
    if request.method =="POST":
        username=request.POST["username"]
        password=request.POST["password"]

        user= auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request=request,user=user)
            messages.add_message(request,messages.SUCCESS,"oturum açıldı")
            return redirect("index")
        else:
            messages.add_message(request,messages.WARNING,"kullanıcı adı ya da parola yanlış")
            return redirect("login")
    else:
        return render(request,"users/login.html")
def register(request):
    if request.method =="POST":
        messages.add_message(request,messages.ERROR,"HATALI USERNAME YA DA PAROLA")
        username=request.POST["username"]
        email=request.POST["email"]
        password=request.POST["password"]
        repassword=request.POST["repassword"]

        if(password==repassword):
            if(User.objects.filter(username=username)).exists():
                messages.add_message(request,messages.WARNING,"bu kullanıcı adı daha önce alınmış")
        else:
            if(User.objects.filter(email=email)).exists():
                messages.add_message(request,messages.WARNING,"bu email adı daha önce alınmış")
                return redirect("register")
            else:
                user=User.objects.create_user(username=username,password=password,email=email,repassword=repassword)
                # herşey güzel be yolunda
                user.save()
                messages.add_message(request,messages.SUCCESS,"hesabınız oluşturuldu")

                return redirect("login")
    else:
        return render(request,"users/register.html")
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.add_message(request,messages.SUCCESS,"OTURUMUNUZ KAPATILMIŞ")
        return redirect("index")