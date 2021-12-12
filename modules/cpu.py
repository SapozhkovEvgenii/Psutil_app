import psutil


def get_cpu_info():
    cpu_info = {}
    cpu_load = "Загрузка ЦП (%)"
    numbers_cores = "Количество ядер"
    cpu_info[cpu_load] = psutil.cpu_percent(interval=1)
    cpu_info[numbers_cores] = psutil.cpu_count(logical=False)
    return cpu_info
