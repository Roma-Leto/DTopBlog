from django.db import models
from django.contrib.auth.models import AbstractUser


class BUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Прошёл активацию?')


    class Meta(AbstractUser.Meta):
        pass
