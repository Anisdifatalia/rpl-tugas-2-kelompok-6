def buat_soal():
    soal = "Berapakah hasil 2 + 2?"
    jawaban = "4"
    return soal, jawaban


def hitung_skor(jawaban, kunci):
    if jawaban == kunci:
        return 10
    return 0
print("Program kuis siap dijalankan!")