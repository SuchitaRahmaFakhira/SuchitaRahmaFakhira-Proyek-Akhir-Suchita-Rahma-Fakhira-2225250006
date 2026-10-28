def tampilkan_pesan(pesan):
    """Menampilkan pesan ke terminal."""
    print(pesan)


def minta_jawaban(soal):
    """Menampilkan soal dan meminta jawaban pengguna."""
    print(f"Soal: {soal}")
    return input("Jawaban kamu: ").strip()


def minta_jumlah_soal():
    """Meminta jumlah soal dari pengguna."""
    while True:
        try:
            jumlah = int(input("Masukkan jumlah soal: "))

            if jumlah > 0:
                return jumlah

            print("Jumlah soal harus lebih dari 0.")
        except ValueError:
            print("Input tidak valid. Masukkan bilangan bulat.")