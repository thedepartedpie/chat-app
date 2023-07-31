from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from chat.forms import LoginForm, RegistrationForm
from chat.models import ChatModel


@login_required
def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

@login_required
def chat(request, reciever_id):
    reciever = User.objects.get(id=reciever_id)

    sender_chats = ChatModel.objects.filter(sender=request.user.sendermodel, receiver=reciever.receivermodel)
    reciever_chats = ChatModel.objects.filter(sender=reciever.sendermodel, receiver=request.user.receivermodel)

    chats = list(sender_chats)
    if request.user.id != reciever.id:
        chats += list(reciever_chats)
    
    chats.sort(key=lambda chat: chat.pk)

    context = {
        'chats': chats,
        'reciever': reciever
    }
    return render(request, 'chat.html', context)



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('chat:home')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password1)

            if user is not None:
                login(request, user)
                return redirect('chat:home')
            
            return redirect('chat:login')
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})