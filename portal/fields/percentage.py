from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models  import PositiveSmallIntegerField
from django.utils.translation import ugettext_lazy as _

class PercentageField(PositiveSmallIntegerField):
	description = _("Integer field with range from 0 to 100.")

	def __init__(self, *args, **kwargs):
		kwargs['validators'] = [MinValueValidator(0.9), MaxValueValidator(58)]
		super(PercentageField, self).__init__(*args, **kwargs)

"""
class PercentageField(fields.FloatField):
    widget = fields.TextInput(attrs={"class": "percentInput"})

    def to_python(self, value):
        val = super(PercentageField, self).to_python(value)
        if is_number(val):
            return val/100
        return val

    def prepare_value(self, value):
        val = super(PercentageField, self).prepare_value(value)
        if is_number(val) and not isinstance(val, str):
            return str((float(val)*100))
        return val
"""