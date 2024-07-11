from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    year = models.IntegerField(verbose_name="개봉 연도")
    genre = models.CharField(max_length=50, verbose_name="장르")
    star = models.FloatField(verbose_name="별점")
    review = models.TextField(verbose_name="리뷰내용")
    director = models.CharField(max_length=50 ,verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="주연배우")
    running = models.IntegerField(verbose_name="러닝타임")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)