from django.contrib.auth.base_user import BaseUserManager


class CardManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, number, pin, **extras):
        if not number:
            raise ValueError('Number must be set')

        card = self.model(number=number, **extras)
        card.set_password(pin)
        card.save(using=self._db)
        return card

    def create_user(self, number, pin, **extras):
        extras.setdefault('is_active', True)
        extras.setdefault('balance', 0)
        extras.setdefault('auth_attempts_failed', 0)

        return self._create_user(number, pin, **extras)

    def create_superuser(self, number, pin, **extras):
        return self.create_user(number, pin, **extras)  # kinda stub for console createsuperuser
