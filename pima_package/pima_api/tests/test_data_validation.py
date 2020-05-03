import json

from deployment_pima.config import config
from deployment_pima.processing.pipeline_helper import load_data


def test_prediction_endpoint_validation_200(flask_test_client):
    # Given
    # Load the test data from the deployment_pima package.
    # This is important as it makes it harder for the test
    # data versions to get confused by not spreading it
    # across packages.
    test_data = load_data(file_name=config.TEST_FILE_NAME)
    post_json = test_data.to_json(orient='records')

    # When
    response = flask_test_client.post('/v1/predict/classify',
                                      json=json.loads(post_json))

    # Then
    assert response.status_code == 200
    response_json = json.loads(response.data)

    # Check correct number of errors removed
    assert len(response_json.get('predictions')) + len(
        response_json.get('errors')) == len(test_data)
