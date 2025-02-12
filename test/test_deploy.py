from deployment.deploy_streamlit import deploy_streamlit
import os
import shutil


def test_deploy_streamlit():
    test_streamlit_dir = "test_deployment"
    if os.path.exists(test_streamlit_dir):
        shutil.rmtree(test_streamlit_dir)

    deploy_streamlit(test_streamlit_dir)
    assert os.path.exists(test_streamlit_dir)  # Ensure the deployment was successful
