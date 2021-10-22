from journey import Step


# TODO: move this to inside validators.py?
def validate_step(step: Step):
    results = []
    for validator in step.validators:
        ValidationClass = validator.validation_class
        value = next(
            (
               field.value
                for field in step.fields
                if field.name == validator.field_name
            ),
            None
        )
        results.append(ValidationClass().is_valid(value))

    return results and all(results)


def populate_step(step: Step):
    for field in step.fields:
        field.value = "Foo"
