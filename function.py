import aes_modes
from aes_modes import *
from key_gen import key_generation


def function(data: bytearray, key: bytearray, mode: str, debug_option=False, iv=None, encrypt_mode=True) -> bytearray:
    if len(key) != size_part_for_handling:
        raise Exception('Error! Incorrect size of key!')
    parts = [data[i: i + size_part_for_handling] for i in range(0, len(data), size_part_for_handling)]
    if len(parts[-1]) != size_part_for_handling:
        for i in range(len(parts[-1]), size_part_for_handling):
            parts[-1].append(0x00)
    k = key_generation(key)
    if debug_option:
        for i in range(1, 4):
            print("Key {}: ".format(i), k[i].hex)
    if mode == 'ecb':
        if encrypt_mode:
            return aes_modes.ECB_encrypt(parts, k, debug_option)
        else:
            return aes_modes.ECB_decrypt(parts, k, debug_option)
    elif mode == 'cbc' and iv is not None:
        iv_byte = bytearray.fromhex(iv)
        if len(iv_byte) != size_part_for_handling:
            raise Exception("Error! Incorrect size of IV!")
        if encrypt_mode:
            return aes_modes.CBC_encrypt(parts, k, iv_byte, debug_option)
        else:
            return aes_modes.CBC_decrypt(parts, k, iv_byte, debug_option)
    else:
        raise Exception("Error! Choose the correct mode!")
