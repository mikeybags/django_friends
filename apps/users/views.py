from django.shortcuts import render, redirect
import datetime
from django.contrib import messages
from models import *

# Create your views here.
def index(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == "POST":
        name = request.POST['name']
        alias = request.POST['alias']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        birthdate = request.POST['birthdate']
        errors = User.objects.validate(name, alias, password, password_confirm, email, birthdate)
        if errors:
            for e in errors:
                messages.add_message(request, e)
        else:
            user = User.objects.register(name, alias, password, email, birthdate)
            if 'errors' in user:
                messages.error(request, user['errors'][0])
            else:
                request.session['id'] = user['user'].id
                request.session['alias'] = user['user'].alias
                return redirect('friendships:home')
        return redirect('users:index')

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.authenticate(email, password)
        if 'errors' in user:
            messages.error(request, user['errors'][0])
        else:
            request.session['id'] = user['user'].id
            request.session['alias'] = user['user'].alias
            return redirect('friendships:home')
    return redirect('users:index')

def logout(request):
    request.session.clear()
    return redirect('users:index')







# eighteen_years_ago = datetime.date.today() - datetime.timedelta(weeks=totalweeks)
