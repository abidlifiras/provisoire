from flask import Flask, request,jsonify
from pymongo import MongoClient
from flask_cors import CORS
from Service import sheet_info ,Classifier




# client = MongoClient("mongodb+srv://Sofrecom:Sofrecom@cluster0.tlki0xj.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient('localhost', 27017)
db = client["BR"]
collection1=db.Workflow
collection2=db.Sheets
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/demo/upload-demo-data', methods=['POST'])
def upload_demo_data():
    files = request.files.getlist('file')       
    (predicted,list)=sheet_info.get_sheet_info(files)

    return jsonify(result= predicted ,list_file=list)




@app.route('/demo/result', methods=['GET'])
def result():
    return jsonify(result= Classifier.classifier())

            


if __name__ == '__main__':
    app.run(debug=True)
