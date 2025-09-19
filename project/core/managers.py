from typing import Any
from django.contrib.auth.models import UserManager


class CustomUserManager(UserManager):
    def create_user(self, username: str, password: str) -> Any:
        return super().create_user(username, password)
