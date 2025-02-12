from src.ml_repro.data_loader import load_data
from src.ml_repro.data_transformation import preprocess_data
from src.ml_repro.model_trainer import train_model
from src.ml_repro.model_evaluation import evaluate_model
from src.ml_repro.predict import make_predictions
from src.helper import create_directory
from deployment.deploy_streamlit import deploy_streamlit
import joblib

def run_pipeline(config):
    # Step 1: Load data
    data = load_data()

    # Step 2: Preprocess data (split into train/test)
    X_train, X_test, y_train, y_test = preprocess_data(data)

    # Step 3: Train model
    model = train_model(X_train, y_train)

    # Step 4: Evaluate model
    results = evaluate_model(model, X_test, y_test)

    # Step 5: Save trained model
    create_directory(config['data']['models'])
    joblib.dump(model, config['data']['models'] + '/model.pkl')

    # Step 6: Deploy to Streamlit app
    deploy_streamlit(config['deployment']['streamlit_dir'])

    return results
