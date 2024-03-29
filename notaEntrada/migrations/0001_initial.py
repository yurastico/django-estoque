# Generated by Django 2.2.4 on 2019-10-18 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotasEntradas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField(default=0, verbose_name='Quantidade')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('criado', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modificado', models.DateTimeField(auto_now=True, verbose_name='Modificado')),
                ('produto', models.ForeignKey(on_delete='protect', to='produto.Produtos')),
            ],
        ),
    ]
