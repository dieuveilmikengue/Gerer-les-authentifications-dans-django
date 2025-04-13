from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Todo
from .forms import TodoForm

@login_required
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todolist/todo_list.html', {'todos': todos})

@login_required
def todo_create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # Associer la tâche à l'utilisateur connecté
            todo.save()
            return redirect('todolist:todo_list')  # Redirection vers la liste des tâches
    else:
        form = TodoForm()
    return render(request, 'todolist/todo_form.html', {'form': form})

@login_required
def todo_update(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todolist:todo_list')  # Redirection vers la liste des tâches
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todolist/todo_form.html', {'form': form})

@login_required
def todo_delete(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('todolist:todo_list')  # Redirection après suppression
    return render(request, 'todolist/todo_confirm_delete.html', {'todo': todo})
