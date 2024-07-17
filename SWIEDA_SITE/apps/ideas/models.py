from django.db import models
from apps.tools.models import Tool

# Create your models here.
class Idea(models.Model):
    title = models.CharField('제목', max_length=24)
    content = models.CharField('내용', max_length=300)
    photo = models.ImageField('이미지', blank=True, upload_to='posts/%Y%m%d')
    interest = models.IntegerField('아이디어 관심도', default=0)
    devtool = models.ForeignKey(Tool, on_delete=models.SET_NULL, verbose_name="개발툴", null=True)
    # 찜하기 여부
    dibs = models.BooleanField('찜', default = False)
    created_date = models.DateTimeField('작성일', auto_created=True, auto_now_add=True)
    updated_date = models.DateTimeField('수정일', auto_created=True, auto_now=True)

# class IdeaStar(models.Model):
#     idea = models.ForeignKey(Idea, on_delete=models.CASCADE)