import psutil
from datetime import datetime
from decorators import decorator

def run():
    @decorator.my_decorator_sensors
    def get_sensors_info():
        time_file = datetime.now()
        sensors = {}
        time = "Дата и время"
        core_0 = "Температура Core 0"
        core_1 = "Температура Core 1"
        sensors[time] = str(time_file)
        sensors[core_0] = psutil.sensors_temperatures().get('coretemp')[1].current
        sensors[core_1] = psutil.sensors_temperatures().get('coretemp')[2].current
        return sensors


    @decorator.my_decorator_cpu
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

    @decorator.my_decorator_net
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

    @decorator.my_decorator_memory
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


if __name__ == '__main__':
    run()

