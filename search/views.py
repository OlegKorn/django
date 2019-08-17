from django.shortcuts import render
from .getsearch import Search_


def get_search(request):
    
    if request.GET:

        url = request.GET.get("url")
        num = request.GET.get("num") 
        url2 = str(url) + str(num)
        
        print('------------------URL IS: ', url2)
        
        s = Search_(url2)
        s.get_soup()
        print(s.all_data)
        print(s.no_records_found())

        if not s.no_records_found():
            s.get_data()
            context = {
              'data' : s.all_data,
              'url' : url,
              'num'  : num
            }

        if s.no_records_found():
            context = {
              'data' : 'Nothing foundNothing found',
              'url' : url,
              'num'  : num
            }

    return render(request, 'search/search.html', context)
    


