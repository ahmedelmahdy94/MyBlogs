from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
    )
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import  *

# Create your views here.

def login_view(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        print(username)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/")
    return render(request, "login.html", {"form":form, "title": "LogIn"})



def signup_view(request):
    next = request.GET.get('next')
    form = UserSignupForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        email = form.cleaned_data.get('email')
        print(email)
        # send_mail(
        #     'Subject here',
        #     'Here is the message.',
        #     'from@example.com',
        #     [email],
        #     fail_silently=False,
        #     )
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/")
    #
    context = {
        "form": form,
        "title": "SignUp"
    }
    return render(request, "signup.html", context)

def logout_view(request):
    logout(request)
    return redirect("/")
