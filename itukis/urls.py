from django.conf.urls import url, include
from django.contrib import admin
from web import views as webclient

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^(?P<slug>\w+)$', webclient.index, name='page'),
    url(r'^$', webclient.index, name='index'),
]
