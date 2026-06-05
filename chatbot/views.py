from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from .models import Conversation, Message
from .services.groq_service import ask_groq

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    # Ensure there is a conversation for the user; get latest or create
    conversation, created = Conversation.objects.get_or_create(user=request.user)
    return render(request, "chatbot/chat.html")


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def chat_api(request):
    if request.method == "POST":
        message = request.POST.get("message")
        if not message:
            return JsonResponse({"error": "Message vide"}, status=400)
        # Get or create conversation for the user
        conversation, created = Conversation.objects.get_or_create(user=request.user)
        # Save user message
        Message.objects.create(conversation=conversation, content=message, is_user=True)
        try:
            answer = ask_groq(message)
            # Save bot response
            Message.objects.create(conversation=conversation, content=answer, is_user=False)
            return JsonResponse({"answer": answer})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
    return JsonResponse({"error": "Méthode non autorisée"}, status=405)