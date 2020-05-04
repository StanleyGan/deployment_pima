from deployment_pima.processing.pipeline_helper import load_data
from deployment_pima.predict import make_predictions
from deployment_pima.config import config
import numpy as np
import json

def test_predictions():
    data = load_data(config.TEST_FILE_NAME)
    test_json = data.to_json(orient='records')
    output = make_predictions(json.loads(test_json))

    assert output is not None
    assert output.get('predictions').dtype.type == np.int64
    assert (output.get('predictions') == np.array([0,1])).all()
