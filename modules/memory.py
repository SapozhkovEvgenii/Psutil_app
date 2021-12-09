import psutil


def get_memory_info():
    memory_info = {}
    memory_info["Объем физической памяти (байт)"] = psutil.virtual_memory().total
    memory_info["Объем доступной памяти (байт)"] = psutil.virtual_memory().available
    memory_info["Объем памяти подкачки (байт)"] = psutil.swap_memory().total
    return memory_info
