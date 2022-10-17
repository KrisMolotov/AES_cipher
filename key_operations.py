from bitarray import bitarray


def xor(a: bytearray, b: bytearray) -> bytearray:
    len_a = len(a)
    len_b = len(b)
    if len_a != len_b:
        raise Exception("Error! Lengths of arguments for XOR are not equal! {0}, {1}".format(len_a, len_b))
    c = bytearray()
    for i in range(0, len_a):
        c.append(a[i] ^ b[i])
    return c


def invert(data: bytearray) -> bytearray:
    bits = bitarray()
    bits.frombytes(data)
    bits.reverse()
    return bytearray(bits.tobytes())
