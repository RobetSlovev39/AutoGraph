# Таски для Celery ( обновление базы данными из AutoGraph )

from .services.core import (
    auth,
    update_schemas,
    update_devices
)

from settings import celery_app


@celery_app.task(name='autograph_auth')
def ag_auth() -> bool:
    ''' Обновление token'а '''

    return auth()


@celery_app.task(name='update_schemas')
def ag_update_schemas() -> bool:
    ''' Обновление схем '''

    return update_schemas()

@celery_app.task(name='update_devices')
def ag_update_devices() -> bool:
    ''' Обновление машин '''

    return update_devices()
