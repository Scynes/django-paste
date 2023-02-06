from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Link (models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
