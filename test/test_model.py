
from src.ml_repro.predict import make_predictions
from src.ml_repro.model_trainer import train_model
from src.ml_repro.data_transformation import preprocess_data
from src.ml_repro.data_loader import load_data


def test_train_model():
    data = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(X_train, y_train)
    assert model is not None
    assert hasattr(model, "predict")


def test_load_data():
    data = load_data()
    assert data is not None
    assert "target" in data.columns


def test_make_predictions():
    data = load_data()
    X_train, X_test, y_train, y_test = preprocess_data(data)
    model = train_model(X_train, y_train)
    predictions = make_predictions(model, X_test)
    assert len(predictions) == len(y_test)
