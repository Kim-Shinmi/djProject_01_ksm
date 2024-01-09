from django.contrib import admin
from .models import Post            # Post 모델을 불러옴

# Register your models here.
admin.site.register(Post)           # Post 모델을 관리자 페이지에서 볼 수 있도록 등록
