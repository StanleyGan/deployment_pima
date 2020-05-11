import math
import os

from deployment_pima.config import config as model_config
from deployment_pima.predict import make_predictions
from deployment_pima.processing.pipeline_helper import load_data
import pandas as pd
import pytest

from api import config


@pytest.mark.differential
def test_model_prediction_differential(
        *,
        save_file: str = 'test_data_predictions.csv'):
    """
    This test compares the prediction result similarity of
    the current model with the previous model's results.
    """

    # Given
    # Load the saved previous model predictions
    previous_model_df = pd.read_csv(os.path.join(config.PACKAGE_ROOT, 'tests', save_file))
    previous_model_predictions = previous_model_df.predictions.values

    test_data = load_data(file_name=model_config.DATA_FILE)
    multiple_test_input = test_data[:20]

    # When
    current_result = make_predictions(input_data=multiple_test_input)
    current_model_predictions = current_result.get('predictions')

    # Then
    # diff the current model vs. the old model
    assert len(previous_model_predictions) == len(
        current_model_predictions)

    # Perform the differential test
    assert( math.isclose(
                sum(previous_model_predictions), sum(current_model_predictions),
                rel_tol=model_config.ACCEPTABLE_MODEL_DIFFERENCE
        )
    )
