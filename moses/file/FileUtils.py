import os
import shutil
import types

from moses.hash import Hash
from moses.collection import CollectionUtils


def get_size(path: (str,)):
    """
    unit: byte
    :param path:
    :return:
    """
    return os.stat(path).st_size


def delete(path: (str,)):
    os.remove(path)


def move(src: (str,), dest: (str,)):
    """
    will delete src
    :param src:
    :param dest:
    :return:
    """
    shutil.move(src, dest)


def get_dir(path: (str,)):
    """
    complete path: /home/moses/test.txt will return /home/moses
    :param path:
    :return:
    """
    return os.path.dirname(path)


def get_name(path: (str,)):
    """
    complete path: /home/moses/test.txt will return test.txt
    :param path:
    :return:
    """
    return os.path.basename(path)


def get_pure_name(path: (str,)):
    """
    complete path: /home/moses/test.txt will return test
    :param path:
    :return:
    """
    file_name, file_ext = os.path.splitext(get_name(path))
    return file_name


def get_ext(path: (str,)):
    """
    complete path: /home/moses/test.txt will return .txt
    :param path:
    :return:
    """
    file_name, file_ext = os.path.splitext(path)
    return file_ext


def get_pure_ext(path: (str,)):
    """
    complete path: /home/moses/test.txt will return txt
    :param path:
    :return:
    """
    ext = get_ext(path)
    return ext[1::] if ext else ""


def get_files_recursive(path: (str,)):
    files = []
    for (_path, _dirs, _files) in os.walk(path):
        for _file in _files:
            file_path = _path + "\\" + _file
            files.append(file_path)

    return files


def group_by_size(paths: (list,)):
    groups = {}
    for file_path in paths:
        groups.setdefault(get_size(file_path), []).append(file_path)

    return groups


def group_by_md5_until(paths: (list,), extent: (int,)):
    groups = {}
    for path in paths:
        groups.setdefault(Hash.md5_until(path, extent), []).append(path)

    return groups


def group_by_md5(paths: (list,), filter_func: (types.FunctionType,) = None):
    """
    group_by_md5
    :param paths:
    :param filter_func:
    :return:
    """
    if filter_func is not None and not hasattr(filter_func, '__call__'):
        raise RuntimeError("filter_func must be function-like type")

    def predicate(k1, v1):
        return filter_func is not None and not filter_func(k1, v1)

    x1 = group_by_size(paths)
    CollectionUtils.remove(x1, predicate)

    x2 = {}
    for key, value in x1.items():
        for k, v in group_by_md5_until(value, 4096).items():
            x2.setdefault(k, []).extend(v)
    CollectionUtils.remove(x2, predicate)

    x3 = {}
    for key, value in x2.items():
        for path in value:
            x3.setdefault(Hash.md5(path), []).append(path)
    CollectionUtils.remove(x3, predicate)

    return x3
