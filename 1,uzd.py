def lasit_un_drukaj_failu(ceils_uz_failu):
    try:
        with open(ceils_uz_failu, 'r') as faila_objekts:
            saturs = faila_objekts.read()
            print("Faila saturs:")
            print(saturs)
    except FileNotFoundError:
        print(f"Kļūda: Fails '{ceils_uz_failu}' nav atrasts.")
    except Exception as e:
        print(f"Kļūda: Neizdevās nolasīt failu. Kļūda: {e}")
