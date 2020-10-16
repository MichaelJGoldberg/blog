from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from .models import User,Question,Comment,Choice
from .forms import CommentForm,SearchForm,AddForm
# Create your views here.

def index(request):
    q_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list':q_list}
    return render(request, 'index.html', context)

def comment(request, question_id):
    _CommentForm = CommentForm()
    return render(request, 'comment.html',{'form':_CommentForm})

def commenting(request, question_id):
    if request.method == "POST":
        _text = request.POST.get("_input")
        value = Question.objects.get(id = question_id)
        comment = Comment(texts= _text,post = value)
        comment.save()
        return redirect('http://127.0.0.1:8000/')

def details(request, question_id):

    value = Question.objects.get(id = question_id)
    _question = get_object_or_404(Question, pk=question_id)

    c_list = Comment.objects.filter(post = value)
    ch_list = Choice.objects.filter(votepage = value)

    context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list}

    return render(request, 'details.html', context)

def select(request, question_id):

    if request.method == "POST":
        _question = get_object_or_404(Question, pk=question_id)
        _id = request.POST.get("choice")

        _choice = Choice.objects.get(id = _id)
        _choice.votes += 1
        _choice.save()

        return render(request, 'results.html', {"choice":_choice})

def search(request):

    _SearchForm = SearchForm

    context = {"search_form":_SearchForm}

    return render(request, 'search.html',context)

def searching(request):

    if request.method == "POST":
        value = request.POST.get("_input")
        _question = Question.objects.get(title = value)
        c_list = Comment.objects.filter(post = _question)
        ch_list = Choice.objects.filter(votepage = _question)
        context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list}
        link = '//127.0.0.1:8000/'+str(_question.id)
        return redirect(link)

def add(request):

    _AddForm = AddForm()
    context = {"add_form": _AddForm}
    return render (request, 'add.html', context)

def adding(request): 

    if request.method == "POST":
        _title = request.POST.get("title")
        _text = request.POST.get("text")
        _author = request.POST.get("author")
        _user = User.objects.get(name=_author)
        obj = Question.objects.create(title = _title, text = _text, user = _user )
        context  = {"object":obj}
        return render(request, 'add_results.html', context)

def upvote(request, question_id):

    if request.method == "POST":
        _question = Question.objects.get(id = question_id)

        _question.upvotes += 1
        _question.save()

        link = '//127.0.0.1:8000/'+str(_question.id)
        return redirect(link)

def downvote(request, question_id):
    
    if request.method == "POST":
        _question = Question.objects.get(id = question_id)

        _question.downvotes += 1
        _question.save()

        link = '//127.0.0.1:8000/'+str(_question.id)
        return redirect(link)

