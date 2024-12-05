from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from prediction import predict_calories

app = FastAPI()

class InputData(BaseModel):
    carbs: float
    protein: float
    fats: float

@app.post('/predict')
def predict(input_data: InputData):
    try:
        result = predict_calories(input_data.dict())
        return {"calories": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
