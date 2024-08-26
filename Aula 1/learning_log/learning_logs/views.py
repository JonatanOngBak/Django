from django.shortcuts import render

def index(request):
    """pagina principla do learning_log"""
    return render(request, 'learning_logs/index.html')
