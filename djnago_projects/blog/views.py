from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Gaurav Choube',
        'title': 'First post of the blog',
        'content': 'Ethics and Values related to AI',
        'date_psoted': 'March 26, 2020'
    },
    {
        'author': 'Andrew Ng',
        'title': 'Second post of the blog',
        'content': 'Tuning Hyperparameters and regularization of models',
        'date_psoted': 'March 26, 2020'
    }
]

def home(request):
    context = {
            'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About  '})