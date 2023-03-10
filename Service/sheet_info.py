from datetime import datetime
from bson import Binary
import pandas as pd
from pymongo import MongoClient
from difflib import get_close_matches


client = MongoClient('localhost', 27017)
db = client["BR"]
collection1=db.Sheets




def get_sheet_info(files):
    all_files_data = []
    list_fichier=["R25","R27","liste effectif"]
    mapping = []
    timestamp = datetime.now() 
    file_info = {}
    file_info['timestamp'] = timestamp
    files_content=[]
    for file in files:
        file_data = file.read()
        file_data_binary = Binary(file_data)
        file_data_dict={'filename':file.filename,'data' :file_data_binary}
        files_content.append(file_data_dict)
        predict=get_close_matches(file.filename,list_fichier,1,0.5)
        mapping.append((file.filename,predict))
    file_info['file_content'] = files_content
    all_files_data.append(file_info)

    collection1.insert_many(all_files_data)

    return (mapping,list_fichier)