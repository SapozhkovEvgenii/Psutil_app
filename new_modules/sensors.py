import psutil
from datetime import datetime


def get_sensors_info():
    time_file = datetime.now()
    sensors = {}
    time = "Дата и время"
    core_0 = "Температура Core 0"
    core_1 = "Температура Core 1"
    sensors[time] = str(time_file)
    sensors[core_0] = psutil.sensors_temperatures().get('coretemp')[1].current
    sensors[core_1] = psutil.sensors_temperatures().get('coretemp')[2].current
    return sensors

