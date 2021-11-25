from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ''' На случай расширения User'а '''
    pass
