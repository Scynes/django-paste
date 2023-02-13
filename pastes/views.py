from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import render, redirect
from django.views.generic import View
from . import latest_records

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

            if paste.private == True and paste.user != request.user:

                return render(request, 'error_page.html', { 'error': 'You do not have permission to view this paste! Please login.' })

            syntax = Paste.get_syntax_value(paste.syntax)
            context = { 'paste': paste, 'syntax': syntax }

            if request.user.is_authenticated:
                context['recent_pastes'] = latest_records.get_latest_records_for_user(Paste, request.user, 10)

            if paste.user == request.user:
                context['owner'] = paste.user.id

            # Make sure that a redirect doesn't trigger burning...
            if 'HTTP_REFERER' not in request.META and paste.burn == True:
                paste.delete()
            
            return render(request, 'paste_details.html', context)

        else:

            return render(request, 'error_page.html', { 'error': 'Oops! Paste does not exist.' })

    def delete(self, request, id):
        
        record = Paste.objects.filter(pk=id).first()

        if record:

            if record.user != request.user:

                return JsonResponse({'message': 'Unauthorized. You do not have permissions to delete this paste!'}, status=401)

            record.delete()

            return JsonResponse({'message': 'Successfully deleted! The paste will no longer be viewable if you refresh this page.'}, status=202)

        else:   
        
            return JsonResponse({'message': 'Oops! The paste was not located.'}, status=404)

class PasteUploadView(View):
    
    def get(self, request):

        context = { 'form': PasteForm() }

        if request.user.is_authenticated:
            context['recent_pastes'] = latest_records.get_latest_records_for_user(Paste, request.user, 10)
        
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

        if request.user.is_authenticated:
            paste.user = request.user

        # Save the paste
        paste.link = link
        paste.save()

        return redirect(f'/{link.short_uuid}')