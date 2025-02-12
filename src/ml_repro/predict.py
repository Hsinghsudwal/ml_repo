class Prediction:
    def __init__(self, config):
        self.config = config

    def predict(self, model, new_data):
        # Prediction logic using the trained model
        predictions = model.predict(new_data)  # based on the model inputs
        return predictions
