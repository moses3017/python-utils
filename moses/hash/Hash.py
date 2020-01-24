import hashlib
from moses.file.File import File


class Hash:
    """

    """

    @staticmethod
    def md5(file: (str, File)):
        if not isinstance(file, (str, File)):
            raise RuntimeError("file must be type in (str, File)")

        file_path = file if isinstance(file, str) else file.get_path()
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        return hash_md5.hexdigest()

    @staticmethod
    def md5_until(file: (str, File), extent: (int, )):
        if not isinstance(file, (str, File)):
            raise RuntimeError("file must be type in (str, File)")

        if not isinstance(extent, (int, )):
            raise RuntimeError("extent must be type in (int,)")

        file_path = file if isinstance(file, str) else file.get_path()
        hash_md5 = hashlib.md5()
        with open(file_path, "rb") as f:
            hash_md5.update(f.read(extent))
            return hash_md5.hexdigest()

