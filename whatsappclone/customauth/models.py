from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# class WcUser(models.Model):
#     username = models.TextField(unique=True, max_length=55)
#     password = models.CharField(max_length=128)

#     def save(self, *args, **kwargs):
#         # hash password before saving to DB
#         if not self.password.startswith('pbkdf2_'):
#             self.password = make_password(self.password)
#         super().save(*args, **kwargs)

#     def verify_password(self, raw_password):
#         return check_password(raw_password, self.password)

#     def __str__(self) -> str:
#         return self.username
