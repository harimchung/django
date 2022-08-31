from django.db import models

# Create your models here.
class Article(models.Model):
    # 클래스의 변수가 하나의 필드가 된다. (스키마 제작)
    # title : 필드 이름, => 인스턴스
    # models.CharField() => 타입, 필수키워드 인자가 존재한다.
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)