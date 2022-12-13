from collections import deque


def get_last(filename, n=5):
    """
    Возвращаем последние N кол-во строк из файла
    """
    try:
        with open(filename) as f:
            return deque(f, n)
    except OSError:
        print("Файл не открывается: {}".format(filename))
        raise
