# Generated by Django 4.0.3 on 2022-11-28 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboardapp', '0004_leadbuyer_mrp'),
    ]

    operations = [
        migrations.CreateModel(
            name='DMLdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sr_No', models.CharField(max_length=50)),
                ('Status', models.TextField()),
                ('Idea_No', models.CharField(max_length=100)),
                ('Idea_for', models.TextField()),
                ('DML_days', models.TextField()),
                ('DML_recieve', models.TextField()),
                ('Model', models.CharField(max_length=50)),
                ('DML_no', models.CharField(max_length=150)),
                ('DML_description', models.CharField(max_length=100)),
                ('S_no', models.FloatField()),
                ('Added_PartNo', models.CharField(max_length=50)),
                ('Deleted_Partno', models.CharField(max_length=100)),
                ('C_S', models.CharField(max_length=50)),
                ('Rev', models.CharField(max_length=50)),
                ('Qty', models.CharField(max_length=50)),
                ('DML_Remarks', models.TextField()),
                ('VC_no', models.CharField(max_length=50)),
                ('Description', models.TextField()),
                ('Added_PartStatus', models.TextField()),
                ('Deleted_PartStatus', models.TextField()),
                ('AddedPart_BuyerName', models.TextField()),
                ('DeletedPart_BuyerName', models.TextField()),
                ('DeletedPart_Department', models.TextField()),
                ('AddedPart_Vendor', models.TextField()),
                ('DeletedPart_Vendor', models.TextField()),
                ('Added_partSOB', models.TextField()),
                ('AddedPart_str_loc', models.CharField(max_length=50)),
                ('Deleted_partSOB', models.TextField()),
                ('DeletedPart_str_loc', models.TextField()),
                ('AddedPart_Map', models.CharField(max_length=50)),
                ('DeletedPart_Map', models.CharField(max_length=50)),
                ('AddedPart_Bulk', models.CharField(max_length=50)),
                ('DeletedPart_Bulk', models.CharField(max_length=100)),
                ('Difference', models.CharField(max_length=100)),
                ('MailShareToTeam', models.CharField(max_length=50)),
                ('PrimaryStock_Recieved', models.CharField(max_length=50)),
                ('Trail_On', models.CharField(max_length=100)),
                ('FinalStock_communication', models.CharField(max_length=50)),
                ('Implemented_On', models.CharField(max_length=100)),
            ],
        ),
    ]
