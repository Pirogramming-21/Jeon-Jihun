from django.db import models

# Create your models here.

class Review(models.Model):
    title = models.CharField(max_length=100, verbose_name="제목")
    year = models.IntegerField(verbose_name="개봉 연도")

    # 장르 선택할 수 있게 개발
    genre_choices = (
        ('액션', '액션'),
        ('애니메이션', '애니메이션'),
        ('드라마', '드라마'),
        ('판타지', '판타지'),
        ('로맨스', '로맨스'),
        ('미스터리', '미스터리'),
        ('SF', 'SF'),
        ('호러', '호러'),
        ('범죄', '범죄'),
        ('기타', '기타'),
    )
    genre = models.CharField(max_length=50, choices=genre_choices, default='기타', verbose_name="장르")
    star = models.FloatField(verbose_name="별점")
    review = models.TextField(verbose_name="리뷰내용")
    director = models.CharField(max_length=50 ,verbose_name="감독")
    actor = models.CharField(max_length=50, verbose_name="주연배우")
    running = models.IntegerField(verbose_name="러닝타임")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)