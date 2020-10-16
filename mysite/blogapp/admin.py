from django.contrib import admin
from .models import User, Question, Comment, Choice
# Register your models here.
admin.site.register(User)
admin.site.register(Question)
admin.site.register(Comment)
admin.site.register(Choice)

