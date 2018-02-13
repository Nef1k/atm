from django.contrib.auth.base_user import BaseUserManager


class CardManager(BaseUserManager):
    use_in_migrations = True
