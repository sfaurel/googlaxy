from django.shortcuts import render
# from django.http import HttpResponse

from .models import Items, Numerals
from .forms import GooglaxyForm, AddItemForm, AddNumeralForm
from .utils.GalacticInterpreter import GalacticInterpreter


def index(request):
    question = ""
    response = ""
    form = GooglaxyForm()

    if request.method == 'POST':
        form = GooglaxyForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            if question:
                response = GalacticInterpreter.interpretateEntry(question)
    context = {
        'question': question,
        'response': response,
        'form': form
    }
    return render(request, 'currency/index.html', context)


def settings(request):
    return render(request, 'settings/index.html')


def itemsSettings(request):
    form = AddItemForm()
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = Items(name=form.cleaned_data['name'],
                         price=form.cleaned_data['price'])
            item.save()
    itemsData = Items.objects.all()
    context = {
        'itemsData': itemsData,
        'form': form
    }
    return render(request, 'settings/items.html', context)


def numeralsSettings(request):
    form = AddNumeralForm()
    if request.method == 'POST':
        form = AddNumeralForm(request.POST)
        if form.is_valid():
            item = Numerals(name=form.cleaned_data['name'],
                            roman=form.cleaned_data['roman'])
            item.save()
    numeralsData = Numerals.objects.all()
    context = {
        'itemsData': numeralsData,
        'form': form
    }
    return render(request, 'settings/numerals.html', context)
