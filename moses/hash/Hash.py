import _hashlib
import hashlib


def md5(path: (str,)):
    return _hash(path, hashlib.md5())


def md5_until(path: (str,), extent: (int,) = 4096):
    return _hash_until(path, hashlib.md5(), extent)


def sha1(path: (str,)):
    return _hash(path, hashlib.sha1())


def _hash(path: (str,), hash_object: (_hashlib.HASH,)):
    return _hash_until(path, hash_object)


def _hash_until(path: (str,), hash_object: (_hashlib.HASH,), extent: (int,) = -1):
    """
    common hash until
    :param path:
    :param hash_object:
    :param extent: <0: unlimited, 0: empty, >0: limited
    :return:
    """
    if not isinstance(path, (str,)):
        raise RuntimeError("path must be type in (str,)")

    if not isinstance(extent, (int,)):
        raise RuntimeError("extent must be type in (int,)")

    default_chunk_size = 4096
    x = {"extent": extent}

    def _next():
        chunk_t = b""
        if x["extent"] < 0:
            chunk_t = f.read(default_chunk_size)
        elif x["extent"] == 0:
            pass
        elif x["extent"] > default_chunk_size:
            chunk_t = f.read(default_chunk_size)
            x["extent"] -= default_chunk_size
        else:
            chunk_t = f.read(x["extent"])
            x["extent"] = 0

        return chunk_t

    with open(path, "rb") as f:
        while chunk := _next():
            hash_object.update(chunk)

    return hash_object.hexdigest()
