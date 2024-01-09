from django.db import models

class Post(models.Model):       # Post 모델 정의
    title = models.CharField(max_length=30)         # .CharField() : 한줄 문장을 입력(<input> 타입)
    content = models.TextField()                    # .TextField() : 여러줄의 문장을 입력할 수 있는 형식 (<textarea> 타입)

    created_at = models.DateTimeField(auto_now_add=True)    # auto_now_add: 생성시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True)        # auto_now: 수정시간을 자동으로 저장
    # author : 추후 작성 예정

    def __str__(self):                      # 객체를 문자열로 표현할 때 사용
        return f'[{self.pk}] {self.title}'           # pk: 객체의 고유한 번호, title: 제목. 게시물의 기본키가 대괄호로
    
    def get_absolute_url(self):             # get_absolute_rul 메서드 정의
        return f'/board/{self.pk}'                   # 게시물의 상세 페이지 주소를 반환 (포스팅된 게시물의 페이지번호를 pk를 이용하여 자동으로 추가)

