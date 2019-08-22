from django.shortcuts import render
from .getsearch import Search_, OnePage
from django.core.paginator import Paginator


def get_search(request):
    
    if request.method == 'GET':

        type_ = request.GET["type"]
        s = Search_()
        url = s.set_url(type_)
        print(url)
        s.get_soup()
        
        if s.records_found(): # если есть записи в рубрике

            if s.only_one_page_found(): # если лишь одна страница объявлений
                # создаем объект OnePage()
                o = OnePage()
                o.main()

                paginator = Paginator(o.all_data, 5) 
                page_number = request.GET.get('page')
                pagination = paginator.get_page(page_number)

                context = {
                  #'data'                 : o.all_data,
                  'property_type_radio'  : type_,
                  'url'                  : url,
                  'pagination'           : pagination,
                }

            if not s.only_one_page_found(): # если больше одной страницы объявлений               
                s.get_url_digits()
                s.main()

                paginator = Paginator(s.all_data, 4) 
                page_number = request.GET.get('page')
                pagination = paginator.get_page(page_number)

                context = {
                  'property_type_radio'  : type_,
                  'url'                  : url,
                  'pagination'           : pagination,
                }
        
        if not s.records_found(): # если нет записей в рубрике     
            context = {
              'url'                      : url
            }
    

    return render(request, 'search/search.html', context) 


