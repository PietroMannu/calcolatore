def somma(a, b):
    return a + b

def divisione(a, b):
    if b == 0:
        return "Errore: Divisione per zero impossibile"
    return a / b

def main():
    print("Calcolatore avviato")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print("Risultato somma:", somma(a, b))
    print("Risultato divisione:", divisione(a, b))

if __name__ == "__main__":
    main()