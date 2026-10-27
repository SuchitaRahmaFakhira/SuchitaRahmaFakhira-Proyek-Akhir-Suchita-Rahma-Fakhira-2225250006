import random


def buat_soal():
    angka1 = random.randint(1, 10)
    angka2 = random.randint(1, 10)
    angka3 = random.randint(1, 10)
    operasi = random.choice(["+", "-", "*"])

    soal = f"{angka1} {operasi} {angka2} + {angka3}"
    jawaban = eval(soal)

    return soal, jawaban


def main():
    print("=== GENERATOR SOAL ARITMETIKA ===")

    try:
        jumlah_soal = int(input("Masukkan jumlah soal: "))

        if jumlah_soal < 1:
            print("Jumlah soal minimal 1.")
            return

    except ValueError:
        print("Input harus berupa angka.")
        return

    benar = 0

    for nomor in range(1, jumlah_soal + 1):
        soal, kunci = buat_soal()
        print(f"\nSoal {nomor}: {soal}")

        try:
            jawaban = float(input("Jawaban kamu: "))

            if jawaban == kunci:
                print("Jawaban benar!")
                benar += 1
            else:
                print(f"Jawaban salah. Jawaban yang benar: {kunci}")

        except ValueError:
            print("Input harus berupa angka.")

    nilai = (benar / jumlah_soal) * 100

    print("\n=== HASIL LATIHAN ===")
    print(f"Jumlah soal : {jumlah_soal}")
    print(f"Jawaban benar: {benar}")
    print(f"Nilai akhir : {nilai:.2f}")


if __name__ == "__main__":
    main()