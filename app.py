from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schemas.user_inputs import UserInput
from model.predict import predict_output,MODEL_VERSION
from schemas.prediction_response import PredictResponse
# import the ml model

app = FastAPI()



@app.post('/predict',response_model=PredictResponse)
def predict_premium(data: UserInput):
    user_input ={
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction=predict_output(user_input)
        return JSONResponse(status_code=200,content={'predicted_category': prediction})
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})

@app.get('/')
def home():
    return JSONResponse(status_code=200, content={'message': 'Welcome to the Insurance Premium Prediction API'})

##machine reading model is not always available, so we can add a health check endpoint 

@app.get('/health')
def health_check():
    return JSONResponse(status_code=200, content={'status': 'healthy','version': MODEL_VERSION}) 