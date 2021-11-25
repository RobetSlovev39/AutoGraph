# Таски для Celery ( обновление базы данными из AutoGraph )

from .services import autograph_session
from settings import celery_app


@celery_app.task(name='autograph_auth')
def autograph_auth() -> bool:
    return autograph_session.auth()
