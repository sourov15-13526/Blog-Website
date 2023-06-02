from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post,Category

def home(request):
    # load all the post from db
    posts = Post.objects.all()
    cats = Category.objects.all()
    
    data = {
        'posts': posts,
        'cats':cats
    }
    return render(request, 'home.html',data)


def post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()
    data = {
        'post': post
    }
    return render(request, 'posts.html', {'post': post, 'cats': cats})


def category(request, url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat=cat)
    return render(request, "category.html",{'cat':cat, 'posts':posts})

def about(request):
    persons = [
    {'name': 'Md. Sourov Mia', 'photo_url': '/static/images/sourov.jpg', 'bio': 'Founder of L-Blogs and  a current student  CSE department at Daffodil International University'},
    {'name': 'Md. Aiyub Ali', 'photo_url': '/static/images/aiyub.jpg', 'bio': 'Software Engineer and a current student  CSE department at Daffodil International University'},
    {'name': 'Rabeya Boshri Mou', 'photo_url': '/static/images/mou.jpg', 'bio': 'Founder of L-Blogs'},
    {'name': 'Nafisa Haque Saima', 'photo_url': '/static/images/nafisa.jpg', 'bio': 'Founder of L-Blogs'}
    ]
    return render(request,'about.html',{'persons':persons})
