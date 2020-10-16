from django.urls import path
from . import views
from .models import Question, Comment, User
urlpatterns = [
    path('', views.index),
    path('<int:question_id>/comment/commenting/',views.commenting),
    path('<int:question_id>/', views.details),
    path('<int:question_id>/comment/', views.comment ),
    path('<int:question_id>/select/', views.select),
    path('search/', views.search),
    path('search/searching/', views.searching),
    path('add/', views.add),
    path('adding/', views.adding),
    path('<int:question_id>/upvote/', views.upvote),
    path('<int:question_id>/downvote/', views.downvote),

]