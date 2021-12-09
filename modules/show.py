def show(**kwargs):
    inform_cpu = "|{:*^70}|".format(" ИНФОРМАЦИЯ О ПРОЦЕССОРЕ ")
    print(inform_cpu)
    for key in kwargs["cpu"]:
        lenght_str_cpu = 70 - len(key)
        cpu_info = "|{}{:->{lenght}}|".format(key, kwargs["cpu"][key], lenght=lenght_str_cpu)
        print(cpu_info)
    print()

    inform_memory = "|{:*^70}|".format(" ИНФОРМАЦИЯ О ПАМЯТИ ")
    print(inform_memory)
    for key in kwargs["memory"]:
        lenght_str_memory = 70 - len(key)
        memory_info = "|{}{:->{lenght}}|".format(key, kwargs["memory"][key], lenght=lenght_str_memory)
        print(memory_info)
    print()

    inform_net = "|{:*^70}|".format(" ИНФОРМАЦИЯ О СЕТИ ")
    print(inform_net)
    for key in kwargs["net"]:
        lenght_str_net = 70 - len(key)
        net_info = "|{}{:->{lenght}}|".format(key, kwargs["net"][key], lenght=lenght_str_net)
        print(net_info)
    print()

    inform_sensors = "|{:*^70}|".format(" ИНФОРМАЦИЯ О ДАТЧИКАХ ")
    print(inform_sensors)
    for key in kwargs["sensors"]:
        lenght_str_sensors = 70 - len(key)
        sensors_info = "|{}{:->{lenght}}|".format(key, kwargs["sensors"][key], lenght=lenght_str_sensors)
        print(sensors_info)

