from django.db import models

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from .short_uid import generate

class Link (models.Model):

    # Model fields
    short_uuid = models.CharField(max_length=8)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_at = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def create(content_type, object_id):
        
        new_link = Link(short_uuid = generate(), content_type = content_type, object_id = object_id)

        return new_link
