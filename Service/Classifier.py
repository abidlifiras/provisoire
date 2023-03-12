from datetime import datetime
import pandas as pd
from pymongo import MongoClient
import pymongo
import yaml

from Model.Workflow import Workflow


client = MongoClient('localhost', 27017)
db = client["BR"]
collection1=db.Sheets
collection2=db.Results




def classifier():
    result = {}
    last_files = collection1.find_one(sort=[('timestamp', pymongo.DESCENDING)])
    if last_files == None:
        return " veillez entrer des fichiers "
    files_content = last_files['file_content']
    existing_result = collection2.find_one({'file_timestamp': last_files['timestamp']})
    if existing_result is not None:
        return existing_result['result']
    with open("Ressources/mapping.yml", 'r') as stream:
        file_workflow_kpis = yaml.safe_load(stream)
    for file_data_dict in files_content:
        file_name = file_data_dict['filename']
        file_content = file_data_dict['data']
        result[file_name] = []
        workflows_kpis = file_workflow_kpis.get(file_name, [])
        i = 1
        for workflow_data in workflows_kpis:
            workflow_name = workflow_data['workflow_name']
            kpis_name = workflow_data['kpis']
            charts_name = workflow_data['charts']
            workflow = Workflow(i, workflow_name)
            i += 1
            workflow.charger_workflow(kpis_name, charts_name)
            df = pd.read_excel(file_content)
            workflow.compute(df)
            result[file_name].append(workflow.get_result())
    timestamp = datetime.now()
    result_doc = {
        "file_timestamp" : last_files['timestamp'],
        "timestamp": timestamp,
        "result": result
    }
    collection2.insert_one(result_doc)

    return result





