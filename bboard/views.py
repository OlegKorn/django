from django.http import HttpResponse
from .models import Bb

def index(request):
    s = 'List of ads\r\n\r\n\r\n'
   
    for bboard in Bb.objects.order_by('-published'):    #   - in -published is for descending sort
        s += bboard.title + '\r\n' + bboard.content + '\r\n\r\n'

    return HttpResponse(s, content_type = 'text/plain; charset=utf-8')