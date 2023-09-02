
def get_val(collection, key, default='git'):
    """
        :param collection: исходный словарь.
        :param key: ключ элемента.
        :param default: значение по-умолчанию.
        :return: значение по ключу (если есть) или значение по-умолчанию.
    """

    if key in collection:
        return collection[key]
    return default
