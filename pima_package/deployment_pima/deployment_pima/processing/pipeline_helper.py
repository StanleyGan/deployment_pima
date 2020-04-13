import pandas as pd
import os
import logging
import joblib
from deployment_pima.config import config
from deployment_pima import __version__ as _version
from sklearn.pipeline import Pipeline

_logger = logging.getLogger(__name__)

def load_data(file_name: str) -> pd.DataFrame:
    """
    Args:
        file_name (A str)
    """
    _data = pd.read_csv(os.path.join(config.DATA_DIR, file_name))
    return _data

def save_pipeline(pipeline_to_persist) -> None:
    """ Persist the pipeline

    Saves the versioned model, and overwrites any previous
    saved models. This ensures that when the package is
    published, there is only one trained model that can be
    called, and we know exactly how it was built.

    Args:
        pipeline_to_persist (A sklearn Pipeline object)
    """
    # File name
    save_file = "{}_{}.pkl".format(config.PIPELINE_FILE, _version)
    save_path = config.MODEL_DIR / save_file

    remove_old_pipelines(file_to_keep=save_file)
    joblib.dump(pipeline_to_persist, save_path)
    _logger.info("Saved pipeline: {}".format(save_file))

def remove_old_pipelines(file_to_keep) -> None:
    """ Remove other pipelines and only keep one for deployment

    Args:
        file_to_keep (A str/ A Pathlib object)

    """
    for f in config.MODEL_DIR.iterdir():
        if f not in [file_to_keep, '__init__.py']:
            f.unlink()

def load_pipeline(file_name: str) -> Pipeline:
    """ Load saved model

    Args:
        file_name (A str)
    """
    model = joblib.load(os.path.join(config.MODEL_DIR, file_name))

    return model
