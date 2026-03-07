import joblib
import numpy as np
import pandas as pd

model = joblib.load('model/car_price_model.pkl')
preprocessor = joblib.load('model/preprocessor.pkl')


def predict_price(input_data):
    df = pd.DataFrame([input_data])

    # preprocess
    df['car_age'] = 2026 - df['year']
    
    X = preprocessor.transform(df)

    # prediction on log_price
    pred_log = model.predict(X)

    #convert to real price
    price = np.exp(pred_log)

    return price[0]