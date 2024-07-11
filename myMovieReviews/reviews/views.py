from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def review_list(request):
    reviews = Review.objects.all()
    content = {
        'reviews':reviews,
    }
    return render(request, 'review_list.html', content)

def review_create(request):
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

    context = {}

    return render(request, "review_create.html", context=context)

def review_detail(request,id):
    review = Review.objects.get(id=id)
    context = {
        "review":review
    }
    return render(request, "review_detail.html", context=context)

def review_update(request, id):
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
    
    review = Review.objects.get(id=id)
    context = {
        "review":review
    }
    return render(request, "review_update.html", context=context)

def review_delete(request,id):
    if request.method=="POST":
        review = Review.objects.get(id=id)
        review.delete()
    return redirect("/reviews")