from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from . import models


def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        emailid = request.POST.get('emailid')
        pwd = request.POST.get('pwd')

        if User.objects.filter(username=fnm).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})

        if User.objects.filter(email=emailid).exists():
            return render(request, 'signup.html', {'error': 'Email already registered'})

        User.objects.create_user(username=fnm, email=emailid, password=pwd)

        return redirect('/login/')   # ✅ fixed

    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        user = authenticate(request, username=fnm, password=pwd)

        if user is not None:
            auth_login(request, user)
            return redirect('/todopage/')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')


@login_required(login_url='/login')
def todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            models.TODOO.objects.create(title=title, user=request.user)
        return redirect('/todopage/')

    res = models.TODOO.objects.filter(user=request.user).order_by('-date')

    total = res.count()
    completed = res.filter(is_completed=True).count()
    pending = res.filter(is_completed=False).count()

    return render(request, 'todo.html', {
        'res': res,
        'total': total,
        'completed': completed,
        'pending': pending
    })


@login_required(login_url='/login')
def edit_todo(request, srno):
    obj = get_object_or_404(models.TODOO, srno=srno, user=request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        if title:
            obj.title = title
            obj.save()
        return redirect('/todopage/')   # ✅ fixed

    return render(request, 'edit_todo.html', {'obj': obj})


@login_required(login_url='/login')
def delete_todo(request, srno):
    if request.method == 'POST':   # ✅ safe delete only
        obj = get_object_or_404(models.TODOO, srno=srno, user=request.user)
        obj.delete()
    return redirect('/todopage/')


@login_required(login_url='/login')
def toggle_complete(request, srno):
    obj = get_object_or_404(models.TODOO, srno=srno, user=request.user)
    obj.is_completed = not obj.is_completed
    obj.save()
    return redirect('/todopage/')


def signout(request):
    logout(request)
    return redirect('/login/')