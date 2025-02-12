from pipelines.run_pipeline import run_pipeline
from config import config

def main():
    # Load configuration
    with open("config/config.yaml", "r") as file:
        config = yaml.safe_load(file)
    
   
    results = run_pipeline(config)
    print("Pipeline results:", results)

if __name__ == "__main__":
    main()


# main.py
import os
import sys
import subprocess
from pipelines.run_pipeline import run_pipeline

def deploy_streamlit():
    """Deploy Streamlit app after pipeline execution"""
    subprocess.run(["python", "deployment/deploy_streamlit.py"])

def start_monitoring():
    """Start monitoring after deployment"""
    subprocess.run(["python", "monitor/monitor.py"])

def main():
    """Main pipeline execution"""
    print("Running the pipeline...")
    run_pipeline()  # Run the pipeline logic
    deploy_streamlit()  # Deploy the Streamlit app
    start_monitoring()  # Start monitoring

if __name__ == "__main__":
    main()
