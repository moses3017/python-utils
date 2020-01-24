import os


class File:
    """

    """

    def __init__(self, path):
        if not isinstance(path, str):
            raise RuntimeError("path must be str type.")

        self._path = path
        self._stat = os.stat(path)

    def get_size(self):
        """

        :return:
        """
        return self._stat.st_size

    def get_path(self):
        """

        :return:
        """
        return self._path
