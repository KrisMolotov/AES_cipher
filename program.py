import argparse
from function import function


def createParser():
    prs = argparse.ArgumentParser(prog='Cipher', description='AES study cipher in ECB and CBC forms')
    prs.add_argument('-v', '--version', action='version', version='%(prog)s 1.0.0', help="Program version")
    prs.add_argument('-m', '--mode', choices=['ecb', 'cbc'], required=True, help="Choose mode for AES")
    prs.add_argument('-e', '--enc', action='store_true', help="encryption flag")
    prs.add_argument('-d', '--dec', action='store_true', help="decryption flag")
    prs.add_argument('-k', '--key', required=True, help="32-bit key in hex")
    prs.add_argument('-i', '--iv', help="32-bit initialization vector for CBC mode.")
    prs.add_argument('-g', '--debug', action='store_true', help="flag for displaying all intermediate values")
    prs.add_argument('filename', help="File with plaintext/cipher")
    return prs


parser = createParser()
args = parser.parse_args()
file_path = args.filename
mode = args.mode
iv = args.iv
debug = args.debug
enc = args.enc
dec = args.dec

if __name__ == '__main__':
    try:
        if mode == 'cbc' and iv is None:
            raise Exception('You must use iv in CBC algorithm')
        key = bytearray.fromhex(args.key)
        data = bytearray.fromhex(open(args.filename, 'r').read())
        res = function(data, key, mode, debug, iv, enc).hex()
        print(res)
    except Exception as message:
        print(message)
