import logging
import pandas as pd
from deployment_pima.config import config

_logger = logging.getLogger(__name__)

def validate_inputs(input_data: pd.DataFrame) -> pd.DataFrame:
    """ Validate input data so that it's in expectation as seen in training

    Args:
        input_data (A pandas DataFrame)
    """
    validated_data = input_data.copy()

    non_na_cols_in_train = list(set(config.FEATURES) - set(config.IMPUTE_FEATURES))

    if validated_data[non_na_cols_in_train].isnull().any().any():
        validated_data = validated_data.dropna(
            axis=0, subset=non_na_cols_in_train
        )
        _logger.info(
            "NaN values are found and dropped in non-imputable features. \
            There are {} of such rows".format(
                input_data.shape[0] - validated_data.shape[0]
            )
        )

    return validated_data
