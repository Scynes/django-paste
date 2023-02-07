from django.shortcuts import render
from django.views.generic import View

class PasteUploadView(View):
    
    def get(self, request):
        
        return render(request, 'paste_upload.html')
