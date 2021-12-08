from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Googlxy")


from django.shortcuts import render

# from .models import Question
from .forms import GooglaxyForm

def index(request):
    question = ""
    response = ""
    form = GooglaxyForm()

    if request.method == 'POST':
        form = GooglaxyForm(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            # if question:
            #     response = Question.objects.order_by('-pub_date')[:5]
    context = {
        'question': question,
        'response': response,
        'form': form
    }
    print(context)
    return render(request, 'currency/index.html', context)
