from django.shortcuts import render
from . models import Page

# Create your views here.

def index(request, pagename):
    pagename = '/'+pagename
    pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
    }
    # assert False
    return render(request, 'pages/page.html', context)