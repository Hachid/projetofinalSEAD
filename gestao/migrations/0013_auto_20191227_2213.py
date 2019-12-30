# Generated by Django 3.0.1 on 2019-12-28 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0012_auto_20191221_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rubrica',
            name='codigoDesp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestao.Orcamento', verbose_name='Código da despesa'),
        ),
        migrations.AlterField(
            model_name='rubrica',
            name='descricao',
            field=models.CharField(max_length=70, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='rubrica',
            name='subelemento',
            field=models.CharField(max_length=2, verbose_name='Subelemento '),
        ),
        migrations.AlterField(
            model_name='rubrica',
            name='valorRubrica',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor da rubrica'),
        ),
    ]