def lasit_un_drukāt_faila_saturs():
    try:
        # Ievada faila nosaukumu no lietotāja
        faila_nosaukums = input("Ievadiet faila nosaukumu: ")

        # Ievada faila formātu (paplašinājumu) no lietotāja
        faila_formats = input("Ievadiet faila formātu (paplašinājumu, piemēram, txt): ")

        # Izveido pilno faila ceļu, pievienojot paplašinājumu faila nosaukumam
        pilns_fails = f"{faila_nosaukums}.{faila_formats}"

        # Atver failu un nolasa tā saturu
        with open(pilns_fails, 'r', encoding='utf-8') as faila:
            saturs = faila.read()

        # Izdrukā faila saturu
        print(f"Faila '{pilns_fails}' saturs:")
        print(saturs)

    except FileNotFoundError:
        print(f"Faila '{pilns_fails}' nav atrasts.")
    except PermissionError:
        print(f"Nav atļaujas lasīt failu '{pilns_fails}'.")
    except Exception as e:
        print(f"Radās kļūda: {e}")