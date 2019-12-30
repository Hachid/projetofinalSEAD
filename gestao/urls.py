from django.conf.urls import url
from django.urls import include, path
from .views import (
home,
lista_fiscais, 
fiscal_novo,
fiscal_update,
fiscal_delete,
lista_empresas,
empresa_novo,
empresa_update,
empresa_delete,
lista_contratos,
contrato_novo,
contrato_update,
contrato_delete
)

urlpatterns = [
    path(r'', home, name='gestao'),
    path(r'fiscais', lista_fiscais, name='gestao_lista_fiscais'),
    path(r'fiscais-novo', fiscal_novo, name='gestao_fiscal_novo'),
    #path(r'fiscais-update/(?P<id>\d+)/$', fiscal_update, name='gestao_fiscal_update'),
    #path(r'fiscais-delete/(?P<id>\d+)/$', fiscal_delete, name='gestao_fiscal_delete'),
    
    path(r'empresas', lista_empresas, name='gestao_lista_empresas'),
    path(r'empresas-novo', empresa_novo, name='gestao_empresa_novo'),
    #path(r'empresas-update/(?P<id>\d+)/$', empresa_update, name='gestao_empresa_update'),
    #path(r'empresas-delete/(?P<id>\d+)/$', empresa_delete, name='gestao_empresa_delete'),
    
    path(r'contratos', lista_contratos, name='gestao_lista_contratos'),
    path(r'contratos-novo', contrato_novo, name='gestao_contrato_novo'),
    #path(r'contratos-update/(?P<id>\d+)/$', contrato_update, name='gestao_contrato_update'),
    #path(r'contratos-delete/(?P<id>\d+)/$', contrato_delete, name='gestao_contratos_delete'),

    #URL dispensas
    #URL rubricas
    

]

