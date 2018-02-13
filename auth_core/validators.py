from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CommonLengthValidator:
    def __init__(self, min_length=4, max_length=4):
        self.min_length = min_length
        self.max_length = max_length

    def validate(self, pin, card=None):
        if len(pin) < self.min_length or len(pin) > self.max_length:
            return ValidationError(_('Pin\'s length must be between%(min_length)d and %(max_length)d'),
                                   code='invalid_pin_length',
                                   params={
                                       'min_length': self.min_length,
                                       'max_length': self.max_length
                                   })

    def get_help_text(self):
        return _(
            'Your pin\'s length must be between %(min_length)d and %(max_length)d' % {
                'min_length': self.min_length,
                'max_length': self.max_length
            }
        )