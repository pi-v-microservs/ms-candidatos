from datetime import datetime, date
from wtforms.validators import ValidationError


class YearSpan:
    def __init__(self, min_year: int, max_year: int, message=None):
        self.min_dt: date = datetime(min_year, 1, 1).date()
        self.max_dt: date = datetime(max_year, 1, 1).date()
        if not message:
            message = u'Data deve variar entre %i e %i.' % (min_year, max_year)
        self.message = message

    def __call__(self, form, field):
        input_date = form.data.get(field.name)
        if input_date is None:
            return

        if self.min_dt > input_date or self.max_dt < input_date:
            raise ValidationError(self.message)

