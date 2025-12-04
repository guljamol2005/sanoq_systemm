def bin_to_oct(binary: str) -> str:
    return oct(int(binary, 2))[2:]

def dec_to_bin(decimal: int) -> str:
    return bin(decimal)[2:]

def hex_to_bin(hex_num: str) -> str:
    return bin(int(hex_num, 16))[2:]

def oct_to_bin(octal: str) -> str:
    return bin(int(octal, 8))[2:]

def bin_to_dec(binary: str) -> int:
    return int(binary, 2)
