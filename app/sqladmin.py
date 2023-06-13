from sqladmin import Admin, ModelView
from .models import Device, Pond, Users, Vibration, VibrationHealth

def create_admin(app, engine):
    admin = Admin(app, engine)

    class DeviceAdmin(ModelView, model=Device):
        column_list = ['id', 'device_id', 'pond_id', 'signal_strength', 'battery_strength', 'condition']
    class PondAdmin(ModelView, model=Pond):
        column_list = ['id', 'pond_id', 'user_id', 'pond_location']
    class UsersAdmin(ModelView, model=Users):
        column_list = ['id', 'user_id', 'user_infos', 'alarm_sound', 'notification_sound', 'contacts']
    class VibrationAdmin(ModelView, model=Vibration):
        column_list = ['id', 'timestamp', 'device_id', 'accx', 'accy', 'accz']
    class VibrationHealthAdmin(ModelView, model=VibrationHealth):
        column_list = ['id', 'timestamp', 'device_id', 'health_category', 'health_score']

    admin.add_view(DeviceAdmin)
    admin.add_view(PondAdmin)
    admin.add_view(UsersAdmin)
    admin.add_view(VibrationAdmin)
    admin.add_view(VibrationHealthAdmin)