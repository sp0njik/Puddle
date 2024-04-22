from django.shortcuts import render

def index(request):
    return render(request, 'puddle/index.html')


def contact(request):
    return render(request, 'puddle/contact.html')