from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk') #모든 Post 레코드 가져오기 / pk를 역순으로 정렬 (최신순)

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk) #single_post_page() 함수의 매개변수로 받은 pk와 Post 모델의 pk 필드 값이 같은 레코드 가져오기

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post,
        }
    )