from django.contrib import admin
from .models import Empresa, Fiscal, GestaoContrato, Orcamento, Rubrica


class EmpresaAdmin(admin.ModelAdmin):
        fieldsets =[
            ('Dados da Empresa', {'fields':
                  [('empresa', 'cnpj_Empresa'), ('telefone', 'email')]
            }),
            ('Dados do Contrato', {'fields':
                   [('processoRaiz','objeto'), ('contrato', 'dataAssinatura'),
                    ('valor_contratual', 'saldo_utilizado')]
            }),
            ('Dados da Fiscalização',  {'fields':
                    ['Nomfiscal']
            }),
        ]

        raw_id_fields = ['Nomfiscal']

        #list_filter = ['Nomfiscal'] #Filtro Lateral
        list_display = (
            'empresa',  'objeto', 'Nomfiscal', 'contrato',
            'valor_contratual', 'saldo_utilizado', 'saldoDisponivel',
            'dataAssinatura',  'vigencia', 'processoRaiz'
        )
        search_fields = ('empresa', 'objeto', 'Nomfiscal')#defeito
        autocomplete_fields = ['Nomfiscal']

        #se eu quiser colocar no grid o fiscal que é de outra classe.
        #coloco essa função depois no nome da função no display 'fiscal'
        def fiscal (self, obj):
            return obj.fiscal



class FiscalAdmin(admin.ModelAdmin):
        list_display = ('fiscal', 'siape', 'portaria',
        'setor', 'email', 'ramal')
        search_fields = ('siape', 'fiscal')
        
        def empresa (self, obj):
                return obj.empresa


class GestaoContratoAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'processoSei', 'numNota', 
    'mesCompetencia', 'recebido_nota', 'atesteNota','totalNota',
    'totalPago', 'obs')

class OrcamentoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'tipo', 'natureza', 'valor')
    search_fields = ('codigo', 'tipo', 'natureza')


class RubricaAdmin(admin.ModelAdmin):
    list_display = ('codigoDesp', 'subelemento', 'descricao',
                    'valorRubrica')
    search_fields = ('codigoDesp', 'subelemento', 'descricao')


    def codigo(self, obj):
        return obj.codigo

admin.site.register(Empresa, EmpresaAdmin)
admin.site.register(Fiscal, FiscalAdmin)
admin.site.register(GestaoContrato, GestaoContratoAdmin)
admin.site.register(Orcamento, OrcamentoAdmin)
admin.site.register(Rubrica, RubricaAdmin)
