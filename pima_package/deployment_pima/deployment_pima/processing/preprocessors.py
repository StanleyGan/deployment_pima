from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np
import pandas as pd

class MissingNaNImputer(BaseEstimator, TransformerMixin):
    """Replace 0 values with NaN for specified columns

    Args:
        columns (A list of str): Defaults to []
    """
    def __init__(self, columns: list = []):
        self.columns = columns

    def fit(self, X: pd.DataFrame, y: pd.Series) -> "MissingNaNImputer":
        """ To accommodate sklearn pipeline
        """
        return self

    def transform(self, X: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            X (A pd.DataFrame)
        """
        X_ = X.copy()
        for c in self.columns:
            X_.loc[X[c] == 0, c] = np.nan

        return X_
