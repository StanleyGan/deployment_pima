from marshmallow import Schema, fields
from marshmallow import ValidationError

import typing as t
import json


class InvalidInputError(Exception):
    """Invalid model input."""


class PimaDataSchema(Schema):
    Pregnancies = fields.Integer()
    Glucose = fields.Float()
    BloodPressure = fields.Float()
    SkinThickness = fields.Float()
    Insulin = fields.Float()
    BMI = fields.Float()
    DiabetesPedigreeFunction = fields.Float()
    Age = fields.Integer()



def _filter_error_rows(errors: dict,
                       validated_input: t.List[dict]
                       ) -> t.List[dict]:
    """Remove input data rows with errors."""

    indexes = errors.keys()
    # delete them in reverse order so that you
    # don't throw off the subsequent indexes.
    for index in sorted(indexes, reverse=True):
        del validated_input[index]

    return validated_input


def validate_inputs(input_data):
    """Check prediction inputs against schema."""

    # set many=True to allow passing in a list
    schema = PimaDataSchema(strict=True, many=True)
    errors = {}

    try:
        schema.load(input_data)
    except ValidationError as exc:
        errors = exc.messages

    if errors:
        validated_input = _filter_error_rows(
            errors=errors,
            validated_input=input_data)
    else:
        validated_input = input_data

    return validated_input, errors
