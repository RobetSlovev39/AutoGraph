from .session import Session
import os  # from django.conf import settings

autograph_session = Session(
    api=os.environ['AG_SERVER'],  # settings.AG_SERVER
    login=os.environ['AG_LOGIN'],  # settings.AG_LOGIN
    password=os.environ['AG_PASSWORD'],  # settings.AG_PASSWORD
    time_difference=120  # settings.TIME_DIFFERENCE_IN_MIN
)

__all__ = ('autograph_session',)
