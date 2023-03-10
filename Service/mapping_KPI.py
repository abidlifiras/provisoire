
from datetime import datetime
import pandas as pd 

def calculate_Nbre_de_départs(data):
    HF=data["Date dépôt Démission"]
    
    now=datetime.strptime( "03/08/2023","%m/%d/%Y")
    H=0
    
    for i in HF :
        
        dd=datetime.strptime(i, "%m/%d/%Y")
        print(str(dd), now)
        if dd.month<now.month:
            
            H+=1
            
    return (H,"démissions")

df = pd.read_excel("Ressources/liste effectif.xlsx")
print(calculate_Nbre_de_départs(df))

'''
data=pd.ExcelFile("Ressources/liste effectif.xlsx")
sheet_names =data.sheet_names
for names in sheet_names :
    if names=="R72" :
        df = pd.read_excel(data, sheet_name=names, header=3,skiprows=1)
print(df.head())
'''