from django.shortcuts import render
from django.http import JsonResponse

from .services.groq_service import ask_groq


def home(request):
    return render(request, "chatbot/chat.html")


def chat_api(request):

    if request.method == "POST":

        message = request.POST.get("message")

        if not message:
            return JsonResponse(
                {"error": "Message vide"},
                status=400
            )

        try:
            answer = ask_groq(message)

            return JsonResponse({
                "answer": answer
            })

        except Exception as e:
            return JsonResponse({
                "error": str(e)
            }, status=500)

    return JsonResponse({
        "error": "Méthode non autorisée"
    }, status=405)