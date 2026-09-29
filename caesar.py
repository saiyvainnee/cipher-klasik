"""Caesar Cipher: c = (p + k) mod 26, p = (c - k) mod 26"""


def encrypt(teks, k):
    hasil = ""
    for ch in teks:
        if ch.isalpha():
            awal = ord("A") if ch.isupper() else ord("a")
            hasil += chr((ord(ch) - awal + k) % 26 + awal)
        else:
            hasil += ch
    return hasil


def decrypt(teks, k):
    return encrypt(teks, -k)


def brute_force(cipherteks):
    """Exhaustive key search: coba semua k = 0..25"""
    return {k: decrypt(cipherteks, k) for k in range(26)}