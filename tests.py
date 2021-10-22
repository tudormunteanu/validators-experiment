from fields import RegistrationNumber
from journey import Step
from services import validate_step
from validators import Validator, AlwaysTrue, APPLIES_BEFORE_STEP, RequiredValue


def test_step_with_always_true_field():
    # GIVEN
    step = Step(
        key="registration",
        version="x.x.x",
        fields=[
            RegistrationNumber(name="registration_number")
        ],
        validators=[
            Validator(field_name="registration_number", validation_class=AlwaysTrue),
            Validator(field_name=APPLIES_BEFORE_STEP, validation_class=AlwaysTrue),
        ]
    )
    
    # THEN
    assert validate_step(step) == True


def test_step_with_required_field():
    # GIVEN
    step = Step(
        key="registration",
        version="x.x.x",
        fields=[
            RegistrationNumber(name="registration_number")
        ],
        validators=[
            Validator(field_name="registration_number", validation_class=RequiredValue),
            Validator(field_name=APPLIES_BEFORE_STEP, validation_class=AlwaysTrue),
        ]
    )
    
    # THEN
    assert validate_step(step) == False



if __name__ == "__main__":
    test_step_with_always_true_field()
    test_step_with_required_field()

