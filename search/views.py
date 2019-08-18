from django.shortcuts import render
from .getsearch import Search_


def get_search(request):
    
    if request.GET:

        root = request.GET.get("url")
        num = request.GET.get("num") 
        url = str(root) + str(num)
        
        print('------------------URL IS: ', url)
        
        s = Search_(url)
        s.get_soup()

        if not s.no_records_found():
            s.main()
            context = {
              'data' : s.all_data,
              'url'  : url,
              'num'  : num
            }
        
        if s.no_records_found():
            context = {
              'data' : 'NONE',
              'url'  : url,
              'num'  : num
            }

    return render(request, 'search/search.html', context) 


