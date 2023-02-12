from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.views.generic.edit import View
from django.contrib.auth.forms import AuthenticationForm

from .forms import RegisterForm

class Register(View):

    def post(self, request):

        form = RegisterForm(request.POST)

        if form.is_valid():

            form.save()

            login(request, authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password1')))

            return redirect('upload')
        
        else:

            return redirect('upload')

    def get(self, request):

        form = RegisterForm()

        context = { 'form': form }

        return render(request, 'register.html', context)

class Login(View):

    def post(self, request):

        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))

            if user is not None:

                login(request, user)

                return redirect('upload')

    def get(self, request):

        form = AuthenticationForm(request)

        context = { 'form': form }

        return render(request, 'login.html', context)

class Logout(View):

    def get(self, request):

        logout(request)

        return redirect('upload')