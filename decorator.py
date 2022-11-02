from typing import Callable


def singleton(class_object: Callable):
    """
    :param class_object: singleton object
    :return: decorator
    """
    instances: dict = {}

    def get_instance(*args, **kwargs):
        if class_object not in instances:
            instances[class_object] = class_object(*args, **kwargs)
        return instances[class_object]

    return get_instance
