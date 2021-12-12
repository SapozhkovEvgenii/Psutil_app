import psutil
from datetime import datetime


def get_cpu_info():
    time_file = datetime.now()
    cpu_info = {}
    time = "Дата и время"
    cpu_load = "Загрузка ЦП (%)"
    numbers_cores = "Количество ядер"
    cpu_info[time] = str(time_file)
    cpu_info[cpu_load] = psutil.cpu_percent(interval=1)
    cpu_info[numbers_cores] = psutil.cpu_count(logical=False)
    return cpu_info

