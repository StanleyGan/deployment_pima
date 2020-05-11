from deployment_pima.config import config
from deployment_pima import __version__ as _version
from deployment_pima.processing.pipeline_helper import load_pipeline
from deployment_pima.processing.data_validation import validate_inputs
import pandas as pd

import logging
_logger = logging.getLogger(__name__)

saved_model_path = "{}_{}.pkl".format(config.PIPELINE_FILE, _version)
saved_model = load_pipeline(saved_model_path)

def make_predictions(input_data) -> dict:
    """ Make predictions

    Args:
        input_data (A list of dictionaries loaded from json)
    """
    data = pd.DataFrame(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = saved_model.predict(validated_data[config.FEATURES])

    results = {
        'predictions': prediction,
        'version': _version
    }

    _logger.info("Predictions made with model version {}".format(_version))

    return results
