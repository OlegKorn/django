from django.shortcuts import render
from .currency import Currency_
from bboard.models import Rubric


def get_currency(request):
    
    c = Currency_()
    c.get_soup()
    all = c.get_list_of_all()
    
    rubrics = Rubric.objects.all()

    context = {
        'all' : all, 
        'rubrics' : rubrics,
    }

    return render(
        request, 
        'getcurrency/currency.html', 
        context        
    )
