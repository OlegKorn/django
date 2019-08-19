from django.shortcuts import render
from .getsearch import Search_, OnePage
from django.core.paginator import Paginator


def get_search(request):
    
    if request.GET:

        root = request.GET.get("root")
        property_type_radio = request.GET.get("property_type_radio") 
        url = str(root) + str(property_type_radio)
        print('--URL IS--: ', url)
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
                
                paginator = Paginator(s.all_data, 15) # Show 25 contacts per page
                page = request.GET.get('page') 
                contacts = paginator.get_page(page)

                print(contacts, '15', len(s.all_data))

                context = {
                  'data'                 : s.all_data,
                  'property_type_radio'  : property_type_radio,
                  'url'                  : url,
                  'contacts'             : contacts
                }
        
        if not s.records_found(): # если нет записей в рубрике     
            message = 'Sorry, no records were found in ' + url
            context = {
              'data'                 : message,
              'property_type_radio'  : property_type_radio,
              'url'                  : url
            }

    return render(request, 'search/search.html', context) 


