from django.shortcuts import render


def about_user(request):

    return render(request, 'home/about.html')
