from django.shortcuts import render, redirect

from .forms import *


# Create your views here.
def home(request):
    women = Women.objects.all()
    data = {
        'title': 'Главная страница',
        'women': women
    }
    return render(request, 'main/home.html', data)


def showpost(request, post_id):
    women = Women.objects.filter(id=post_id)
    data = {
        'womenpost': women
    }
    print(data)
    return render(request, 'main/showpost.html', data)


def addpost(request):
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = AddPost()
    data = {
        'title': 'Добавить новую запись',
        'form': form,
    }
    return render(request, 'main/addpost.html', data)
