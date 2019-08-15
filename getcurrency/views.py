from django.shortcuts import render
from .currency import Currency_ 


def get_currency(request):
    
    c = Currency_()
    c.get_soup()
    all = c.get_list_of_all()
    
    context = {
        'all' : all, 
    }

    return render(
        request, 
        'getcurrency/currency.html', 
        context        
    )
