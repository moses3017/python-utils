import types


def remove(dictionary: (dict,), predicate: (types.FunctionType,) = None):
    for k in [k for k, v in dictionary.items() if predicate(k, v)]:
        del dictionary[k]
