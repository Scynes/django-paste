from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.edit import CreateView

from .forms import RegisterForm

class Register(CreateView):

    def post(self, request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            login(request, authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1')))

            return redirect('upload')

    def get(self, request):

        return redirect('upload')
