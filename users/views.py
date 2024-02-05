from django.shortcuts import render , reverse

from django.contrib.auth import authenticate , login as auth_login , logout as auth_logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User

from users.forms import UserForm
from main.function import generate_form_errors


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(request, username=username , password=password)
            if user is not None:
                auth_login(request,user)

                return HttpResponseRedirect("/")
            
            else:
                context = {
                    "title" : "Login",
                    "error" : True,
                    "message" : "Invalid username or password"
                }
                return render(request, "users/login.html",context=context)

        else:
            context = {
                "title" : "Login",
                "error" : True,
                "message" : "Invalid username or password"
            }
            return render(request, "users/login.html",context=context)

    context={
        "title" : "Login"
    }
    return render(request, "users/login.html",context=context)


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse("EnglishDictionary:index"))


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            isinstance = form.save(commit=False)

            User.objects.create_user(
                username = isinstance.username,
                password = isinstance.password,
                email = isinstance.email,
                first_name = isinstance.first_name,
                last_name = isinstance.last_name,
            )

            user = authenticate(request, username = isinstance.username , password = isinstance.password)
            auth_login(request,user)

            return HttpResponseRedirect(reverse("EnglishDictionary:index"))
        else: 
            message = generate_form_errors(form)
            
            form = UserForm()
            context = {
                "title" : "Signup",
                "error" : True,
                "message" : message,
                "form" : form ,
            }
            return render(request, "users/signup.html",context=context)

    else:
        form = UserForm()
        context = {
            "title" : "signup" ,
            "form" : form ,
    }
    return render(request , "users/signup.html" , context=context)
