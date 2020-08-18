from django.urls import path
from . import views

app_name = 'axisPosts' # NameSpace for app

urlpatterns = [
    path('', views.postView, name='postView'),
    path('postTest1/', views.postViewTest1, name='PostListTest1'),
    path('reactions/', views.reactions, name='reactions'),
]
