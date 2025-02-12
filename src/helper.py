def __init__(self, config):
    self.config = config


def load_data(self, file_path):
    return pd.read_csv(file_path)


def save_processed_data(self, data, file_path):
    data.to_csv(file_path, index=False)


def save_model(self, model, file_path):
    joblib.dump(model, file_path)


def load_model(self, file_path):
    return joblib.load(file_path)


def create_directory(directory):
    """Create a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
