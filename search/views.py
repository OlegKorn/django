from django.shortcuts import render


def get_test(request):
    
    if request.GET:
        
        url = request.GET.get("url")
        num = request.GET.get("num")

        context = {
          'url' : url,
          'num' : num,
        }
        print('TEST', url, num)

    return render(request, 'search/search.html', context)
