import psutil
from datetime import datetime


def get_net_info():
    time_file = datetime.now()
    net_info = {}
    time = "Дата и время"
    packets_sent = "Количество отправленных пакетов"
    packets_recv = "Количество полученных пакетов"
    bytes_sent = "Количество отправленных байтов"
    bytes_recv = "Количество полученных байтов"
    net_info[time] = str(time_file)
    net_info[packets_sent] = psutil.net_io_counters().packets_sent
    net_info[packets_recv] = psutil.net_io_counters().packets_recv
    net_info[bytes_sent] = psutil.net_io_counters().bytes_sent
    net_info[bytes_recv] = psutil.net_io_counters().bytes_recv
    return net_info

