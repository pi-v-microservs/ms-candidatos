import json
from typing import Dict, Tuple, List, Callable, Set

from werkzeug.datastructures import ImmutableMultiDict


class ValidationResult:
    def __init__(self):
        self._errors: Dict[str, List[str]] = {}

    @property
    def errors(self):
        return self._errors.copy()

    @errors.setter
    def errors(self, prop_name_prop_error: Tuple[str, List[str]]):
        self._errors[prop_name_prop_error[0]] = prop_name_prop_error[1]

    def has_errors(self):
        return len(self._errors) > 0

    def to_json(self):
        return json.dumps(self._errors)


class ValidationResultBuilder:
    def __init__(self):
        self._result: ValidationResult = ValidationResult()

    @staticmethod
    def new():
        return ValidationResultBuilder()

    def add_error(self, prop_name: str, error: List[str]):
        self._result.errors = (prop_name, error)
        return self

    def use_missing_attributes_check(self, form_data: ImmutableMultiDict, expected_model_attributes: Set[str]):
        form_data_keys = form_data.keys()
        form_model_keys_intersect = {x for x in form_data.keys() if x in expected_model_attributes}

        if len(form_model_keys_intersect) < len(expected_model_attributes):
            model_form_diff = expected_model_attributes - form_data_keys
            [self.add_error(prop, ['required']) for prop in model_form_diff]

    def use_field_validation_rules(self, data: Dict[str, str], validation_rules: Dict[str, List[Callable]]):
        for key, value in data.items():
            field_rules = validation_rules.get(key)
            if field_rules is None:
                continue
            self._result.errors = key, list(filter(lambda x: x is not None, [rule(value) for rule in field_rules]))

    def build(self):
        return self._result
