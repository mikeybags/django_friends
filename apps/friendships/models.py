from __future__ import unicode_literals
from django.db import models
from ..users.models import User
# Create your models here.

class FriendManager(models.Manager):
    def create_friendship(self, user_id, friend_id):
        user = User.objects.get(user_id = user_id)
        friend = User.objects.get(user_id = friend_id)
        pass

class Friend(models.Model):
    user = models.ForeignKey(User, related_name="users_friend")
    friend = models.ForeignKey(User, related_name="friends_friend")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = FriendManager()
