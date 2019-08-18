from django.shortcuts import render
from .getsearch import Search_


def get_search(request):
    
    if request.GET:

        root = request.GET.get("root")
        property_type_input = request.GET.get("property_type_input") 
        url = str(root) + str(property_type_input)
        
        print('------------------URL IS: ', url)
        
        s = Search_(url)
        s.get_soup()

        if not s.no_records_found():
            s.main()
            context = {
              'data'                 : s.all_data,
              'property_type_input'  : property_type_input,
              'url'                  : url
            }
        
        if s.no_records_found():
            context = {
              'data'                 : 'NONE',
              'url'                  : url,
              'property_type_input'  : property_type_input
            }

    return render(request, 'search/search.html', context) 


