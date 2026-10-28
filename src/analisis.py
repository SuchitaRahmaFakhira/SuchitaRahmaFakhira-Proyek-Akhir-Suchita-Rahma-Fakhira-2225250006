def periksa_jawaban(jawaban_pengguna, jawaban_benar):
    """Memeriksa apakah jawaban pengguna benar."""
    try:
        return float(jawaban_pengguna) == float(jawaban_benar)
    except (ValueError, TypeError):
        return False


def hitung_nilai(jumlah_benar, jumlah_soal):
    """Menghitung nilai akhir dalam skala 100."""
    if jumlah_soal <= 0:
        return 0

    return (jumlah_benar / jumlah_soal) * 100