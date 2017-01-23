from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .form import PostForm

# Create your views here.
def post_home(request):
    queryset = Post.objects.all()
    context = {
        "title": "Title!",
        "posts": queryset,
    }
    return render(request, "index.html", context)

def detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Title!",
        "instance": instance,
    }
    return render(request, "my_post.html", context)

def post_create(request):
    # form = PostForm()
    # if request.method=="POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
    #     # Post.objects.create(title=title,~~)
    form = PostForm(request.POST)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form" : form,
    }
    return render(request, "post_form.html", context)

def post_update(request, id=None):
    # form = PostForm()
    # if request.method=="POST":
    #     print request.POST.get("content")
    #     print request.POST.get("title")
    #     # Post.objects.create(title=title,~~)
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance= instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    
    context = {
        "form" : form,
        "instance" : instance,
    }
    return render(request, "post_form.html", context)