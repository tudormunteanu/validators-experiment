from dataclasses import dataclass
from typing import Type, List

from validators import Validator
from fields import BaseField


@dataclass
class Step:
    key: str
    version: str
    fields: List[BaseField]
    validators: List[Validator]
