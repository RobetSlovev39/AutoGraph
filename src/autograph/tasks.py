# Таски для Celery ( обновление базы данными из AutoGraph )

from .services.core import (
    auth,
    update_schemas
)

from settings import celery_app


@celery_app.task(name='autograph_auth')
def ag_auth() -> bool:
    return auth()

@celery_app.task(name='update_schemas')
def ag_update_schemas() -> bool:
    return update_schemas()
