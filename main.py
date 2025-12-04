def bin_to_oct(binary: str) -> str:
    return oct(int(binary, 2))[2:]

def dec_to_bin(decimal: int) -> str:
    return bin(decimal)[2:]
