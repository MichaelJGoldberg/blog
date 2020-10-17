from django import forms

class CommentForm(forms.Form):
    _input = forms.CharField(max_length=400)

class SearchForm(forms.Form):
    _input = forms.CharField(max_length=100)

class AddForm(forms.Form): 
    title = forms.CharField(max_length = 100)
    text = forms.CharField(max_length = 1000)
    author = forms.CharField(max_length = 1000)

class LoginForm(forms.Form): 
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField()
    password = forms.IntegerField()
    email = forms.EmailField()

class EnterForm(forms.Form): 
    name = forms.CharField(max_length=100)
    password = forms.IntegerField()

