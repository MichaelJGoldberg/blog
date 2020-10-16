from django import forms

class CommentForm(forms.Form):
    _input = forms.CharField(max_length=400)

class SearchForm(forms.Form):
    _input = forms.CharField(max_length=100)

class AddForm(forms.Form): 
    title = forms.CharField(max_length = 100)
    text = forms.CharField(max_length = 1000)
    author = forms.CharField(max_length = 1000)


