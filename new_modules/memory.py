import psutil
from datetime import datetime


def get_memory_info():
    time_file = datetime.now()
    memory_info = {}
    time = "Дата и время"
    total_memory = "Объем физической памяти (байт)"
    available_memory = "Объем доступной памяти (байт)"
    total_swap = "Объем памяти подкачки (байт)"
    memory_info[time] = str(time_file)
    memory_info[total_memory] = psutil.virtual_memory().total
    memory_info[available_memory] = psutil.virtual_memory().available
    memory_info[total_swap] = psutil.swap_memory().total
    return memory_info

