from django.urls import path
from . import views
from .models import Question, Comment
urlpatterns = [
    path('index/', views.index),
    path('', views.welcome),
    path('<int:question_id>/comment/commenting/',views.commenting),
    path('<int:question_id>/', views.details),
    path('<int:question_id>/comment/', views.comment ),
    path('<int:question_id>/comment/commenting/', views.commenting ),
    path('<int:question_id>/select/', views.select),
    path('search/', views.search),
    path('search/searching/', views.searching),
    path('add/', views.add),
    path('add_question/',views.add_question),
    path('adding/', views.adding),
    path('<int:question_id>/upvote/', views.upvote),
    path('<int:question_id>/downvote/', views.downvote),
    path('login/', views.login_page),
    path('log_in/', views.login),


]