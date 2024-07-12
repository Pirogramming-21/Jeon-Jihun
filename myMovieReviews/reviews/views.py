from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def review_list(request):
    sort = request.GET.get('sort','-created_at')
    if sort == 'title':
        reviews = Review.objects.order_by('title','-created_at')
    elif sort == 'star':
        reviews = Review.objects.order_by('-star','-created_at')
    elif sort == 'running':
        reviews = Review.objects.order_by('running','-created_at')
    else:
        reviews = Review.objects.order_by('-created_at')
    content = {
        'reviews':reviews,
        'sort':sort
    }
    return render(request, 'review_list.html', content)

def review_create(request):
    genre_choices = Review.genre_choices
    if request.method == 'POST':
        title = request.POST["title"]
        year = request.POST["year"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        review = request.POST["review"]
        director = request.POST["director"]
        running = request.POST["running"]

        Review.objects.create(title=title, year=year, actor=actor, genre=genre, star=star, review=review, director=director, running=running)
        return redirect("/reviews")

    context = {"genre_choices": genre_choices}

    return render(request, "review_create.html", context=context)

def review_detail(request,id):
    review = Review.objects.get(id=id)
    review.running_time_hours = review.running // 60
    review.running_time_mins = review.running % 60
    context = {
        "review":review
    }
    return render(request, "review_detail.html", context=context)

def review_update(request, id):
    review = Review.objects.get(id=id)
    if request.method == "POST":
        title = request.POST["title"]
        year = request.POST["year"]
        actor = request.POST["actor"]
        genre = request.POST["genre"]
        star = request.POST["star"]
        review = request.POST["review"]
        director = request.POST["director"]
        running = request.POST["running"]

        Review.objects.filter(id=id).update(title=title, year=year, actor=actor, genre=genre, star=star, review=review, director=director, running=running)
        return redirect(f"/reviews/{id}")
    
    context = {
        "review":review
    }
    return render(request, "review_update.html", context=context)

def review_delete(request,id):
    if request.method=="POST":
        review = Review.objects.get(id=id)
        review.delete()
    return redirect("/reviews")