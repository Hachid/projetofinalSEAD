from django.db import models
from datetime import date
import decimal
import operator
import math

class Fiscal(models.Model):
    fiscal = models.CharField(max_length=50, blank=True, null=True)
    siape = models.CharField(max_length=7, blank=True, null=True)
    portaria = models.CharField(max_length=10, blank=True, null=True)
    setor = models.CharField(max_length=7, blank=True, null=True)
    email = models.EmailField(("E-mail do Fiscal"), max_length=254)
    ramal = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        verbose_name_plural= "Cadastro de Fiscais"

    def __str__(self):
        return self.fiscal


class Empresa(models.Model):
    empresa = models.CharField(verbose_name=("Empresa"), max_length=80, blank=False, null=False)
    cnpj_Empresa = models.CharField(max_length=18, blank=True, null=True)
    processoRaiz = models.CharField(verbose_name=("Processo Raiz"), max_length=20, blank=False, null=False)
    contrato = models.CharField(max_length=9, blank=True, null=True)
    objeto = models.CharField(max_length=50, blank=True, null=True)
    valor_contratual = models.DecimalField( max_digits=14, decimal_places=2)
    saldo_utilizado = models.DecimalField( max_digits=14, decimal_places=2)
    dataAssinatura = models.DateField(("data de assinatura"), auto_now=False, auto_now_add=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(("E-mail"), max_length=254)
    Nomfiscal = models.ForeignKey('Fiscal',verbose_name=("Fiscal"), related_name='Fiscal', on_delete=models.CASCADE)
    #fiscal = models.ForeignKey('Fiscal', verbose_name=("Fiscal"), on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural= "Cadastro de Empresas"

    def __str__(self):
        return self.empresa

    def saldoDisponivel(self):
        return (self.valor_contratual - self.saldo_utilizado)
    
    def vigencia(self):
        hoje = date.today()
        assinatura = self.dataAssinatura
        futuro = (date.fromordinal(assinatura.toordinal()+365))
        renova = (futuro.toordinal() - hoje.toordinal())
        return renova

class GestaoContrato (models.Model):
    empresa = models.ForeignKey('empresa', verbose_name=("Empresa"), on_delete=models.CASCADE)
    #contrato = models.ForeignKey('contrato', verbose_name=("contrato"), on_delete=models.CASCADE)#número do contrato ***/****
    processoSei = models.CharField(max_length=20, blank=False, null=False)#processo SEI *****.******/****-**
    numNota = models.CharField(max_length=20, blank=False, null=False)#Número da Nota ou Fatura
    mesCompetencia = models.CharField(max_length=8, blank=False, null=False)#Competência da execução do serviço **/****
    emissNota = models.DateField(("data de emissão da nota"), auto_now=False, auto_now_add=False)
    recebido_nota = models.DateField(("data de recebimento"), auto_now=False, auto_now_add=False)
    atesteNota = models.DateField(("data de ateste"), auto_now=False, auto_now_add=False)
    totalNota = models.DecimalField(verbose_name="Total da Nota", max_digits=10, decimal_places=2)
    totalPago = models.DecimalField(verbose_name=("Total Pago"),max_digits=10, decimal_places=2)
    obs = models.TextField(("Observações"))

    class Meta:
        verbose_name_plural= "Gestão de Contratos"

    def __str__(self):
        return str(self.empresa)


class Orcamento(models.Model):
    codigo = models.CharField(verbose_name=("Código da despesa"), max_length=6, blank=False, null=False)
    natureza= models.CharField(verbose_name=("Descrição da despesa"), max_length=50, blank=False, null=False)
    tipo = models.CharField(verbose_name=("Tipo"), max_length=20, blank=False, null=False)
    funcao = models.TextField(("Função da despesa"))
    valor = models.DecimalField(verbose_name=("Valor orçamentário"), max_digits=14, decimal_places=2)

    class Meta:
        verbose_name_plural= "Gestão Orçamentária"


    def __str__(self):
        return str(self.codigo)


class Rubrica (models.Model):
    codigoDesp = models.ForeignKey('Orcamento', verbose_name=("Código da despesa"), on_delete=models.CASCADE)
    subelemento = models.CharField(verbose_name=("Subelemento "), max_length=2, blank=False, null=False)#sub elemento
    descricao = models.CharField(verbose_name=("Descrição"), max_length=70, blank=False, null=False)#Definição do sub elemento
    valorRubrica = models.DecimalField(verbose_name=("Valor da rubrica"), max_digits=10, decimal_places=2)
    #saldo_reservado = models.DecimalField(max_digits=10, decimal_places=2)#valor solicitado, mas não empenhado
    #obsReserva = models.TextField(("Observação da reserva"))
    #valorDisponRubrica = models.DecimalField(max_digits=10, decimal_places=2)
    

    class Meta:
        verbose_name_plural= "Gestão de Rubricas"