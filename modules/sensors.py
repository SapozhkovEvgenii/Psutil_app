import psutil


def get_sensors_info():
    sensors_info = {}
    core_0 = "Температура Core 0"
    core_1 = "Температура Core 1"
    sensors_info[core_0] = psutil.sensors_temperatures().get('coretemp')[1].current
    sensors_info[core_1] = psutil.sensors_temperatures().get('coretemp')[2].current
    return sensors_info

