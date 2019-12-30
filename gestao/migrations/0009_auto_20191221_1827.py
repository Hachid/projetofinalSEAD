# Generated by Django 3.0.1 on 2019-12-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao', '0008_auto_20191220_1151'),
    ]

    operations = [
        migrations.CreateModel(
            name='orcamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
                ('natureza', models.CharField(max_length=50)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=14)),
            ],
        ),
        migrations.RenameField(
            model_name='rubrica',
            old_name='saldo_disponivel',
            new_name='saldo_reservado',
        ),
        migrations.RenameField(
            model_name='rubrica',
            old_name='saldo_empenhado',
            new_name='valorDisponRubrica_empenhado',
        ),
        migrations.RenameField(
            model_name='rubrica',
            old_name='saldo_total',
            new_name='valorRubrica',
        ),
        migrations.AddField(
            model_name='rubrica',
            name='obsReserva',
            field=models.TextField(default=1, verbose_name='Observação da reserva'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gestaocontrato',
            name='totalNota',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total da Nota'),
        ),
        migrations.AlterField(
            model_name='gestaocontrato',
            name='totalPago',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Pago'),
        ),
    ]