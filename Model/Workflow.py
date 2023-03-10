import json


class Workflow:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.kpis = []
        self.kpisName=[]
    
    def charger_workflow(self,name_kpis) :
        self.kpisName=name_kpis
    
    def add_kpi(self, KPI):
        self.kpis.append(KPI)
        
    def compute(self,data) :
        for name in self.kpisName :
            kpi = KPI(name, self.title)
            kpi.calculate(data)
            self.add_kpi(kpi)
    def get_result(self) :
        result=[]
        for kpi in self.kpis : 
            result.append(kpi.to_dict())
        return result
    
    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'kpis': json.dumps([kpi.to_dict() for kpi in self.kpis])}

#-----------------------------------------------------------------------------------------------------------------------------    
import importlib

class KPI:
    def __init__(self, name,workflowName):
        self.name = name
        self.workflow = workflowName
        self.calculate_func = None
        self.value=None
        self.unit=None
        
    def calculate(self, data):
        if not self.calculate_func:
            udf_module = importlib.import_module('Service.UDF')
            self.calculate_func = getattr(udf_module, f"calculate_{self.name}")
        result = self.calculate_func(data)
        (self.value,self.unit)=result
        return result
    def to_dict(self):
        return { 'name': self.name, 'workflow':self.workflow , 'valeur': self.value , 'unit':self.unit}

#-----------------------------------------------------------------------------------------------------------------------------
    
class KPIEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, KPI):
            return {"name": obj.name, "workflowName": obj.workflow , "value":obj.value}
        return super().default(obj)
    
#-----------------------------------------------------------------------------------------------------------------------------
    