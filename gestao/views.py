from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Fiscal, Empresa, GestaoContrato
from .forms import FiscalForm, EmpresaForm, GestaoContratoForm


@login_required
def home(request):
    context = {'mensagem': 'Olá mundo! - #### Home-Page ###'}
    return render(request, 'base.html', context)


@login_required
def lista_fiscais(request):
    fiscais = Fiscal.objects.all()
    form = FiscalForm()
    data = {'fiscais': fiscais, 'form': form}
    return render(request, 'gestao/lista_fiscais.html', data)


@login_required
def fiscal_novo(request):
    form = FiscalForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('gestao_lista_fiscais')


@login_required
def fiscal_update(request, id):
    data = {}
    fiscal = Fiscal.objects.get(id=id)
    form = FiscalForm(request.POST or None, instance=fiscal)
    data ['fiscal'] = fiscal
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('gestao_lista_fiscais')
    else:
        return render(request, 'gestao/update_fiscal.html', data)

@login_required
def fiscal_delete(request, id):
    fiscal = Fiscal.objects.get(id=id)
    if request.method == 'POST':
        fiscal.delete()
        return redirect ('gestao_fiscal_delete')
    else:
        return render(request, 'gestao/delete_confirm.html', {'fiscal': fiscal})


@login_required
def lista_empresas(request):
    empresas = Empresa.objects.all()
    form = EmpresaForm()
    data = {'empresa': empresas, 'form': form}
    return render(request, 'gestao/lista_empresas.html', data)


@login_required
def empresa_novo(request):
    form = EmpresaForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('gestao_lista_empresas')


@login_required
def empresa_update(request, id):
    data = {}
    empresa = Empresa.objects.get(id=id)
    form = EmpresaForm(request.POST or None, instance=empresa)
    data ['empresa'] = empresa
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('gestao_lista_empresas')
    else:
        return render(request, 'gestao/update_empresa.html', data)


@login_required
def empresa_delete(request, id):
    empresa = empresa.objects.get(id=id)
    if request.method == 'POST':
        empresa.delete()
        return redirect ('gestao_empresa_delete')
    else:
        return render(request, 'gestao/delete_confirm.html', {'obj': empresa})


@login_required
def lista_contratos(request):
    contratos = GestaoContrato.objects.all()
    form = GestaoContratoForm()
    data = {'contratos': contratos, 'form': form}
    return render(request, 'gestao/lista_contratos.html', data)


@login_required
def contrato_novo(request):
    form = GestaoContratoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect ('gestao_lista_contratos')


@login_required
def contrato_update(request, id):
    data = {}
    contrato = GestaoContrato.objects.get(id=id)
    form = GestaoContratoForm(request.POST or None, instance=contrato)
    data ['contratada'] = contrato
    data ['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect ('gestao_lista_contratos')
    else:
        return render(request, 'gestao/update_contrato.html', data)


@login_required
def contrato_delete(request, id):
    contrato = contrato.objects.get(id=id)
    if request.method == 'POST':
        contrato.delete()
        return redirect ('gestao_contrato_delete')
    else:
        return render(request, 'gestao/delete_confirm.html', {'obj': contrato})


#TODO: Ver se eu vou trabalhar com VIEWS ou com o ADMIN