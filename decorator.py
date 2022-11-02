def singleton(class_object):
    instances = {}

    def get_instance(*args, **kwargs):
        if class_object not in instances:
            instances[class_object] = class_object(*args, **kwargs)
        return instances[class_object]

    return get_instance
