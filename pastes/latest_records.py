from typing import Type
from django.db import models
from django.contrib.auth.models import User

def get_latest_records_for_user(model: Type[models.Model], user: User, count: int):

    return model.objects.filter(user=user).order_by('-id')[:count]

def get_latest_records_for_global(model: Type[models.Model], count: int):

    return model.objects.filter(private=False, burn=False).order_by('-id')[:count]