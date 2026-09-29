import caesar, railfence, columnar

# Tugas 1: Caesar (soal Latihan slide 9)
c = caesar.encrypt("ADA RENCANA PENYELUNDUPAN NARKOBA DI BANDARA", 5)
print("Caesar    :", c)
print("Brute force XMZVH k=21:", caesar.brute_force("XMZVH")[21])

# Tugas 2: Rail Fence (contoh slide 44)
c = railfence.encrypt("CRYPTOGRAPHY AND DATA SECURITY", 3)
print("Rail Fence:", c)
print("Dekripsi  :", railfence.decrypt(c, 3))

# Tugas 3: Columnar, kunci TOMBAK (contoh slide 42)
c = columnar.encrypt("sistem dan teknologi informasi itb", "TOMBAK")
print("Columnar  :", c)
print("Dekripsi  :", columnar.decrypt(c, "TOMBAK"))