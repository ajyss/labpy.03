def hitung_keuntungan():
    # Modal awal
    modal = 100000000  # 100 juta
    total_keuntungan = 0
    
    print("Modal awal:", format(modal, ','), "rupiah")
    print("\nPerhitungan laba per bulan:")
    
    for bulan in range(1, 9):  # 8 bulan
        if bulan < 3:  # Bulan 1-2
            laba_persen = 0
            laba = 0
        elif bulan < 5:  # Bulan 3-4
            laba_persen = 1
            laba = modal * (laba_persen/100)
        elif bulan < 8:  # Bulan 5-7
            laba_persen = 5
            laba = modal * (laba_persen/100)
        else:  # Bulan 8
            laba_persen = 3
            laba = modal * (laba_persen/100)
        
        total_keuntungan += laba
        
        print(f"Bulan ke-{bulan}:")
        print(f"Persentase laba: {laba_persen}%")
        print(f"Laba: Rp {format(int(laba), ',')}")
        print("-" * 40)
    
    print("\nTotal Keuntungan selama 8 bulan:")
    print("Rp", format(int(total_keuntungan), ','))
    
    return total_keuntungan

# Menjalankan fungsi
hitung_keuntungan()