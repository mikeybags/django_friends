from __future__ import unicode_literals
from django.db import models
from django.db import IntegrityError
import bcrypt
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[A-Za-z]+$')

class UserManager(models.Manager):
    def validate(self, name, alias, password, password_confirm, email, birthdate):
        errors = []
        if len(name) < 3:
            errors.append("Name must be longer than 2 characters.")
        elif not NAME_REGEX.match(name):
           errors.append("Your name must only contain characters.")
        if len(alias) < 2:
            errors.append("Your Alias must be at least 2 characters.")
        if len(password) < 8:
            errors.append("Password must be at least 8 characters long.")
        if password_confirm != password:
            errors.append("Passwords do not match. Please re-enter your password.")
        if not EMAIL_REGEX.match(email):
            errors.append("Please enter a valid email address.")
        return errors

    def register(self, name, alias, password, email, birthdate):
        errors = []
        try:
            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.objects.create(name=name, alias=alias, password_hash=hashed, email=email, birthday=birthdate)
        except IntegrityError:
            errors.append("That email is already taken.")
            return {'errors': errors}
        return {'user': user}

    def authenticate(self, email, password):
        errors = []
        try:
            user = User.objects.get(email=email)
        except:
            errors.append("Email not found, please register.")
            return {'errors': errors}
        if bcrypt.hashpw(password.encode(), user.password_hash.encode()) == user.password_hash:
            return {'user': user}
        else:
            errors.append("Incorrect password. Please re-enter your password.")
            return {'errors': errors}

class User(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=25)
    password_hash = models.CharField(max_length=256)
    email = models.CharField(max_length=50, unique=True)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
