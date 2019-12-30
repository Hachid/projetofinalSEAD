from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(r'gestao/', include('gestao.urls')), #URL home da app ^Começa e $Termina
    path('admin/', admin.site.urls),
    
]
