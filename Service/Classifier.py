import pandas as pd
from pymongo import MongoClient
import pymongo

from Model.Workflow import Workflow


client = MongoClient('localhost', 27017)
db = client["BR"]
collection1=db.Sheets
collection2=db.Results


file_workflow_kpis = {
    "R25.xls": [("people", ["average_age"]),("budget",["test_chart"])],
    "R27.xlsx": [("budget", ["moyenne"])],
    "liste effectif.xlsx" :[('people',["HF" ,"Nbre_de_départs"])]
}


def classifier():
    result = {}
    last_file = collection1.find_one(sort=[('timestamp', pymongo.DESCENDING)])
    files_content = last_file['file_content']
    for file_data_dict in files_content:
        file_name = file_data_dict['filename']
        file_content = file_data_dict['data']
        result[file_name] = []
        workflows_kpis = file_workflow_kpis.get(file_name, [])
        i = 1
        for workflow_name, kpis_name in workflows_kpis:
            workflow = Workflow(i, workflow_name)
            i += 1
            workflow.charger_workflow(kpis_name)
            df = pd.read_excel(file_content)
            workflow.compute(df)
            result[file_name].append(workflow.get_result())

    return result






