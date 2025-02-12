# ml_repo


Key Features:
Pipeline: The core of the project in pipeline.py integrates various nodes like data preprocessing, training, evaluation, and prediction.
Deployment: After executing the pipeline, it automatically deploys the model to a Streamlit app located in the deployment/streamlit_app directory.
Prediction: A separate script (predict.py) to make predictions using the trained model.
Modularity: Each stage of the pipeline (data, training, evaluation, prediction, storage) is encapsulated into separate nodes, which can easily be extended or modified.
Logging: Provides useful logging during the execution of the pipeline for tracking progress and debugging.

Running the Pipeline:

To run the pipeline, execute:

```bash
python pipelines/run_pipeline.py
```
This will run the pipeline, train the model, save it, deploy the Streamlit app, and display the evaluation results.

To make predictions after deployment:

```bash
python pipelines/predict.py
```

streamlit
```bash
streamlit run deployment/app.py
```
This custom framework gives you full control over your ML pipeline, including deployment to Streamlit after training. It also supports making predictions using the saved model.