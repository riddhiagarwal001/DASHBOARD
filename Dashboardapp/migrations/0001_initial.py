# Generated by Django 4.0.3 on 2022-11-28 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VC_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vc_number', models.CharField(blank=True, max_length=100, null=True)),
                ('model', models.CharField(blank=True, max_length=250, null=True)),
                ('Type_of_vehicle', models.CharField(max_length=150)),
                ('sub_model_group', models.CharField(max_length=150)),
                ('Dom_Exp', models.CharField(max_length=100)),
            ],
        ),
    ]
