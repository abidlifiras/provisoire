from datetime import datetime

import pandas as pd


def calculate_average_age(data):
    age_col = data['Age']
    num_employees = len(age_col)
    total_age = age_col.sum()
    average_age = total_age / num_employees
    
    return (average_age,'annee')

def calculate_moyenne(data):
    X4 = data['x4']
    num = len(X4)
    total= X4.sum()
    average= total / num
    
    return (average,"moyenne")

def calculate_test_chart(data):

    result=[111 , 1,12,]
    return (result,"test","Histograme")

def calculate_HF(data):
    HF=data['H/F']
    F=0
    H=0
    for i in HF :
        if i=='Female' :
            F+=1
        else :
            H+=1
            
    result=[f"Homme :{H}" , f"Femme :{F}" ]
    return (result,"homme","Histograme")

def calculate_Nbre_de_departs(data):
    HF = data["Date de sortie"]
    now = datetime.now()
    H = 0

    for i in HF:
        dd = datetime.strptime(i, "%m/%d/%Y")
        if dd.year < now.year:
            H += 1
        elif dd.year == now.year and dd.month < now.month:
            H += 1
        elif dd.year == now.year and dd.month == now.month and dd.day < now.day:
            H += 1

    return (H, "démissions")


def calculate_effectif_par_mois_par_pole(df):
    current_year = datetime.now().year
    
    df_current_year = df[pd.to_datetime(df["Date d'entrée OIT"]).dt.year == current_year]
    
    counts = df_current_year.groupby(["Pole", pd.to_datetime(df_current_year["Date d'entrée OIT"]).dt.month]).size()
    
    result_dict = {}

    for (pole, month), count in counts.items():
        if month not in result_dict:
            result_dict[month] = []
        result_dict[month].append((pole, count))

    result = []
    for month, pole_counts in result_dict.items():
        for pole, count in pole_counts:
            result.append([month, pole, count])
        
    return (result,"effectif","chart")