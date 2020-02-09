import configparser

from moses.file import FileUtils


def write(config: (dict,), path: (str,)):
    """
    config format:
        [section1]
        key1 = value1
        key2 = value2
        [section2]
        key3 = value3
        key5 = value4
    :param path:
    :param config: {section: {key: value...}...}
    :return:
    """
    cp = configparser.RawConfigParser()
    for section, kvs in config.items():
        cp.add_section(section)
        for k, v in kvs.items():
            cp.set(section, k, v)

    FileUtils.create_dirs(FileUtils.get_dir(path))
    with open(path, "w", encoding="utf-8-sig") as f:
        cp.write(f)


def read(path: (str,)):
    """
    return dict contains section, key, value
    :param path:
    :return: {section: {key: value...}...}
    """
    if not FileUtils.is_file(path):
        return {}

    cp = configparser.RawConfigParser()
    cp.read(path, encoding="utf-8-sig")
    return {section: {k: v for k, v in cp.items(section)} for section in cp.sections()}
