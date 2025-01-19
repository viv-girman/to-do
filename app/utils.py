import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def mobile_number_validator(value):
    regex = re.compile("^[6-9][0-9]{9}$")
    match = regex.match(str(value))
    if match is None:
        raise ValidationError(
            _(
                f"{value} is not a valid mobile number, which needs to begin with 6, 7, 8, or 9, and have a total of 10 digits."
            ),
            params={"value": value},
        )
