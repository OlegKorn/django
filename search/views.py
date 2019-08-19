from django.shortcuts import render
from .getsearch import Search_, OnePage


def get_search(request):
    
    if request.GET:

        root = request.GET.get("root")
        property_type_radio = request.GET.get("property_type_radio") 
        url = str(root) + str(property_type_radio)

        s = Search_(url)
        s.get_soup()
        
        if s.records_found(): # если есть записи в рубрике

            if s.only_one_page_found(): # если лишь одна страница объявлений
                # создаем объект OnePage()
                o = OnePage()
                o.main()
                context = {
                  'data'                 : o.all_data,
                  'property_type_radio'  : property_type_radio,
                  'url'                  : url
                }

            if not s.only_one_page_found(): # если больше одной страницы объявлений               
                s.get_url_digits()
                s.main()

                print(len(s.all_data))

                context = {
                  'data'                 : s.all_data,
                  'property_type_radio'  : property_type_radio,
                  'url'                  : url
                }
        
        if not s.records_found(): # если нет записей в рубрике     
            context = {
              'url'                      : url
            }

    return render(request, 'search/search.html', context) 


