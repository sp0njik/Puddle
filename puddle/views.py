from django.shortcuts import render

from item.models import Category, Item
from puddle.forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'puddle/index.html', {'categories': categories,'items': items})


def contact(request):
    return render(request, 'puddle/contact.html')


def signup(request):
    form = SignupForm()
    return render(request, 'puddle/signup.html', {'form': form})