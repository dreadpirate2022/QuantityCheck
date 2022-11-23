from django.shortcuts import render, redirect
from . models import Profile, Message
from django.contrib.auth.models import User
from constructions.models import Construction, Tag
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from . forms import CustomUserCreationForm, ProfileForm, PositionForm, MessageForm
from django.contrib.auth.decorators import login_required
from . utils import searchProfiles, paginateProfiles

# Create your views here.
def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('constructions:constructions')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('constructions:constructions')
        else:
            messages.error(request, 'Username OR Password is incorrect')

    return render(request, 'users/login_register.html')

def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('users:login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created')

            login(request, user)
            return redirect('users:edit-account')

        else:
            messages.error(request, 'An error has occured during registration')



    context = {'page':page, 'form':form}
    return render(request, 'users/login_register.html', context)

def profiles(request):
    profiles, search_query = searchProfiles(request)
    custom_range, profiles = paginateProfiles(request, profiles, 6)
    context = {'profiles': profiles, 'search_query': search_query, 'custom_range': custom_range}

    return render(request, 'users/profiles.html', context)

def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)    
    constructions = Construction.objects.all()
    context = {'profile':profile, 'constructions':constructions}
    return render(request, 'users/user-profile.html', context)

@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    constructions = profile.construction_set.all()

    context = {'profile':profile, 'constructions':constructions}
    return render(request, 'users/account.html', context)

@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('users:account')

    context = {'form':form}
    return render(request, 'users/profile_form.html', context)

def deleteAccount(request, pk):
    profile = request.user.profile
    if request.method == 'POST':
        profile.delete()
        messages.success(request, 'Your profile was deleted succesfully')
        return redirect('constructions:constructions')
    context = {'object':profile}
    return render(request, 'users/delete_template.html', context)

@login_required(login_url='login')
def inbox(request):
    profile = request.user.profile
    messageRequests = profile.messages.all()
    numberOfMessages = messageRequests.count()
    unreadCount = messageRequests.filter(is_read=False).count()
    context = {
        'messageRequests':messageRequests,
        'numberOfMessages':numberOfMessages,
        'unreadCount':unreadCount,
    }
    return render(request, 'users/inbox.html', context)

@login_required(login_url='login')
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.get(id=pk)
    if message.is_read == False:
        message.is_read = True
        message.save()
    context = {'message':message}
    return render(request, 'users/message.html', context)

def createMessage(request, pk):
    recipient = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient

            if sender:
                message.name = sender.name
                message.email = sender.email
            message.save()

            messages.success(request, 'Your message was successfully sent')
            return redirect('users:user-profile', pk=recipient.id)

    context = {'recipient':recipient, 'form':form}
    return render(request, 'users/message_form.html', context)

def deleteMessage(request, pk):
    message = Message.objects.get(id=pk)
    if request.method == 'POST':
        message.delete()
        messages.success(request, 'The message was deleted')
        return redirect('users:inbox')
    context = {'object':message}
    return render(request, 'users/delete_template.html', context)