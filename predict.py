import pandas as pd
import numpy as np
import tensorflow as tf
from datetime import datetime, timedelta

# Load the data
df = pd.read_excel('Dolar.xlsx')

# Data preprocessing
df['Tarih'] = pd.to_datetime(df['Tarih'], dayfirst=True)
df.set_index('Tarih', inplace=True)
df['Dolar'] = df['Dolar'].interpolate(method='linear')
df["Dolar"] = df["Dolar"].astype("float32")
df.dropna(inplace=True)

# Set the global variables for window and horizon size
WINDOW_SIZE = 30  # Adjust this to match the model's expected input size
HORIZON = 1


def predict_dollar_price(date, df):
    # Date validation
    if not isinstance(date, datetime):
        raise ValueError("Input should be a datetime object")

    # Ensure the date is within the allowed range
    start_date = df.index.min()
    end_date = df.index.max()

    if date <= end_date:
        raise ValueError("The requested date should be in the future compared to the dataset")

    # Load the model
    model = tf.keras.models.load_model("model_experiments/model_2_dense/")

    # Initialize the last known window prices from the dataset
    last_known_date = df.index[-1]
    window_prices = df['Dolar'].iloc[-WINDOW_SIZE:].values

    # Predict iteratively up to the requested date
    current_date = last_known_date + timedelta(days=1)
    while current_date <= date:
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


# Example usage
date_to_predict = datetime(2025, 5, 15)

for predicted_price in predict_dollar_price(date_to_predict, df):
    print(f"The predicted dollar price on {date_to_predict.date()} is: {predicted_price}")
