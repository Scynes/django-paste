from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import View

from .forms import PasteForm

class PasteUploadView(View):
    
    def get(self, request):

        context = { 'form': PasteForm() }
        
        return render(request, 'paste_upload.html', context)

    def post(self, request):
        
        form_data = PasteForm(request.POST)

        if not form_data.is_valid():
            return HttpResponse('Not valid hoe')

        # Validation good, let's get a record going
        paste = form_data.save(commit=False)

        # Check if there's a user associated
        if isinstance(request.user, User):
            
            paste.user = request.user

        # Save the paste
        paste.save()
        
        return HttpResponse(paste)


