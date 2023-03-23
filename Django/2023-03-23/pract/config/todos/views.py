from django.shortcuts import render, redirect
from .form import TodoForms
from .models import Todo

# Create your views here.
def index(request):
    print('index함수 도착')
    form = TodoForms()
    todo_lst = Todo.objects.all()
    print(todo_lst)
    
    context = {
        'form' : form, 
        'todos' : todo_lst,
    }
    
    return render(request, 'todos/index.html', context)

def create(request):
    print(request)
    print(request.method)
    print(type(request.method))
    print(request.POST)

    if request.method == "POST": #작성요청
        form = TodoForms(request.POST)
        if form.is_valid: # 유효성 검사 -> cleaned data (dict) 가 나옴 
            form.save()
            print('왜')
            return redirect('todos:index')

def update(request, pk):
    print('update')
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid :
            form.save()
        return redirect('todos:index')
    
    else:
        form = TodoForms(instance = todo) 
    
    context = {
        'form' : form,
        'todo' : todo,
    }

    return render(request, 'todos/update.html',context)

def delete(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect('todos:index')

    else:
        return redirect('todos:index')