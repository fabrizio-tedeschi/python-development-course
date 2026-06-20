anno_nascita = int(input("Inserire anno di nascita: "))
anno_futuro = int(input("Inserire anno futuro: "))

if anno_futuro < anno_nascita:
    print("Errore: inserito anno precedente all'anno di nascita.")
else:
    anni = anno_futuro - anno_nascita
    print(f"Nell'anno {anno_futuro} avrai {anni} anni.")