import pathlib
import os
import deployment_pima
import pandas as pd

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

# Paths
ROOT = pathlib.Path(deployment_pima.__file__).resolve().parent
MODEL_DIR = ROOT / 'trained_models'
DATA_DIR = ROOT / 'datasets'

# data
DATA_FILE = 'diabetes.csv'
TARGET = 'Outcome'
FEATURES = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness',
            'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
TEST_FILE_NAME = "test_case1.csv"

SEED = 42
VAL_SIZE = 0.2
IMPUTE_FEATURES = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
IMPUTE_ITER = 30

# Model
PIPELINE_FILE = "lgbm"
MODEL_HYP = {"max_depth":5, "n_estimators":500, "random_state":SEED, "num_leaves":12}
