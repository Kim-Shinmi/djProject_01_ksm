from django.shortcuts import render
from .models import Post

# Create your views here.
def boardList(request):
    posts = Post.objects.all().order_by('-pk')      # 모든 Post 객체를 가져와서 정렬 ('-pk' : pk 역순정렬)

    return render(          # render 함수는 세 번째 인수로 전달된 딕셔너리 데이터를 템플릿 파일에 적용하여 HTML 코드로 변환
        request,                    # 첫 번째 인수: 반드시 request
        'boardList.html',           # 두 번째 인수: 템플릿 파일의 경로
        {                           # 세 번째 인수(블록으로 표기)
            'posts' : posts,                # posts 키에 posts 변수를 할당
        }
    )

def boardPage(request, pk):                  # pk 인자: URL에서 추출한 게시물의 고유 번호
    post = Post.objects.get(pk=pk)          # pk가 매개변수 pk와 같은 Post 객체를 post 변수에 할당

    return render(
        request,
        'boardPage.html',       # 템플릿 파일의 경로
        {
            'post': post,
        }
    )
