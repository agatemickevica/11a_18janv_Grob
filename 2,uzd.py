import csv

def lasit_otro_kolonnu(csv_faila_nosaukums):
    try:
        with open(csv_faila_nosaukums, 'r', newline='', encoding='utf-8') as csv_faila:
            csv_lasitajs = csv.reader(csv_faila)
            for rinda in csv_lasitajs:
                if len(rinda) > 1:  # Pārliecināties, ka rinda satur vismaz divus elementus
                    otra_kolonna = rinda[1]
                    print(otra_kolonna)
    except FileNotFoundError:
        print(f"Faila '{csv_faila_nosaukums}' nav atrasts.")
    except Exception as e:
        print(f"Radās kļūda: {e}")

# Aizstājiet 'tavs_faila_nosaukums.csv' ar patieso CSV faila nosaukumu
lasit_otro_kolonnu('tavs_faila_nosaukums.csv')