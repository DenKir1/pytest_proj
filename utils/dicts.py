
def get_val(collection, key, default='git'):
    """
        :param array: исходный список.
        :param index: индекс элемента.
        :param default: значение по-умолчанию.
        :return: значение по индексу (если есть) или значение по-умолчанию.
    """
    if 0 <= key < len(collection):
        return collection[key]
    return default

