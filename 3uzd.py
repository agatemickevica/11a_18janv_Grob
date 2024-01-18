def lasit_trešo_rindu(teksta_faila_nosaukums):
    try:
        with open(teksta_faila_nosaukums, 'r', encoding='utf-8') as teksta_faila:
            visas_rindas = teksta_faila.readlines()
            if len(visas_rindas) >= 3:
                tresa_rinda = visas_rindas[2]
                print(tresa_rinda)
            else:
                print("Failā nav pietiekami daudz rindu.")
    except FileNotFoundError:
        print(f"Faila '{teksta_faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")