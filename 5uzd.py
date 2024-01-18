def ievadit_un_ierakstit_faila():
    try:
        # Ievada lietotāja vārdu
        lietotaja_vards = input("Ievadiet savu vārdu: ")

        # Ieraksta lietotāja vārdu teksta failā
        with open('lietotajs.txt', 'w', encoding='utf-8') as faila:
            faila.write(lietotaja_vards)

        print(f"Lietotāja vārds '{lietotaja_vards}' veiksmīgi ierakstīts failā 'lietotajs.txt'.")

    except PermissionError:
        print("Nav atļaujas rakstīt failā 'lietotajs.txt'.")
    except Exception as e:
        print(f"Radās kļūda: {e}")
