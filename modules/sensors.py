import psutil


def get_sensors_info():
    sensors_info = {}
    sensors_info["Температура Core 0"] = psutil.sensors_temperatures().get('coretemp')[1].current
    sensors_info["Температура Core 1"] = psutil.sensors_temperatures().get('coretemp')[2].current
    return sensors_info

