from datetime import datetime


def calculate_average_age(data):
    age_col = data['Age']
    num_employees = len(age_col)
    total_age = age_col.sum()
    average_age = total_age / num_employees
    
    return (average_age,'age')

def calculate_moyenne(data):
    X4 = data['x4']
    num = len(X4)
    total= X4.sum()
    average= total / num
    
    return (average,"moyenne")

def calculate_test_chart(data):

    result=[111 , 1,12,]
    return (result,"Histograme")

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
    return (result,"Histograme")

def calculate_Nbre_de_départs(data):
    HF=data["Date dépôt Démission"]
    
    now=datetime.strptime( "03/08/2023","%m/%d/%Y")
    H=0
    
    for i in HF :
        
        dd=datetime.strptime(i, "%m/%d/%Y")
        if dd.year<now.year:
            
            H+=1
        else :
            if dd.year==now.year :
                if dd.month<now.month :
                    H+=1
                else :
                    if dd.month==now.month :
                        if dd.day<now.day :
                            H+=1

            
    return (H,"démissions")