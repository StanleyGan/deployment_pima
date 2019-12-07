from deployment_pima.config import config
import pandas as pd

import logging
_logger = logging.getLogger(__name__)

def make_predictions(input_data):
    """ Make predictions

    Args:
        input_data (A json string format)
    """
    data = pd.read_json(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction =
