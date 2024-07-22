from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.http import JsonResponse

from apps.users.models import User as user_model
from . import models, serializers
from .forms import CreatePostForm, UpdatePostForm, CommentForm
from django.urls import reverse
from django.db.models import Count

# Create your views here.

def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentForm()
    ctx = {
        'posts' : posts,
        'comment_form': comment_form
    }
    return render(request, 'posts/post_list.html', ctx)


def post_create(request):
    if request.method == 'GET':
        form = CreatePostForm()
        return render(request, 'posts/post_create.html', {"form": form})
    
    elif request.method == 'POST':
        if request.user.is_authenticated:
            user = get_object_or_404(user_model, pk=request.user.id)
            form = CreatePostForm(request.POST, request.FILES)

            if form.is_valid():
                post = form.save(commit=False)
                post.author = user
                post.save()
            else:
                print(form.errors)
            return redirect(reverse('posts:post_list'))

        else:
            return render(request, 'posts/post_list.html')

def post_like(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        user = request.user
        if user in post.post_likes.all():
            post.post_likes.remove(user)
            result = 'unlike'
        else:
            post.post_likes.add(user)
            result = 'like'
        post.save()
        return JsonResponse({'result': result, 'likes_count': post.post_likes.count()})
    
def comment_create(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(models.Post, pk=post_id)

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.posts = post
            comment.save()

            return redirect(reverse('posts:post_list') + "#comment-"+ str(comment.id))

        else:
            return render(request, 'posts/post_list.html')

def comment_delete(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(models.Comment, pk=comment_id)
        if request.user == comment.author:
            comment.delete()

        return redirect(reverse('posts:post_list'))

    else:
        return render(request, 'posts/post_list.html')