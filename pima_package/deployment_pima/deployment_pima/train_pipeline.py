from deployment_pima.config import config
from sklearn.model_selection import train_test_split
from deployment_pima.data_manager import load_data, save_pipeline
from deployment_pima import __version__ as _version
from deployment_pima import pipeline

import logging
_logger = logging.getLogger(__name__)

def train():
    """Main training function. Loads the data, split it to train and val,
       fit a model, save the model.
    """
    data = load_data(file_name=config.DATA_FILE)

    train, val = train_test_split(
        data,
        test_size=config.VAL_SIZE,
        random_state=config.SEED
    )

    X_train = train[[c for c in data.columns if c != config.TARGET]]
    y_train = train[config.TARGET]
    X_val = val[[c for c in val.columns if c != config.TARGET]]
    y_val = val[config.TARGET]

    pipeline.pima_pipeline.fit(X_train[config.FEATURES], y_train)
    _logger.info('Saving model version: {}'.format(_version))
    save_pipeline(pipeline_to_persist=pipeline.pima_pipeline)

if __name__ == '__main__':
    train()
