from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render
from django.views.generic import View

from .forms import PasteForm
from .models import Paste

from links.models import Link

# TODO I think that this should be a CBV for Link
# that way, it becomes modular and decoupled.
class PasteView(View):

    def get(self, request, id):

        # Query for finding a matching paste short_uuid -> id
        link_result = Link.objects.filter(short_uuid = id).first()

        # Check if the link_result exists
        if link_result:

            # Get the Paste object associated with the Link
            paste = link_result.content_object

            return HttpResponse(paste.body)

        else:

            return HttpResponse('No paste was found!')

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

        paste.save()

        # Save the link
        link = Link.create(ContentType.objects.get_for_model(Paste), paste.id)
        link.save()

        # Save the paste
        paste.link = link
        paste.save()

        return HttpResponse(paste)