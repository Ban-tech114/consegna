import math

#chiediamo all'utente di quale figura geometrica vuole calcolare il perimetro
print("Dimmi pure, di quale figura geometrica vuoi sapere il perimetro? ")
print("1. Quadrato")
print("2. Cerchio")
print("3. Rettangolo")

scelta = input("Inserisci il numero corrispondente alla tua scelta (1, 2 o 3): ")

if(scelta == '1'):
    #calcoliamo il perimetro del quadrato
    lato = float(input("Inserisci il lato del  quadrato: "))
    perimetro = lato * 4
    print(f"Il perimetro del tuo quadrato è: {perimetro}")
elif(scelta == '2'):
    #calcoliamo la circonferenza del cerchio
    raggio = float(input("Inserisci il raggio del cerchio: "))
    circonferenza = 2 * math.pi * raggio
    print(f"La circonferenza del cerchio è: {circonferenza}")
elif(scelta == '3'):
    #calcoliamo la circonferenza del cerchio 
    base = float(input("Inserisci la base del rettangolo: "))
    altezza = float(input("Inserisci l'altezza del rettangolo: "))
    perimetro = (base * 2) + (altezza * 2)
    print(f"Il perimetro del rettangolo è: {perimetro}")
else:
    print("Mi dispiace non ho ancora studiato altre fighure geometriche")
