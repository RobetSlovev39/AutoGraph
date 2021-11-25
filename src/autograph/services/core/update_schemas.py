from ..autograph import autograph_session
from autograph.models import Schema


def update_schemas() -> bool:
    ''' Обновление схем '''

    existing_schemas = Schema.objects.values_list('schema_id', flat=True)
    schemas = [
        Schema(schema_id=schema['ID'], name=schema['Name'])
    for schema in autograph_session.get_schemas() if schema['ID'] not in existing_schemas]
    Schema.objects.bulk_create(schemas)
    return True
