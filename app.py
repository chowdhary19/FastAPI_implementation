

# 1. Library imports
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle
import pandas as pd

# 2. Create the app object
app = FastAPI()

# Load the pre-trained classifier
with open("classifier.pkl", "rb") as file:
    classifier = pickle.load(file)

# Define a Pydantic model for data validation
class BankNoteData(BaseModel):
    variance: float
    skewness: float
    curtosis: float
    entropy: float

# 3. Index route
@app.get('/')
async def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter
@app.get('/{name}')
async def greet_name(name: str):
    return {'message': f'Welcome, {name}'}

# 5. Prediction route
@app.post('/predict')
async def predict_banknote(data: BankNoteData):
    data_dict = data.model_dump()
    features = np.array([[data_dict['variance'], data_dict['skewness'], data_dict['curtosis'], data_dict['entropy']]])
    
    # Perform prediction
    prediction = classifier.predict(features)
    result = "Fake note" if prediction[0] > 0.5 else "Its a Bank note"
    
    return {'prediction': result}

# 6. Run the API with uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)