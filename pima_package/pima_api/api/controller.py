from flask import Blueprint, request, jsonify
from deployment_pima.predict import make_predictions
from deployment_pima import __version__ as model_version

from api.config import get_logger
from api.data_validation import validate_inputs
from api import __version__ as api_version

_logger = get_logger(logger_name=__name__)
classifier_app = Blueprint('classifier_app', __name__)

@classifier_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        _logger.info('health status OK')
        return 'ok'

@classifier_app.route('/version', methods=['GET'])
def version():
    if request.method == 'GET':
        return jsonify({'model_version': model_version,
                        'api_version': api_version})

@classifier_app.route('/v1/predict/classify', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        input_data, errors = validate_inputs(input_data=json_data)

        # Step 3: Model prediction
        result = make_predictions(input_data=input_data)
        _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions').tolist()
        version = result.get('version')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        'version': version,
                        'errors': errors})
