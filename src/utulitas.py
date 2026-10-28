import random


def buat_soal():
    """Membuat soal operasi hitung campuran."""
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    operasi = random.choice(["+", "-", "*"])

    if operasi == "+":
        soal = f"{a} + {b} * {c}"
    elif operasi == "-":
        soal = f"{a} * {b} - {c}"
    else:
        soal = f"{a} + {b} * {c}"

    return soal


def hitung_jawaban(soal):
    """Menghitung jawaban soal berdasarkan aturan matematika."""
    try:
        bagian = soal.split()

        a = int(bagian[0])
        operasi1 = bagian[1]
        b = int(bagian[2])
        operasi2 = bagian[3]
        c = int(bagian[4])

        ekspresi = f"{a} {operasi1} {b} {operasi2} {c}"

        # Evaluasi terbatas untuk operasi aritmetika yang diizinkan.
        if any(kata not in "0123456789+-* /" for kata in ekspresi):
            raise ValueError("Ekspresi tidak valid")

        return eval(ekspresi, {"__builtins__": {}}, {})
    except (ValueError, IndexError, TypeError, SyntaxError):
        raise ValueError("Soal tidak valid")