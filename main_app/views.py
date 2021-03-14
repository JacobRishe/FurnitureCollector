from django.shortcuts import render, redirect
from .models import Furniture
from .forms import DestroyForm
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login
# temporary
from django.http import HttpResponse

# Add the Cat class & list and view function below the imports
# class Furniture:  # Note that parens are optional if not inheriting from another class
# def __init__(self, name, color, description):
#     self.name = name
#     self.color = color
#     self.description = description
#
# furniture = [
#   Furniture('Chair', 'black', 'hardwood with velvet cushions'),
#   Furniture('Table', 'expresso brown', 'maple square table'),
#   Furniture('Bed', 'black tripod', 'solid walnut king size bed')
# ]

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello Jake</h1>')

def about(request):
    return render(request, 'about.html')

def furniture_index(request):
    furniture = Furniture.objects.all()
    return render(request, 'furniture/index.html', {'furniture': furniture})

def furniture_detail(request, furniture_id):
    furniture = Furniture.objects.get(id=furniture_id)
    destroy_form = DestroyForm()
    context = {
    'furniture': furniture,
    'destroy_form': destroy_form
    }
    return render(request, 'furniture/detail.html', context)

def add_destroy(request, furniture_id):
    form = DestroyForm(request.POST)
    if form.is_valid():
        new_destroy = form.save(commit=False)
        new_destroy.furniture_id = furniture_id
        new_destroy.save()
    return redirect('detail', furniture_id=furniture_id)

# def signup(request):
#     error_message = ''
# if they hit the submit button
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#           user = form.save()
#           login(request, user)
#           return redirect('index')
#       else:
#           error_message = 'Invalid sign up - please try again'
#     form = UserCreationForm()
#     context = {'form': form, 'error_message': error_message}
#     return render(request, 'registration/signup.html', context)
