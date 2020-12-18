from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.
def index(request):
    return render(request, 'app_two/index.html')

def help(request):
    my_dict = {'insert_me':'Hello, this was inserted from views.py file. This is a help page.'}
    return render(request, 'app_two/help.html')

def users(request):
    form = forms.NewUserForm()

    if request.method == "POST":
        form = forms.NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Error! Invalid form")

    return render(request, 'app_two/users.html', {'form': form})
