from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path(r'gestao/', include('gestao.urls')), #URL home da app ^Começa e $Termina
    path('admin/', admin.site.urls),
    
]

admin.site.site_header = "Gestão SEAD-PV"
admin.site.index_title = "Gestão Financeira e Orçamentária SEAD-PV"
admin.site.site_title = "teste" #Complemento do título