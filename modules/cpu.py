import psutil


def get_cpu_info():
    cpu_info = {}
    cpu_info["Загрузка ЦП (%)"] = psutil.cpu_percent(interval=1)
    cpu_info["Количество ядер"] = psutil.cpu_count(logical=False)
    return cpu_info
