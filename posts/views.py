from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import PostForm, UpdateForm, CommentForm
from .models import Post
from .filters import PostFilter

def homePageView(request):
    # Show posts in descending order
    posts = Post.objects.all()
    f = PostFilter(request.GET, posts)
    posts = f.qs

    # Show the latest 25 posts (descending (-) with [0:25])
    context = {'posts': posts.order_by('-date_posted')[0:25], 'filter': f}

    return render(request, 'home.html', context)

def createNewPost(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid:
            post = form.save(commit=False)
            post.users = request.user
            post.save()
            return redirect('/')

    context = {'post_form': form}
    
    return render(request, 'new_post.html', context)

def deleteUserPost(request, pk):
    # If you just have post.delete() it's a GET method. We want to let the user have comfirmation
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        post.delete()
        return redirect('/')

    context = {'delete_post': post}
    return render(request, 'delete_post.html', context) 

def updateUserPost(request, pk):
    post = Post.objects.get(pk=pk)
    form = UpdateForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'update_form': form}
    return render(request, 'update_form.html', context)

def createComment(request, pk):
    post = Post.objects.get(pk=pk)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            return redirect('/')

    context = {'comment': form}
    return render(request, 'comment_form.html', context)

def infoPageView(request):
    return render(request, 'info.html')

