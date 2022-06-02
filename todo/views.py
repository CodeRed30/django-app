from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse  
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label='New Task', widget=forms.TextInput(attrs={'placeholder': 'New task'}))
# Create your views here.
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'todo/index.html', {'tasks': request.session["tasks"]})

def add(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            request.session["tasks"] += [form.cleaned_data['task']]
            return HttpResponseRedirect(reverse("todo:index"))
        else:
            return render(request, 'todo/index.html', {'form': form})
    return render(request, 'todo/add.html', {'form': NewTaskForm()}) 