from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseNotAllowed
from .forms import PersonForm,TodoForm
from .models import Todo

# Create your views here.
def hello_word_view(request):
    return HttpResponse('hello_world')

def home(request):
    return HttpResponse('hello from home page view')

def home_render(request):
    return render(request, 'todos/home.html')

def helloGreetings(request,name):
    return HttpResponse(f'Hello {name} Welcome to Django')

def search(request):
    return HttpResponse(f'your search query is {request.GET.get("query")}')


def post_example(request):
    if request.method == 'POST':
        form=PersonForm(request.POST)
        if form.is_valid(): 
            name=form.cleaned_data['name']
            age=form.cleaned_data['age']
            job=form.cleaned_data['job']
            return HttpResponse(f'this is your post data ,Hello {name} you are {age} years old and your job is {job}')
    else:
        return HttpResponseNotAllowed('This is not a post request')
        
        
def submitExample(request):
    return render(request, 'todos/submit.html')     
 
def submitForm(request):
    form =PersonForm()
    return render(request, 'todos/submit_form.html',{'form':form})  


def todos_view(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')
    else:
        form = TodoForm()

    todos = Todo.objects.all()
    return render(request, 'todos/todos.html', {'form': form, 'todos': todos})
