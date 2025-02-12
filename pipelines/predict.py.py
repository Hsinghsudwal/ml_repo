import joblib
import pandas as pd


def predict(model_path, new_data_path):
    model = joblib.load(model_path)
    new_data = pd.read_csv(new_data_path)
    predictions = model.predict(new_data)
    print(predictions)


if __name__ == "__main__":
    predict("data/models/model.pkl", "data/raw/new_data.csv")
