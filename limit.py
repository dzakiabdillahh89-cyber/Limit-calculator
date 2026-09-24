import math

def hitung_limit():
    print("=== KALKULATOR LIMIT SMP KELAS 8 ===")
    print("Menghitung lim (x->0) (sqrt(x+4)-2)/x")
    
    for x in [0.1, 0.01, 0.001, 0.0001]:
        hasil = (math.sqrt(x+4) - 2) / x
        print(f"x={x} -> hasil={hasil}")
    
    print("\nMendekati 0.25 = 1/4")
    print("Dibuat oleh calon engineer TUM")

hitung_limit()