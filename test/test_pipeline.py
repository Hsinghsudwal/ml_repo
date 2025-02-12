import pytest
from pipeline import run_pipeline


@pytest.fixture
def config():
    return {
        "data": {"models": "data/models"},
        "deployment": {"streamlit_dir": "deployment/streamlit_app"},
    }


def test_run_pipeline(config):
    result = run_pipeline(config)
    assert "accuracy" in result
    assert result["accuracy"] > 0.9  # Assume good model performance
