from flask import Flask,request,render_template
from src.pipeline.prediction_pipeline import CustomData,Predict_pipeline

app=Flask(__name__)
web=app
@web.route('/')

def index():
    return render_template('index.html')

@web.route('/home.html',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='GET':
        return render_template('home.html')
    else:
        data=CustomData(            
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('ethnicity'),
            parental_level_of_education=request.form.get('parental_level_of_education'),
            lunch=request.form.get('lunch'),
            test_preparation_course=request.form.get('test_preparation_course'),
            reading_score=float(request.form.get('writing_score')),
            writing_score=float(request.form.get('reading_score'))

        )
        feature=data.coverting_datato_df_format()
        prediction=Predict_pipeline()
        predict_score=prediction.predict(feature)
        return render_template('home.html',results=predict_score[0])


if __name__=="__main__":
    web.run(host="0.0.0.0",debug=True)   