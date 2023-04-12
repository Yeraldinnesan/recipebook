from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:  # if not found in the db
            auth.login(request, user)

            return redirect('home')
        else:

            return redirect('login')

    else:
        return render(request, 'login.html')


def register(request):
    if request.method == 'POST':

        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(username=username).exists():

                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():

                    return redirect('register')
                else:
                    user = User.objects.create_user(
                        username=username, password=password, email=email,)
                    user.save()
                    auth.login(request, user)

                    return redirect('home')
        else:

            return redirect('register')
    else:
        return render(request, 'register.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)

    return redirect('home')
