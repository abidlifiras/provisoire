import json


class Workflow:
    def __init__(self, id, title):
        self.id = id
        self.title = title
        self.kpis = []
        self.kpisName=[]
        self.charts = []
        self.chartName=[]
    
    def charger_workflow(self,name_kpis,name_charts) :
        self.kpisName=name_kpis
        self.chartName=name_charts
    
    def add_kpi(self, KPI):
        self.kpis.append(KPI)

    def add_chart(self, Chart) :
        self.charts.append(Chart)
        
    def compute(self,data) :
        for name in self.kpisName :
            kpi = KPI(name, self.title)
            kpi.calculate(data)
            self.add_kpi(kpi)
        for name in self.chartName:
            chart = Chart(name,self.title)
            chart.calculate(data)
            self.add_chart(chart)

    def get_result(self) :
        result=[]
        for kpi in self.kpis : 
            result.append(kpi.to_dict())
        for chart in self.charts :
            result.append(chart.to_dict())
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
class Chart:
    def __init__(self, name,workflowName):
        self.name = name
        self.workflow = workflowName
        self.calculate_func = None
        self.value=None
        self.type=None
        self.unit=None
        
    def calculate(self, data):
        if not self.calculate_func:
            udf_module = importlib.import_module('Service.UDF')
            self.calculate_func = getattr(udf_module, f"calculate_{self.name}")
        result = self.calculate_func(data)
        (self.value,self.unit,self.type)=result
        return result
    def to_dict(self):
        return { 'name': self.name, 'workflow':self.workflow , 'valeur': self.value , 'unit':self.unit , 'type' : self.type}