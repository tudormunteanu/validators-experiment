from dataclasses import dataclass
from typing import Type

APPLIES_TO_ENTIRE_DATA = "__all__"
APPLIES_BEFORE_STEP = "__pre__"


class BaseValidator:
    # TODO: make this an abstract class
    error_message = "Somethign went wrong."
    def is_valid(self, data):
        raise NotImplementedError


class AlwaysTrue(BaseValidator):
    def is_valid(self, data):
        return True


class RequiredValue(BaseValidator):
    error_message = "Field is required."

    def is_valid(self, data):
        return data is not None and len(data)


@dataclass
class Validator:
    """Associates a data field to a validation class."""
    field_name: str
    validation_class: Type[BaseValidator]
