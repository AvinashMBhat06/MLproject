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
        rounded_score=round(predict_score[0],2)
        return render_template('result.html',L=[predict_score[0],request.form.get('gender').title(),request.form.get('ethnicity').title(),request.form.get('parental_level_of_education').title(),request.form.get('lunch').title(),request.form.get('test_preparation_course').title(),float(request.form.get('writing_score')),float(request.form.get('reading_score')),rounded_score])

if __name__=="__main__":
    web.run(host="0.0.0.0",debug=True)   