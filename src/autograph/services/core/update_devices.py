from ..autograph import autograph_session
from autograph.models import Schema, DeviceGroup, Device


def update_devices() -> bool:
    ''' Обновление машин '''

    schemas = Schema.objects.all()
    existing_device_ids = Device.objects.values_list('device_id', flat=True)

    for schema in schemas:

        devices_json = autograph_session.get_devices(schema.schema_id)
        device_groups = {device_group.name: device_group for device_group in DeviceGroup.objects.filter(active=True, schema=schema)}

        groups = {
            group['ID']: device_groups[group['Name']]
        for group in devices_json['Groups'] if group['Name'] in device_groups}

        devices = [
            Device(name=device['Name'], device_id=device['ID'], group=groups[device['ParentID']])
        for device in devices_json['Items'] if device['ParentID'] in groups and device['ID'] not in existing_device_ids]

        Device.objects.bulk_create(devices)

    return True
