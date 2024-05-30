def get_Key(nested_obj: dict):
    keys = list(nested_obj)
    if len(keys) != 1:
        raise Exception('Either there are multiple keys or the empty dictionary been found')
    else:
        return keys[0]


def get_Value(nested_obj: dict, key: str, isFound = False):
    if type(nested_obj) is not dict and not isFound:
        return None
    if (isFound or (key in nested_obj.keys())) :
        if type(nested_obj[key]) is dict:
            return get_Value(nested_obj[key], get_Key(nested_obj[key]), True)
        else:
            return nested_obj[get_Key(nested_obj)]
    else:
        nestedKey = get_Key(nested_obj)
        return get_Value(nested_obj[nestedKey], key, False)

if __name__ == '__main__':
    nested_obj = {'a': {'b': {'c': 'd'}}}
    nested_value = get_Value(nested_obj, 'b')
    print(nested_value)
