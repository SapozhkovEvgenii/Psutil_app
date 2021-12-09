import psutil


def get_net_info():
    net_info = {}
    net_info["Количество отправленных пакетов"] = psutil.net_io_counters().packets_sent
    net_info["Количество полученных пакетов"] = psutil.net_io_counters().packets_recv
    net_info["Количество отправленных байтов"] = psutil.net_io_counters().bytes_sent
    net_info["Количество полученных байтов"] = psutil.net_io_counters().bytes_recv
    return net_info

