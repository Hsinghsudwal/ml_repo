def load_data(file_path="data/raw_data/data.csv"):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        raise FileNotFoundError(f"Data file {file_path} not found.")
