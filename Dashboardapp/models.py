from django.db import models

# Create your models here.
class VC_Master(models.Model):
    VC=models.TextField(max_length=100,blank=True,primary_key=True)
    Models=models.TextField(max_length=250,blank=True,null=True)
    Type_of_vehicle=models.TextField(max_length=150)
    sub_model_group=models.TextField(max_length=150)
    Dom_Exp=models.TextField(max_length=100)

class V_master(models.Model):
    Vendor=models.CharField(max_length=100,blank=True, primary_key=True)  
    Vendor_Desciption=models.TextField(max_length=150,null=True,blank=True)
    name_3=models.CharField(max_length=100,blank=True,null=True)
    name_4=models.CharField(max_length=100,null=True,blank=True)
    City=models.TextField()
    Postal_Code=models.CharField(max_length=100,null=True,blank=True)
    State=models.TextField()
    Recovery=models.TextField()
    Email=models.CharField(max_length=100,blank=True, null=True)

class StrLoc(models.Model):
    ProcType=models.TextField(max_length=100,blank=True,primary_key=True)
    SPT=models.TextField()
    Material=models.TextField()
    Issue_SL=models.CharField(max_length=150)
    EP_SL=models.CharField(max_length=100)
    Mard_SL=models.CharField(max_length=100)
    In_qual_insp=models.FloatField(max_length=100)
    Unrestricted=models.CharField(max_length=100,blank=True,null=True)
    Bun=models.CharField(max_length=100)

class MAP(models.Model):
    Material=models.TextField(max_length=100,blank=True,primary_key=True)
    Valuation_Type=models.CharField(max_length=150,null=True,blank=True)
    Price=models.FloatField(max_length=100)
    Last_Change=models.DateTimeField()

class Part_Master(models.Model):
    Part_Vendor=models.CharField(max_length=100,blank=True,primary_key=True)
    Material=models.TextField()
    Material_description=models.TextField()
    Vendor_Code= models.CharField(max_length=50,blank=True, null=True)
    Vendor_description=models.TextField()
    Quota_Valid_from=models.DateField()
    Quota_Valid_to=models.DateField()
    Quota_percentage=models.CharField(max_length=50)
    Quota_number= models.CharField(max_length=50,blank=True, null=True)
    Proctype=models.TextField()
    Spl_Proc_Type=models.TextField()
    Bulk_Ind=models.CharField(max_length=100)
    MRP_Cntrl=models.CharField(max_length=50)
    Buyer=models.CharField(max_length=50)
    Lead_Buyer=models.CharField(max_length=50)
    Department=models.CharField(max_length=100)
    Bulk_Part=models.TextField()
    Str_loc=models.TextField()
    Vendor_location=models.TextField()
    Vendor_state=models.TextField()

class MRP(models.Model):
    MRPCn=models.CharField(max_length=50,primary_key=True)
    New_Description=models.CharField(max_length=100,blank=True, null=True)
    Name=models.TextField()
    Group_Lead=models.TextField()



class DMLdetails(models.Model):
    sr_no = models.BigIntegerField(db_column='Sr_No', primary_key=True)  # Field name made lowercase.
    status = models.TextField(db_column='Status', blank=True, null=True)  # Field name made lowercase.
    idea_no = models.TextField(db_column='Idea_No', blank=True, null=True)  # Field name made lowercase.
    idea_for = models.TextField(db_column='Idea_for', blank=True, null=True)  # Field name made lowercase.
    dml_days = models.BigIntegerField(db_column='DML_days', blank=True, null=True)  # Field name made lowercase.
    dml_recieve = models.DateTimeField(db_column='DML_recieve', blank=True, null=True)  # Field name made lowercase.
    model = models.TextField(db_column='Model', blank=True, null=True)  # Field name made lowercase.
    dml_no = models.TextField(db_column='DML_no', blank=True, null=True)  # Field name made lowercase.
    dml_description = models.TextField(db_column='DML_description', blank=True, null=True)  # Field name made lowercase.
    s_no = models.TextField(db_column='S_no', blank=True, null=True)  # Field name made lowercase.
    added_partno = models.TextField(db_column='Added_PartNo', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(db_column='Description', blank=True, null=True)  # Field name made lowercase.
    c_s = models.TextField(db_column='C_S', blank=True, null=True)  # Field name made lowercase.
    rev = models.TextField(db_column='Rev', blank=True, null=True)  # Field name made lowercase.
    qty = models.TextField(db_column='Qty', blank=True, null=True)  # Field name made lowercase.
    deleted_partno = models.TextField(db_column='Deleted_Partno', blank=True, null=True)  # Field name made lowercase.
    description_1 = models.TextField(db_column='Description_1', blank=True, null=True)  # Field name made lowercase.
    c_s_1 = models.TextField(blank=True, null=True)
    rev_1 = models.TextField(blank=True, null=True)
    qty_1 = models.TextField(blank=True, null=True)
    dml_remarks = models.TextField(db_column='DML_Remarks', blank=True, null=True)  # Field name made lowercase.
    vc_no = models.TextField(db_column='VC_no', blank=True, null=True)  # Field name made lowercase.
    description_2 = models.TextField(db_column='Description_2', blank=True, null=True)  # Field name made lowercase.
    added_partstatus = models.TextField(db_column='Added_PartStatus', blank=True, null=True)  # Field name made lowercase.
    deleted_partstatus = models.TextField(db_column='Deleted_PartStatus', blank=True, null=True)  # Field name made lowercase.
    addedpart_buyername = models.TextField(db_column='AddedPart_BuyerName', blank=True, null=True)  # Field name made lowercase.
    deletedpart_buyername = models.TextField(db_column='DeletedPart_BuyerName', blank=True, null=True)  # Field name made lowercase.
    deletedpart_department = models.TextField(db_column='DeletedPart_Department', blank=True, null=True)  # Field name made lowercase.
    addedpart_vendor = models.TextField(db_column='AddedPart_Vendor', blank=True, null=True)  # Field name made lowercase.
    deletedpart_vendor = models.TextField(db_column='DeletedPart_Vendor', blank=True, null=True)  # Field name made lowercase.
    added_partsob = models.TextField(db_column='Added_partSOB', blank=True, null=True)  # Field name made lowercase.
    addedpart_str_loc = models.TextField(db_column='AddedPart_str_loc', blank=True, null=True)  # Field name made lowercase.
    deleted_partsob = models.TextField(db_column='Deleted_partSOB', blank=True, null=True)  # Field name made lowercase.
    deletedpart_str_loc = models.TextField(db_column='DeletedPart_str_loc', blank=True, null=True)  # Field name made lowercase.
    addedpart_map = models.TextField(db_column='AddedPart_Map', blank=True, null=True)  # Field name made lowercase. This field type is a guess.    
    deletedpart_map = models.TextField(db_column='DeletedPart_Map', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    addedpart_bulk = models.TextField(db_column='AddedPart_Bulk', blank=True, null=True)  # Field name made lowercase.
    deletedpart_bulk = models.TextField(db_column='DeletedPart_Bulk', blank=True, null=True)  # Field name made lowercase.
    difference = models.TextField(db_column='Difference', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mailsharetoteam = models.DateTimeField(db_column='MailShareToTeam', blank=True, null=True)  # Field name made lowercase.
    primarystock_recieved_field = models.TextField(db_column='PrimaryStock_Recieved ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    trail_on = models.TextField(db_column='Trail_On', blank=True, null=True)  # Field name made lowercase.
    finalstock_communication = models.TextField(db_column='FinalStock_communication', blank=True, null=True)  # Field name made lowercase.
    implemented_on = models.TextField(db_column='Implemented_On', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Dashboardapp_dmldetails'
    
    


#C:\Users\LENOVO\Dashboardproject\Dashboardapp\models.py