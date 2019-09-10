from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from accounts.views import *

from django.contrib.auth.models import User



@login_required (login_url='/login/')
def post_create_view(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        form.save()
        form = PostForm()
        return redirect('../../')
    context = {
        'form': form,
        'page': "Create new post"
    }
    return render(request, "posts/post_create.html", context)

@login_required (login_url='/login/')
def post_update_view(request, id=id):
    obj = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('..')
    context = {
        'form': form,
        'id': id,
        'page': "update post with id "
    }
    return render(request, "posts/post_create.html", context)

@login_required (login_url='/login/')
def post_list_view(request):
    queryset = Post.objects.filter(user=request.user)# list of objects
    # print(queryset)
    context = {
        "user": request.user,
        "object_list": queryset
    }
    return render(request, "posts/post_list.html", context)

@login_required (login_url='/login/')
def post_detail_view(request, id):
    obj = get_object_or_404(Post, id=id)
    context = {
        "object": obj
    }
    return render(request, "posts/post_detail.html", context)

@login_required (login_url='/login/')
def post_delete_view(request, id):
    obj = get_object_or_404(Post, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../../')
    context = {
        "object": obj
    }
    return render(request, "posts/post_delete.html", context)
