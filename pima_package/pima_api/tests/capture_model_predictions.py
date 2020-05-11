"""
This script should only be run in CI.
Never run it locally or you will disrupt the
differential test versioning logic.
"""

import pandas as pd
import os

from deployment_pima.predict import make_predictions
from deployment_pima.processing.pipeline_helper import load_data
from deployment_pima.config import config as model_config
from api.config import config as config


def capture_predictions() -> None:
    """Save the test data predictions to a CSV."""

    save_file = 'test_data_predictions.csv'
    test_data = load_data(file_name=model_config.DATA_FILE)

    multiple_test_input = test_data[:20]

    predictions = make_predictions(input_data=multiple_test_input)

    # save predictions for the test dataset
    predictions_df = pd.DataFrame(predictions)

    # hack here to save the file to the regression model
    # package of the repo, not the installed package
    predictions_df.to_csv(
        os.path.join(config.PACKAGE_ROOT, "tests", save_file)
    )


if __name__ == '__main__':
    capture_predictions()
