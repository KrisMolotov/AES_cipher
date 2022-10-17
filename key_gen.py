from key_operations import invert, xor


def key_generation(key: bytearray) -> list:
    key_list = []
    key1 = invert(key)
    key2 = xor(key, key1)
    key_list.append(key)
    key_list.append(key1)
    key_list.append(key2)
    return key_list
