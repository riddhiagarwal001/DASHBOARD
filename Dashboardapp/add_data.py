import pandas as pd
from django.core.management.base import BaseCommand
from Dashboardapp.models import VC_Master
from Dashboardapp.models import V_master
from Dashboardapp.models import StrLoc
from Dashboardapp.models import MAP
from Dashboardapp.models import Part_Master
from Dashboardapp.models import MRP
from Dashboardapp.models import DMLdetails

from sqlalchemy import create_engine

class Command(BaseCommand):
    help = "A command to add data from an Excel file to database"

    def VC_master(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(VC_Master._meta.db_table,if_exists='replace',con=engine,index=False)


    def V_master(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(V_master._meta.db_table,if_exists='replace',con=engine,index=False)


    def StrLoc(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(StrLoc._meta.db_table,if_exists='replace',con=engine,index=False)

    def MAP(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(MAP._meta.db_table,if_exists='replace',con=engine,index=False)

    def Part_Master(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(Part_Master._meta.db_table,if_exists='replace',con=engine,index=False)

    def MRP(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(MRP._meta.db_table,if_exists='replace',con=engine,index=False)

    def DMLdetails(excel):
        df = pd.read_excel(excel,keep_default_na=False)
        engine = create_engine('sqlite:///db.sqlite3')
        df.to_sql(DMLdetails._meta.db_table,if_exists='replace',con=engine,index=False)


    

    
   