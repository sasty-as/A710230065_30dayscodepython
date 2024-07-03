while True:
    try:
        # Meminta input dari user
        user_input = input("Masukkan bilangan bulat: ")
        
        # Mengkonversi input menjadi bilangan bulat
        number = int(user_input)
        
        # Menghitung kuadrat dari bilangan bulat
        result = number ** 2
        
        # Mencetak hasil kuadrat
        print(f"Hasil kuadrat dari {number} adalah {result}")
        
        # Keluar dari loop jika input valid
        break
    
    except ValueError:
        # Menampilkan pesan error jika input tidak valid
        print("Input yang dimasukkan tidak valid! Silakan masukkan bilangan bulat yang valid.")
