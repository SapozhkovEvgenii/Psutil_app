from datetime import datetime
import json


def my_decorator_sensors(func):
    """DECORATOR"""
    with open(f"{str(datetime.now())}_sensors.json", "w") as file_result:
        json.dump(func(), file_result, indent=4, ensure_ascii=False)
    return func


def my_decorator_net(func):
    """DECORATOR"""
    with open(f"{str(datetime.now())}_net.json", "w") as file_result:
        json.dump(func(), file_result, indent=4, ensure_ascii=False)
    return func


def my_decorator_cpu(func):
    """DECORATOR"""
    with open(f"{str(datetime.now())}_cpu.json", "w") as file_result:
        json.dump(func(), file_result, indent=4, ensure_ascii=False)
    return func


def my_decorator_memory(func):
    """DECORATOR"""
    with open(f"{str(datetime.now())}_memory.json", "w") as file_result:
        json.dump(func(), file_result, indent=4, ensure_ascii=False)
    return func


