def somma(a, b):
    return a + b

def main():
    print("Calcolatore avviato")
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))
    print("Risultato somma:", somma(a, b))

if __name__ == "__main__":
    main()