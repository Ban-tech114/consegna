#chiediamo all'utente informazioni per poter creare il nome della band
while True:

    citta_di_origine = input("In quale città sei cresciuto?: ")
    nome_del_tuo_gatto = input("Qual'è il nome del tuo gatto?: ")

    #creiamo la variabile per il nome della band
    nome_della_band = citta_di_origine + nome_del_tuo_gatto

    #restituiamo l'output all'utente con il nome della sua band e chiediamo se gli piaccia o meno
    risposta = input(f"Ecco qui il nome della tua band: {nome_della_band}, ti piace? (si/no): ").lower() #uti
    #verifichiamo la risposta dell'utente
    if (risposta == "si"):
        print("Fantastico buona fortuna con la tua nuova band!")
        break #termina il ciclo e quindi lo script
    elif (risposta == "no"):
        print("Nessun problema, proviamone un'altro")
    else:
        print("Perfavore rispondi con 'si' o 'no'")