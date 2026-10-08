def somma(a, b):
    return a + b

def sottrazione(a, b):
    return a - b

def moltiplicazione(a, b):
    return a * b

def divisione(a, b):
    if b == 0:
        return "Errore: Divisione per zero impossibile"
    return a / b

def modulo(a, b):
    if b == 0:
        return "Errore: Modulo per zero impossibile"
    return a % b

def main():
    print("Calcolatore avviato")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))

    print("Risultato somma:", somma(a, b))
    print("Risultato sottrazione:", sottrazione(a, b))
    print("Risultato moltiplicazione:", moltiplicazione(a, b))
    print("Risultato divisione:", divisione(a, b))
    print("Risultato modulo:", modulo(a, b))

if __name__ == "__main__":
    main()