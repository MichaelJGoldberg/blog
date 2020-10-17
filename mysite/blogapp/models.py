from django.db import models
# Create your models here.
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    text = models.TextField()
    pub_date = models.DateField(auto_now=True)  
    upvotes = models.IntegerField(default = 0)
    downvotes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    texts = models.TextField()
    post = models.ForeignKey(Question,related_name='comments',on_delete = models.CASCADE)

    def __str__(self):
        return self.texts

class Choice(models.Model):
    votepage = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.TextField()
    votes = models.IntegerField(default = 0)

    def __str__(self):
        return self.choice_text


