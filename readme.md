# Cipher Klasik
Nama: Sayidina Ramadhan

NIM : 312410112

Tiga aplikasi cipher klasik dalam Python (tanpa dependency tambahan):

| File | Jenis | Kunci |
|------|-------|-------|
| `caesar.py` | Substitusi abjad-tunggal (+ brute force) | angka 0-25 |
| `railfence.py` | Transposisi | jumlah rail |
| `columnar.py` | Transposisi | kata kunci (huruf berbeda) |

## Cara menjalankan
```
python main.py
```

## Tes otomatis
```
python tes_semua.py
```

## Contoh
- Caesar, k=5: `ADA RENCANA PENYELUNDUPAN NARKOBA DI BANDARA` -> `FIF WJSHFSF UJSDJQZSIZUFS SFWPTGF IN GFSIFWF`
- Rail Fence, k=3: `CRYPTOGRAPHY AND DATA SECURITY` -> `CTAAAEIRPORPYNDTSCRTYGHDAUY`
- Columnar, kunci TOMBAK: `sistem dan teknologi informasi itb` -> `EEGRTTTOOIMKIMBSNLFIIAONSSDNIA`
