from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Furniture, Finish
from .forms import DestroyForm, FurnitureForm


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def furniture_index(request):
    furniture = Furniture.objects.filter(user=request.user)
    return render(request, 'furniture/index.html', {'furniture': furniture})

@login_required
def furniture_new(request):
    furniture_form = FurnitureForm(request.POST or None)
    if request.POST and furniture_form.is_valid():
        new_furniture = furniture_form.save(commit=False)
        new_furniture.user = request.user
        new_furniture.save()
        return redirect('index')
    else:
        print("hello")
        return render(request, 'furniture/new.html', { 'furniture_form': furniture_form })

@login_required
def furniture_edit(request, furniture_id):
  # get a reference to a cat
  furniture = Furniture.objects.get(id=cat_id)
  # build a form for the cat filling it with values from the instance or values from the POST request
  furniture_form = FuritureForm(request.POST or None, instance=furniture)
  if request.POST and furniture_form.is_valid():
    # save changes to the cat
    furniture_form.save()
    # redirect to the detail page
    return redirect('detail', furniture_id=furniture_id)
  else:
    return render(request, 'furniture/edit.html', { 'furniture': furniture, 'furniture_form': furniture_form })

@login_required
def furniture_delete(request, cat_id):
  Furniture.objects.get(id=furniture_id).delete()
  return redirect('index')

@login_required
def furniture_detail(request, furniture_id):
    furniture = Furniture.objects.get(id=furniture_id)
    finish_furniture_doesnt_have = Finish.objects.exclude(id__in = furniture.finish.all().values_list('id'))
    destroy_form = DestroyForm()
    context = {
    'furniture': furniture,
    'destroy_form': destroy_form,
    'finishes': finish_furniture_doesnt_have
    }
    return render(request, 'furniture/detail.html', context)

@login_required
def add_destroy(request, furniture_id):
    form = DestroyForm(request.POST)
    if form.is_valid():
        new_destroy = form.save(commit=False)
        new_destroy.furniture_id = furniture_id
        new_destroy.save()
    return redirect('detail', furniture_id=furniture_id)

@login_required
def assoc_finish(request, furniture_id, finish_id):
    furniture = Furniture.objects.get(id=furniture_id)
    furniture.finishes.add(finish_id)
    return redirect('detail', furniture_id=furniture_id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          user = form.save()
          login(request, user)
          return redirect('index')
        else:
          error_message = 'Invalid sign up - please try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
