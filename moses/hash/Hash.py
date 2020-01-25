import hashlib


def md5(path: (str,)):
    if not isinstance(path, (str,)):
        raise RuntimeError("path must be type in (str,)")

    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)

    return hash_md5.hexdigest()


def md5_until(path: (str,), extent: (int, )):
    if not isinstance(path, (str,)):
        raise RuntimeError("path must be type in (str,)")

    if not isinstance(extent, (int, )):
        raise RuntimeError("extent must be type in (int,)")

    hash_md5 = hashlib.md5()
    with open(path, "rb") as f:
        hash_md5.update(f.read(extent))
        return hash_md5.hexdigest()
