import os
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from enum import IntEnum

class DolarOrEuro(IntEnum):
    DOLAR = 1
    EURO = 2

PROJECT_TOP_DIR = os.getcwd() + os.sep + ".." + os.sep
PATH_DATASET_DIR = PROJECT_TOP_DIR + "dataset" + os.sep
PATH_MODEL_DIR = PROJECT_TOP_DIR + "model_experiments" + os.sep
def predict_dollar_or_euro_price(dolarOrEuro:DolarOrEuro, date:datetime):
    if not isinstance(date, datetime):
        raise ValueError("Input should be a datetime object")

    dolar_or_euro:str = "Dolar" if dolarOrEuro == DolarOrEuro.DOLAR else "Euro"
    df = pd.read_excel(f"{PATH_DATASET_DIR}{dolar_or_euro}.xlsx")

    df['Tarih'] = pd.to_datetime(df['Tarih'], dayfirst=True)
    df.set_index('Tarih', inplace=True)
    df[dolar_or_euro] = df[dolar_or_euro].interpolate(method='linear')
    df[dolar_or_euro] = df[dolar_or_euro].astype("float32")
    df.dropna(inplace=True)

    WINDOW_SIZE = 30  # Adjust this to match the model's expected input size

    start_date = df.index.min()
    end_date = df.index.max()

    if date <= end_date:
        raise ValueError("The requested date should be in the future compared to the dataset")

    import tensorflow as tf

    # Load the model
    model = tf.keras.models.load_model(PATH_MODEL_DIR + dolar_or_euro + os.sep +"model_2_dense/")

    # Initialize the last known window prices from the dataset
    last_known_date = df.index[-1]
    window_prices = df[dolar_or_euro].iloc[-WINDOW_SIZE:].values

    # Predict iteratively up to the requested date
    current_date = last_known_date + timedelta(days=1)
    while current_date < date:
        window_prices = np.expand_dims(window_prices, axis=0)  # Shape: (1, 30)
        prediction = model.predict(window_prices)
        predicted_price = prediction[0][0]

        # Slide the window: remove the oldest price and add the predicted price
        window_prices = np.append(window_prices[0, 1:], predicted_price)

        current_date += timedelta(days=1)
        #print(current_date.date(), predicted_price)
        yield current_date.date(), predicted_price

    # Return the predicted price as an integer
    return int(predicted_price)


if False:
    date_to_predict = datetime(2025, 5, 15)

    for predicted_price in predict_dollar_price(date_to_predict):
        print(f"The predicted dollar price on {date_to_predict.date()} is: {predicted_price}")
