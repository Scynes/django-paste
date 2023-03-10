from django.db import models
from django.contrib.auth.models import User

from links.models import Link

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    syntax = models.CharField(max_length=4, choices=SYNTAX_OPTIONS, default=TEXT_SYNTAX, verbose_name='Highlight')
    private = models.BooleanField(default=False)
    burn = models.BooleanField(default=False)
    body = models.TextField(verbose_name='Paste')
    link = models.OneToOneField(Link, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_syntax_value(syntax):

        for element in Paste.SYNTAX_OPTIONS:

            if syntax in element:
                
                return element[1].lower()

    def delete(self, *args, **kwargs):

        self.link.delete()
        super().delete(*args, **kwargs)