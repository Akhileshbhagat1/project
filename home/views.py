from django.shortcuts import render
from django.views.generic import ListView

from user.models import Post


def home(request):
    context = {'post': Post.objects.all()}
    return render(request, 'home/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'post'
    ordering = ['-date_published']



