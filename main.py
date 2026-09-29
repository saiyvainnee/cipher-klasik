import caesar
import railfence
import columnar


def menu_caesar():
    op = input("[1] Enkripsi  [2] Dekripsi  [3] Brute force: ")
    teks = input("Teks: ")
    if op == "3":
        for k, hasil in caesar.brute_force(teks).items():
            print(f"k={k:2d}  {hasil}")
        return
    k = int(input("Kunci (0-25): "))
    print("Hasil:", caesar.encrypt(teks, k) if op == "1" else caesar.decrypt(teks, k))


def menu_railfence():
    op = input("[1] Enkripsi  [2] Dekripsi: ")
    teks = input("Teks: ")
    k = int(input("Jumlah rail: "))
    print("Hasil:", railfence.encrypt(teks, k) if op == "1" else railfence.decrypt(teks, k))


def menu_columnar():
    op = input("[1] Enkripsi  [2] Dekripsi: ")
    teks = input("Teks: ")
    kunci = input("Kata kunci (huruf berbeda): ")
    print("Hasil:", columnar.encrypt(teks, kunci) if op == "1" else columnar.decrypt(teks, kunci))


def main():
    while True:
        print("\n=== CIPHER KLASIK ===")
        print("1. Caesar Cipher\n2. Rail Fence Cipher\n3. Columnar Transposition\n0. Keluar")
        pilih = input("Pilih menu: ")
        if pilih == "1":
            menu_caesar()
        elif pilih == "2":
            menu_railfence()
        elif pilih == "3":
            menu_columnar()
        elif pilih == "0":
            break


if __name__ == "__main__":
    main()