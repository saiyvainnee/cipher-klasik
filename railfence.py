"""Rail Fence Cipher: plainteks ditulis zigzag pada k baris, dibaca baris per baris."""


def _pola(n, k):
    """Nomor baris untuk tiap posisi huruf (0,1,..,k-1,k-2,..,1,0,...)"""
    if k == 1:
        return [0] * n
    siklus = list(range(k)) + list(range(k - 2, 0, -1))
    return [siklus[i % len(siklus)] for i in range(n)]


def _bersihkan(teks):
    return "".join(c for c in teks.upper() if c.isalpha())


def encrypt(teks, k):
    teks = _bersihkan(teks)
    baris = [""] * k
    for ch, r in zip(teks, _pola(len(teks), k)):
        baris[r] += ch
    return "".join(baris)


def decrypt(teks, k):
    n = len(teks)
    pola = _pola(n, k)
    urutan = sorted(range(n), key=lambda i: (pola[i], i))
    hasil = [""] * n
    for ch, idx in zip(teks, urutan):
        hasil[idx] = ch
    return "".join(hasil)