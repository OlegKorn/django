from django.shortcuts import render
from .getsearch import Search_


def get_search(request):
    
    if request.GET:

        root = request.GET.get("root")
        property_type = request.GET.get("property_type") 
        url = str(root) + str(property_type)
        
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
              'data'           : 'NONE',
              'root'           : root,
              'property_type'  : property_type
            }

    return render(request, 'search/search.html', context) 


