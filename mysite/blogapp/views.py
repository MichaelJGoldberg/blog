from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from .models import User,Question,Comment,Choice
from .forms import CommentForm,SearchForm,AddForm,LoginForm,EnterForm
# Create your views here.

def index(request, user_id):

    user = get_object_or_404(User, name = user_id)
    if user.is_authentefikated == True:
        q_list = Question.objects.order_by('-pub_date')[:5]
        context = {'question_list':q_list,'user':user}

        return render(request, 'index.html', context)
    else:
        return redirect('http://127.0.0.1:8000/')

def details(request, question_id, user_id):

    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        value = Question.objects.get(id = question_id)
        _question = get_object_or_404(Question, pk=question_id)
        user = get_object_or_404(User, name = user_id)
        c_list = Comment.objects.filter(post = value)
        ch_list = Choice.objects.filter(votepage = value)

        context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list,'user':user}

        return render(request, 'details.html', context)
    else:
        return redirect('http://127.0.0.1:8000/')

def search(request, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:

        _SearchForm = SearchForm
        context = {"search_form":_SearchForm}
        return render(request, 'search.html',context)
    
    else:
        return redirect('http://127.0.0.1:8000/')

def searching(request, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        if request.method == "POST":
            value = request.POST.get("_input")
            _question = Question.objects.get(title = value)
            c_list = Comment.objects.filter(post = _question)
            ch_list = Choice.objects.filter(votepage = _question)
            context = {'question': _question,'commentary_list':c_list,'choice_list':ch_list}
            link = '//127.0.0.1:8000/'+user_id + ("/") + str(_question.id)
            return redirect(link)
    else:
        return redirect('http://127.0.0.1:8000/')

def comment(request, question_id, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        _CommentForm = CommentForm()
        return render(request, 'comment.html',{'form':_CommentForm})
    else:
        return redirect('http://127.0.0.1:8000/')

def commenting(request, question_id, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        if request.method == "POST":

            _text = request.POST.get("_input")
            value = Question.objects.get(id = question_id)
            comment = Comment(texts= _text,post = value)
            comment.save()
            link = '//127.0.0.1:8000/'+user_id + ("/") + str(question_id)
            return redirect(link)
        else:
            return redirect('http://127.0.0.1:8000/')

def select(request, question_id, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        if request.method == "POST":
            _question = get_object_or_404(Question, pk=question_id)
            _id = request.POST.get("choice")
            _choice = Choice.objects.get(id = _id)
            _choice.votes += 1
            _choice.save()

            return render(request, 'results.html', {"choice":_choice,"user":user})
    else:
        return redirect('http://127.0.0.1:8000/')

def add(request, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        _AddForm = AddForm()
        context = {"add_form": _AddForm,"user":user}
        return render (request, 'add.html', context)

    else:
        return redirect('http://127.0.0.1:8000/')

def adding(request, user_id): 
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        if request.method == "POST":
            _title = request.POST.get("title")
            _text = request.POST.get("text")
            _author = request.POST.get("author")
            _user = User.objects.get(name=_author)
            obj = Question.objects.create(title = _title, text = _text, user = _user )
            context  = {"object":obj,"user":user}
            return render(request, 'add_results.html', context)
    else:
        return redirect('http://127.0.0.1:8000/')

def upvote(request, question_id, user_id):
    user = get_object_or_404(User, name = user_id)
    
    if user.is_authentefikated == True:
        if request.method == "POST":
            _question = Question.objects.get(id = question_id)

            _question.upvotes += 1
            _question.save()

            link = '//127.0.0.1:8000/'+user_id + ("/") + str(_question.id)
            return redirect(link)
    else:
        return redirect('http://127.0.0.1:8000/')

def downvote(request, question_id, user_id):
    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:
        if request.method == "POST":
            _question = Question.objects.get(id = question_id)

            _question.downvotes += 1
            _question.save()

            link = '//127.0.0.1:8000/'+user_id + ("/") + str(_question.id)
            return redirect(link)
        else:
            return redirect('http://127.0.0.1:8000/')

def login(request):
    _LoginForm = LoginForm()
    context = {'login_form':_LoginForm}
    return render(request, 'login.html', context)

def logging(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        password = request.POST.get("password")
        email = request.POST.get("email")
        birth_date = request.POST.get("birth_date")
        user = User.objects.create(name = name, birth_date = birth_date, email = email, password = password)
        context = {'user': user}
        return render(request, 'hello.html', context)

def welcome(request):
    return render(request, "welcome.html")

def enter(request):
    _EnterForm = EnterForm()
    context = {'enter_form':_EnterForm}
    return render(request, "enter.html", context)

def entering(request):
    if request.method == "POST": 
        name = request.POST.get("name")
        password = request.POST.get("password")
        user = get_object_or_404(User,name = name, password = password)
        if user != 0:
            context = {'user':user}
            user.is_authentefikated = True
            user.save()
            return render(request, 'hello.html', context)

def exit(request, user_id):

    user = get_object_or_404(User, name = user_id)

    if user.is_authentefikated == True:

        user = get_object_or_404(User, name = user_id)
        user.is_authentefikated = False
        user.save()
        return redirect('http://127.0.0.1:8000/')

    else:
        return redirect('http://127.0.0.1:8000/')
    






