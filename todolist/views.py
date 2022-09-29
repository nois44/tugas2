from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import TaskEditForm, TaskCreateForm
from .models import Task

# Create your views here.
@login_required(login_url='/todolist/login/')

#Memperlihatkan halaman utama
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    count = tasks.filter(is_finished=False).count()
    search_input = request.GET.get('search_area') or ''
    
    if search_input:
        tasks = Task.objects.filter(user=request.user, title__icontains=search_input)
    else:
        tasks = Task.objects.filter(user=request.user)
    context = {'tasks': tasks, 'count': count, 'search_input': search_input}
    return render(request, 'main_page.html', context)

#Memperlihatkan detail untuk Task yang dipilih
def taskdetail(request, pk):
    task = Task.objects.get(title=pk)
    context = {'task': task}
    return render(request, 'detail.html', context)

#Function yang digunakan untuk meng-edit task
def taskedit(request, pk):
    task = Task.objects.get(title=pk)
    form = TaskEditForm(instance=task)

    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=task.title)

    context = {'task': task, 'form': form}
    return render(request, 'edit.html', context)

#Function untuk menghapus task
def taskdelete(request, pk):
    task = Task.objects.get(title=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('tasklist')

    context = {'task': task}
    return render(request, 'delete.html', context)

#Function untuk membuat task
def taskcreate(request):
    user = request.user
    form = TaskCreateForm()

    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = user
            task.save()
            return redirect('tasklist')

    context = {'form': form}
    return render(request, 'create-task.html', context)

#Memperlihatkan halaman untuk login
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tasklist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

#Logout dari akun yang sedang digunakan
def logout_user(request):
    logout(request)
    return redirect('login')

#Mendaftarkan user ke database
def register_user(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('login')

    context = {'form':form}
    return render(request, 'signup.html', context)

