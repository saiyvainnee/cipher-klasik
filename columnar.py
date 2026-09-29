"""Columnar Transposition Cipher.
Plainteks ditulis per baris sebanyak panjang kunci, dibaca per kolom
sesuai urutan alfabet huruf pada kata kunci."""


def _bersihkan(teks):
    return "".join(c for c in teks.upper() if c.isalpha())


def _urutan_kolom(kunci):
    kunci = kunci.upper()
    return sorted(range(len(kunci)), key=lambda i: (kunci[i], i))


def encrypt(teks, kunci, pad="X"):
    teks = _bersihkan(teks)
    m = len(kunci)
    teks += pad * (-len(teks) % m)  # lengkapi baris terakhir dengan huruf dummy
    return "".join(teks[c::m] for c in _urutan_kolom(kunci))


def decrypt(teks, kunci):
    m = len(kunci)
    n_baris = len(teks) // m
    kolom = [""] * m
    for i, c in enumerate(_urutan_kolom(kunci)):
        kolom[c] = teks[i * n_baris:(i + 1) * n_baris]
    return "".join(kolom[c][r] for r in range(n_baris) for c in range(m))