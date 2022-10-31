from django.shortcuts import render
from .models import Users, Topics, Messages
from .forms import SendingMessageForm, AuthForm
from django.http import HttpResponseRedirect
from django.urls import reverse
import uuid
from .auth import check_password, making_hash

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip 


def get_user_by_token(token, request):
    browser = request.META.get("HTTP_USER_AGENT", "")
    ip = get_client_ip(request)
    amount = Users.objects.filter(token=token)
    user = Users.objects.filter(token=token, browser=browser, ip=ip)
    return [user, amount]


def auth(request):
    token = request.session.get('token','')
    user = None
    amount = None
    if token != '':
        user, amount = get_user_by_token(token, request)
        user = user[0]
        if not user:
            if amount:
                amount.token=''
                amount.save()
            del request.session['token']
    
    return [request, user]


# Create your views here.
def init(request):
    request, user = auth(request)
    

    topics = Topics.objects.filter(created_in=None)
    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context
    return render(
        request,
        'index.html',
        context = {'topics': topics, 'user':user},
    )


def topic(request, pk):
    request, user = auth(request)
    
    topic = Topics.objects.get(id=pk)
    
    # Если контейнер (внутри есть ещё темы)
    if Topics.objects.filter(created_in=pk).count() != 0:
        topics = Topics.objects.filter(created_in=pk)
        return render(
            request,
            'index.html',
            context = {'topics': topics, "user":user},
        )


    # Отправка сообщения
    if request.method == "POST" and user:
        form = SendingMessageForm(request.POST)
        if form.is_valid():
            Messages.objects.create(text = form.cleaned_data['text'], sended_by=user, in_topic=topic)
            return HttpResponseRedirect(reverse('topic',args=[pk]) )
    
    # Просмотр темы форума
    outer = request.GET.get("outer",0)
    messages = topic.messages_set.all()#[outer:outer+10]
    form = SendingMessageForm()
    return render(
        request,
        'topic.html',
        context = {'topic': topic,
        "messages":messages, "form":form, "user":user},
    )


def login(request):
    request, user = auth(request)

    if request.method == "POST":
        form = AuthForm(request.POST)
        if form.is_valid():
            user = Users.objects.filter(name=form.cleaned_data['login'])
            if user and check_password(form.cleaned_data['password'], user[0].password):
                user = user[0]
                user.ip = get_client_ip(request)
                user.browser = request.META.get("HTTP_USER_AGENT", "")
                user.token = uuid.uuid4()
                user.save()
                request.session['token'] = str(user.token)
                return HttpResponseRedirect(reverse('home') )
        return HttpResponseRedirect(reverse('login') )

    if not user:
        form = AuthForm()
        return render(
            request,
            'sign_in.html',
            context = {"form":form, "user":user},
        )
    
    return HttpResponseRedirect(reverse('lk') )


def lk(request):
    request, user = auth(request)

    if not user:
        return HttpResponseRedirect(reverse('login') )
    
    if request.method == "POST":
        del request.session['token']
        user.token = ''
        user.save()
        return HttpResponseRedirect(reverse('home') )

    return render(
        request,
        'lk.html',
        context = {"user":user}
    )


def exit(request):
    request, user = auth(request)

    if user:
        del request.session["token"]
        user.token = ''
        user.save()
    
    
    return HttpResponseRedirect(reverse('home') )


# from django.views import generic

# class TopicsDetailView(generic.DetailView):
#     model = Topics