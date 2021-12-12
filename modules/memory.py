import psutil


def get_memory_info():
    memory_info = {}
    total_memory = "Объем физической памяти (байт)"
    available_memory = "Объем доступной памяти (байт)"
    total_swap = "Объем памяти подкачки (байт)"
    memory_info[total_memory] = psutil.virtual_memory().total
    memory_info[available_memory] = psutil.virtual_memory().available
    memory_info[total_swap] = psutil.swap_memory().total
    return memory_info
