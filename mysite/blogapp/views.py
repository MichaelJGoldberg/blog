from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from .models import Question,Comment,Choice
from .forms import CommentForm,SearchForm,AddForm,LoginForm,EnterForm,ChoiceForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    
    q_list = Question.objects.order_by('-pub_date')[:5]
    context = {'question_list':q_list}

    return render(request, 'index.html', context)

@login_required
def details(request, question_id):

    value = Question.objects.get(id = question_id)
    _question = get_object_or_404(Question, pk=question_id)
    c_list = Comment.objects.filter(post = value)
    ch_list = Choice.objects.filter(votepage = value)
    context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list}
    return render(request, 'details.html', context)

@login_required
def search(request):

        _SearchForm = SearchForm
        context = {"search_form":_SearchForm}
        return render(request, 'search.html',context)

@login_required
def searching(request):

        if request.method == "POST":
            value = request.POST.get("text")
            _question = Question.objects.get(title = value)
            c_list = Comment.objects.filter(post = _question)
            ch_list = Choice.objects.filter(votepage = _question)
            context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list}
            link = '//127.0.0.1:8000/' + str(_question.id)
            return redirect(link)

@login_required
def comment(request, question_id):

        _CommentForm = CommentForm()
        return render(request, 'comment.html',{'form':_CommentForm})

@login_required
def commenting(request, question_id):

        if request.method == "POST":
            _text = request.POST.get("text")
            value = Question.objects.get(id = question_id)
            comment = Comment(texts= _text,post = value, user = request.user)
            comment.save()
            link = '//127.0.0.1:8000/' + str(question_id)
            return redirect(link)

@login_required
def select(request, question_id):

    if request.method == "POST":
        _question = get_object_or_404(Question, pk=question_id)
        _id = request.POST.get("choice")
        _choice = Choice.objects.get(id = _id)
        _choice.votes += 1
        _choice.save()
        return render(request, 'results.html', {"choice":_choice})

@login_required
def add(request):

    _ChoiceForm = ChoiceForm()
    _AddForm = AddForm()
    context = {"add_form": _AddForm,"choice_form":_ChoiceForm}
    return render (request, 'add.html', context)

@login_required
def add_question(request):

    if request.method == "POST":
        _ChoiceForm = ChoiceForm()
        _AddForm = AddForm()
        context = {"add_form": _AddForm,"choice_form":_ChoiceForm}
        return render (request, 'add.html', context)


@login_required
def adding(request): 

    if request.method == "POST":
        _title = request.POST.get("title")
        _text = request.POST.get("text")
        obj = Question.objects.create(title = _title, text = _text, user = request.user )
        context  = {"object":obj}
        return render(request, 'add_results.html', context)


@login_required
def upvote(request, question_id):

    _question = Question.objects.get(id = question_id)
    _question.upvotes += 1
    _question.save()
    link = '//127.0.0.1:8000/'+ str(_question.id)
    return redirect(link)

@login_required
def downvote(request, question_id):

    if request.method == "POST":
        _question = Question.objects.get(id = question_id)
        _question.downvotes += 1
        _question.save()
        link = '//127.0.0.1:8000/' + str(_question.id)
        return redirect(link)

def login_page(request):

    _LoginForm = LoginForm()
    context = {'login_form':_LoginForm}
    return render(request, 'login_page.html', context)

def login(request):

    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        user = User.objects.create_user(name, email, password)
        context = {'user': user}
        return render(request, 'hello.html', context)

def welcome(request):

    return render(request, "welcome.html")

    






