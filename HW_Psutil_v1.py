from modules import cpu, memory, net, sensors, show


def run():
    show.show(cpu=cpu.get_cpu_info(), memory=memory.get_memory_info(),
              net=net.get_net_info(), sensors=sensors.get_sensors_info(),
              )


if __name__ == '__main__':
    run()
