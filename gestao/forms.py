from django.forms import ModelForm
from .models import Fiscal, Empresa, GestaoContrato


class FiscalForm(ModelForm):
    class Meta:
        model = Fiscal
        fields = '__all__'


class EmpresaForm(ModelForm):
    class Meta:
        model = Empresa
        fields = '__all__'


class GestaoContratoForm(ModelForm):
    class Meta:
        model = GestaoContrato
        fields = '__all__'
