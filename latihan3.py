def tarik_uang(saldo):
    try:
        jumlah = int(input("Masukkan jumlah penarikan: "))
        if jumlah > saldo:
            print("Saldo tidak mencukupi!")
            return saldo
        elif jumlah <= 0:
            print("Jumlah penarikan harus lebih dari 0!")
            return saldo
        else:
            saldo -= jumlah
            print("Penarikan berhasil!")
            return saldo
    except ValueError:
        print("Masukkan nominal yang valid!")
        return saldo

def atm_sederhana():
    saldo = 1000000  # Saldo awal Rp 1.000.000
    
    while True:
        print(f"\nSaldo saat ini: Rp {saldo}")
        print("1. Tarik Uang")
        print("2. Keluar")
        
        try:
            pilihan = input("Pilih menu (1/2): ")
            
            if pilihan == "1":
                saldo = tarik_uang(saldo)
            elif pilihan == "2":
                print("Terima kasih telah menggunakan ATM.")
                break
            else:
                print("Pilihan tidak valid! Silahkan pilih 1 atau 2")
        except ValueError:
            print("Masukkan pilihan yang valid!")

# Menjalankan program ATM
atm_sederhana()