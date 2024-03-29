from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm
    return render(request, 'home/register.html', {'form': form})


@login_required
def profile(request):
    form = PostForm(request.POST)
    if form.is_valid():
        form.save()
        form = PostForm()
    return render(request, 'home/profile.html', {'form': form})

