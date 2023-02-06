from django.db import models
from django.contrib.auth.models import user

class Paste (models.Model):
    
    # Define the types of syntax
    TEXT_SYNTAX = 'TXT'
    JAVASCRIPT_SYNTAX = 'JS'
    HTML_SYNTAX = 'HTML'

    # Define the touple syntax
    SYNTAX_OPTIONS = [
        (TEXT_SYNTAX, 'Text'),
        (JAVASCRIPT_SYNTAX, 'JavaScript'),
        (HTML_SYNTAX, 'HTML')
    ]

    # Model fields
    title = models.CharField(max_length=255)
    syntax = models.CharField(max_length=4, choices=SYNTAX_OPTIONS, default=TEXT_SYNTAX)
    private = models.BooleanField(default=False)
    body = models.TextField()
    created_at = models.DateTimeField(auto_created=True)