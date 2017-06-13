from django.shortcuts import render, redirect
from models import *
# Create your views here.

def index(request):
    if "id" not in request.session:
        return redirect("users:index")
    user_id = request.session['id']
    alias = request.session['alias']
    non_friends = User.objects.exclude(id=user_id).exclude(users_friend__friend=user_id).exclude(friends_friend__user=user_id)
    friends = Friend.objects.filter(user=user_id) | Friend.objects.filter(friend=user_id)
    context = {
        'user_id': user_id,
        'alias': alias,
        'non_friends': non_friends,
        'friends': friends
    }
    return render(request, "friendships/home.html", context)

def add(request, friend_id):
    user_id = request.session['id']
    user = User.objects.get(id = user_id)
    friend = User.objects.get(id = friend_id)
    Friend.objects.create(user=user, friend=friend)
    # users = Friend.objects.create_friendship(user_id, friend_id)
    return redirect('friendships:home')

def view(request, user_id):
    user= User.objects.get(id=user_id)
    context = {
    "user":user
    }
    return render(request, "friendships/view.html", context)

def delete(request, friendship_id):
    Friend.objects.get(id=friendship_id).delete()
    return redirect("friendships:home")
