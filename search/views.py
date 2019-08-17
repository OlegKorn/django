from django.shortcuts import render
from .getsearch import Search_


def get_search(request):
    
    if request.method == "GET":

        site = request.GET.get("site")
        estatetype = request.GET.get("estatetype") 
        
        #url = request.GET.get("url")
        print(site, estatetype)

        #num = request.GET.get("num")

        '''s = Search_()
        print(s)
        s.get_soup(url)
        print(s.return_soup())'''

        
        context = {
          'site'       : site,
          'estatetype' : estatetype,
        }

    return render(request, 'search/search.html', context)
    


