def czy_rok_przestepny(rok):
    if (rok % 4 == 0 and rok % 100 != 0) or (rok % 400 == 0):
        return True
    else:
        return False

# Przykład użycia:
rok = int(input("Podaj rok: "))
if czy_rok_przestepny(rok):
    print(f"Rok {rok} jest rokiem przestępnym.")
else:
    print(f"Rok {rok} nie jest rokiem przestępnym.")
