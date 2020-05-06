from sklearn.pipeline import Pipeline
from deployment_pima.processing import preprocessors as preproc
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier as gbm
from deployment_pima.config import config

import logging
_logger = logging.getLogger(__name__)

pima_pipeline = Pipeline(
    [
        ('nan_imputer',
            preproc.MissingNaNImputer(columns=config.IMPUTE_FEATURES)),
        ('iterative_imputer',
            IterativeImputer(max_iter=config.IMPUTE_ITER,
                random_state=config.SEED)),
        ('standard_scaler',
            StandardScaler()),
        ('gbm',
            gbm(**config.MODEL_HYP))
    ]
)
