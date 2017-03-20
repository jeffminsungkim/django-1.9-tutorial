from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def post_create(request):
    return HttpResponse("<h1>Create!</h2>")

def post_detail(request, id=None): # retrieve
    instanace = get_object_or_404(Post, id=id)
    context = {
        "title": instanace.title,
        "instance": instanace,
    }
    return render(request, "post_detail.html", context)

def post_list(request): # list itmes
    queryset = Post.objects.all()
    context = {
        "object_list": queryset,
        "title": "List"
    }
    return render(request, "index.html", context)

def post_update(request):
    return HttpResponse("<h1>Update!</h2>")

def post_delete(request):
    return HttpResponse("<h1>Delete!</h2>")

