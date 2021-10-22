from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseField:
    # TODO: make abstract?
    name: str
    value: Optional[str] = None
    # source could be an enum?
    source: str = "external_service_foo"


@dataclass
class RegistrationNumber(BaseField):
    # TODO: figure out what's specific to this field
    pass

