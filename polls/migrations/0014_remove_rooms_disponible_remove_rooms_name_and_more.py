# Generated by Django 4.2.1 on 2023-06-04 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_alter_clientes_citizenship_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rooms',
            name='disponible',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='name',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='price',
        ),
        migrations.AddField(
            model_name='rooms',
            name='espacio',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rooms',
            name='habitacion',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='clientes',
            name='citizenship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.ciudadania'),
        ),
        migrations.AlterField(
            model_name='clientes',
            name='objeto_arrendamiento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.rooms'),
        ),
    ]
