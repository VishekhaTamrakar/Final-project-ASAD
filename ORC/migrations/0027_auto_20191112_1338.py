# Generated by Django 2.1.5 on 2019-11-12 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ORC', '0026_auto_20191112_1331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenancework',
            name='property_building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mw5', to='ORC.PropertyLocation'),
        ),
    ]
