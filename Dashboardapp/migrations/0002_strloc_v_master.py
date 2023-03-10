# Generated by Django 4.0.3 on 2022-11-28 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboardapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrLoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ProcType', models.TextField()),
                ('SPT', models.TextField()),
                ('Material', models.TextField()),
                ('Issue_SL', models.CharField(max_length=150)),
                ('EP_SL', models.CharField(max_length=100)),
                ('Mard_SL', models.CharField(max_length=100)),
                ('In_qual_insp', models.FloatField(max_length=100)),
                ('Unrestricted', models.CharField(blank=True, max_length=100, null=True)),
                ('Bun', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='V_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vendor', models.CharField(blank=True, max_length=100, null=True)),
                ('Vendor_Desciption', models.TextField(blank=True, max_length=150, null=True)),
                ('name_3', models.CharField(blank=True, max_length=100, null=True)),
                ('name_4', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.TextField()),
                ('Postal_Code', models.CharField(blank=True, max_length=100, null=True)),
                ('State', models.TextField()),
                ('Recovery', models.TextField()),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
