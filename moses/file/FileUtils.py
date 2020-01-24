import os
from moses.file.File import File
from moses.hash.Hash import Hash


class FileUtils:
    """

    """
    def __init__(self):
        pass

    @staticmethod
    def get_size(path: (str,)):
        return File(path).get_size()

    @staticmethod
    def delete(path: (str,)):
        os.remove(path)

    @staticmethod
    def get_files_recursive(path: (str,)):
        files = []
        for (_path, _dirs, _files) in os.walk(path):
            for _file in _files:
                file_path = _path + "\\" + _file
                files.append(file_path)

        return files

    @staticmethod
    def group(path: (str,)):
        """
        group by size, md5_until, md5
        :param path:
        :return:
        """
        x1 = FileUtils.group_by_size(FileUtils.get_files_recursive(path))

        x2 = {}
        for key, value in x1.items():
            if len(value) > 1:
                x2.update(FileUtils.group_by_md5_until(value, 4096))

        x3 = {}
        for key, value in x2.items():
            if len(value) > 1:
                x3.update(FileUtils.group_by_md5(value))

        return x3

    @staticmethod
    def group_by_size(paths: (list,)):
        groups = {}
        for file_path in paths:
            groups.setdefault(FileUtils.get_size(file_path), []).append(file_path)

        return groups

    @staticmethod
    def group_by_md5_until(paths: (list,), extent: (int,)):
        groups = {}
        for path in paths:
            groups.setdefault(Hash.md5_until(path, extent), []).append(path)

        return groups

    @staticmethod
    def group_by_md5(paths: (list,)):
        groups = {}
        for path in paths:
            groups.setdefault(Hash.md5(path), []).append(path)

        return groups

