from src.input_data import minta_jumlah_soal, minta_jawaban
from src.proses import buat_soal, periksa_jawaban, hitung_nilai
from src.output import tampilkan_hasil, simpan_hasil


def main():
    print("=" * 45)
    print("GENERATOR DAN EVALUASI SOAL")
    print("OPERASI HITUNG CAMPURAN")
    print("=" * 45)

    jumlah_soal = minta_jumlah_soal()
    jumlah_benar = 0

    for nomor in range(1, jumlah_soal + 1):
        soal = buat_soal()
        jawaban = minta_jawaban(nomor, soal["soal"])

        if periksa_jawaban(jawaban, soal["jawaban"]):
            print("Jawaban benar!")
            jumlah_benar += 1
        else:
            kunci = float(soal["jawaban"])
            print(f"Jawaban salah. Kunci: {kunci:g}")

    nilai = hitung_nilai(jumlah_benar, jumlah_soal)

    tampilkan_hasil(jumlah_soal, jumlah_benar, nilai)

    try:
        lokasi = simpan_hasil(
            jumlah_soal,
            jumlah_benar,
            nilai
        )
        print(f"Hasil disimpan di: {lokasi}")

    except OSError as error:
        print(f"Gagal menyimpan hasil: {error}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan.")