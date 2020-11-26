from django.shortcuts import render
from django.http import HttpResponse
from blog import auth
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from blog.models import Blog, Post
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class PostListView(ListView):

    model = Post
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.model.objects.all()
        # context['now'] = timezone.now()
        return context


class UserListView(ListView):
    
    model = User
    # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = self.model.objects.all()
        # context['now'] = timezone.now()
        return context


class UserDetailView(DetailView):
    model = User


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.model.objects.get(id=kwargs['user_id'])
        # context['now'] = timezone.now()
        return context


def index(request):
    temp = request.COOKIES
    # return HttpResponse(temp)
    user = authenticate(username=request.COOKIES['username'], password=request.COOKIES['password'])
    if user is not None:
        # A backend authenticated the credentials
        username = request.COOKIES['username']
        return HttpResponse(f'Hello, world. Youre at the polls index. {username} authenticated')
    else:
        return HttpResponse('Hello, world. Youre at the polls index. user undefined')
        # No backend authenticated the credentials


def loginCheck(request):
    temp = request.COOKIES
    resultStr = ''
    responseObj = HttpResponse()


    inputUsername = request.POST['username']
    inputPassword = request.POST['password']


    # искать пользователя с данными
    user = authenticate(username=inputUsername, password=inputPassword)
    if user is not None:
        # A backend authenticated the credentials
        resultStr += f'Hello, world. Youre at the polls index. {inputUsername} authenticated<br>'
        # записать данные в куки
        responseObj.set_cookie('username', inputUsername)
        responseObj.set_cookie('password', inputPassword)


    else:
        resultStr += f'Hello, world. Youre at the polls index. {inputUsername} not found<br>'
        # No backend authenticated the credentials



    resultStr += f'cookies:<br>'
    for key, value in request.COOKIES.items():
        resultStr += f'{key}: {value}<br>'
    responseObj.write(resultStr)
    return responseObj