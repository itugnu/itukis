from django.shortcuts import render
from web.models import WebApplication
from pages.models import Page
from django.http import Http404

def index(request):
    """Home Page."""
    data = {"settings": None}
    settings = WebApplication.objects.all()
    if settings.count():
        data["settings"] = settings[0]
    return render(request, 'web/index.html', data)

def page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404
    data = {'page': page}
    return render(request, 'web/page.html', data)
