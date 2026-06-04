import pickle 
from flask import Flask,render_template,request
import pandas as pd 
import numpy as np 
from src.pipeline.predict_pipeline import CustomData,PredictPipeline
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata',methods=["GET","POST"])
def predictdata():
    if request.method == "POST":
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )
        pd = data.get_data_as_dataframe()
        
        predic_pipeline = PredictPipeline()
        result = predic_pipeline.predict(pd)
        
        return render_template('home.html',result = result[0])
    
    else:
        return render_template('home.html')
    
        




if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000)
