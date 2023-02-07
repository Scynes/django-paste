from django.shortcuts import render
from django.views.generic import View

from .forms import PasteForm

class PasteUploadView(View):
    
    def get(self, request):

        context = { 'form': PasteForm() }
        
        return render(request, 'paste_upload.html', context)


