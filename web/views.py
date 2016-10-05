from django.shortcuts import render
from pages.models import Page
from django.http import Http404

def index(request):
    """Home Page."""
    return render(request, 'web/index.html', {})

def page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
    except Page.DoesNotExist:
        raise Http404
    data = {'page': page}
    return render(request, 'web/page.html', data)
