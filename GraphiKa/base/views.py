from django.shortcuts import render, redirect
from django.http import JsonResponse

from . import translator


def home(request):
    translation = None

    if request.method == 'POST':
        input_text = request.POST.get('long_text', '')
        model_name = request.POST.get('model', '')
        MY_API_KEY = request.POST.get('hugging_face_token', '')
        translation = translator.generate(input_text, model_name, MY_API_KEY, False)  # Your summarization code here
    
    return render(request, "base/home.html", context={'translation': translation})