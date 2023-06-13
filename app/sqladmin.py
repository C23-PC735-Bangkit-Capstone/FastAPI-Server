from sqladmin import Admin, ModelView
from .sqladmin_models import Device, Pond, Users, Vibration, VibrationHealth

def create_admin(app, engine):
    admin = Admin(app, engine)

    class DeviceAdmin(ModelView, model=Device):
        name = "Device"
        name_plural = "Devices"
        icon = "fas fa-mobile"
        column_searchable_list = ['pond_id']
        column_sortable_list = ['device_id', 'pond_id', 'signal_strength', 'battery_strength', 'condition']
        column_list = ['device_id', 'pond_id', 'signal_strength', 'battery_strength', 'condition']

    class PondAdmin(ModelView, model=Pond):
        name = "Pond"
        name_plural = "Ponds"
        icon = "fas fa-fish"
        column_searchable_list = ['user_id']
        column_sortable_list = ['pond_id', 'user_id', 'pond_location']
        column_list = ['pond_id', 'user_id', 'pond_location']

    class UsersAdmin(ModelView, model=Users):
        name = "User"
        name_plural = "Users"
        icon = "fa-solid fa-user"
        column_searchable_list = ['user_id', 'user_infos']
        column_sortable_list = ['user_id', 'user_infos', 'alarm_sound', 'notification_sound', 'contacts']
        column_list = ['user_id', 'user_infos', 'alarm_sound', 'notification_sound', 'contacts']

    class VibrationAdmin(ModelView, model=Vibration):
        name = "Vibration"
        name_plural = "Vibrations"
        icon = "fas fa-wave-square"
        column_searchable_list = ['device_id']
        column_sortable_list = ['device_id', 'timestamp', 'accx', 'accy', 'accz']
        column_list = ['device_id', 'timestamp', 'accx', 'accy', 'accz']

    class VibrationHealthAdmin(ModelView, model=VibrationHealth):
        name = "Vibration Health"
        name_plural = "Vibration Healths"
        icon = "fa-solid fa-heart-pulse"
        column_searchable_list = ['device_id']
        column_sortable_list = ['device_id', 'timestamp', 'health_category', 'health_score']
        column_list = ['device_id', 'timestamp', 'health_category', 'health_score']

    admin.add_view(DeviceAdmin)
    admin.add_view(PondAdmin)
    admin.add_view(UsersAdmin)
    admin.add_view(VibrationAdmin)
    admin.add_view(VibrationHealthAdmin)