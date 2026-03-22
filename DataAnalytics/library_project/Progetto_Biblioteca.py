# Progetto Biblioteca 

biblioteca = {}

def aggiungi_libro(titolo, copie):
    try:
        copie = int(copie)
        if(copie < 0):
            raise ValueError ("Il numero inserito deve essere positivo")
        if(titolo in biblioteca):
            biblioteca[titolo] += copie
        else:
            biblioteca[titolo] = copie
    except(ValueError) as e:
        print("Input utente non valido", e)

    return biblioteca

def rimuovi_libro(titolo):
    if (titolo in biblioteca):
        biblioteca.pop(titolo)
    else:
        print("Il titolo non è in biblioteca")

def verifica_disponibilita(titolo):
    if (titolo in biblioteca and biblioteca[titolo] > 0):
        return True
    else:
        return False
    
def prendi_in_prestito(titolo):
    if (verifica_disponibilita(titolo) == True):
        biblioteca[titolo] -= 1
        print(biblioteca)
    else:
        print("Non c'è.")

def statistiche_biblioteca():
    totale_libri = len(biblioteca)
    copie_totali = sum(biblioteca.values())
    media_copie = copie_totali/totale_libri
    print(f"La biblioteca ha un numeri di titoli pari a:", totale_libri,"\nE ha un numero di copie totali pari a:", copie_totali,"\nLa media di copie per libro è:", round(media_copie, 2))

def visualizza_libri():
    if(len(biblioteca) != 0):
        for libri in biblioteca: 
            print(libri, biblioteca[libri])
    else:
        print("Non ci sono libri in biblioteca.")

def restaurare_libro(titolo, copie):
    if(verifica_disponibilita(titolo) == True):
        biblioteca[titolo] += copie
    else:
        print("Errore")

ex = ""
while(ex != "Esci"):
    ex = input()
    if(ex == "Aggiungi libro"):
        t = input()
        c = int(input())
        aggiungi_libro(t, c)
    if(ex == "Rimuovi libro"):
        t = input()
        rimuovi_libro(t)
    if(ex == "Verifica disponibilità"):
        t = input()
        verifica_disponibilita(t)
    if(ex == "Prendi in prestito"):
        t = input()
        prendi_in_prestito(t)
    if(ex == "Statistiche"):
        statistiche_biblioteca()
    if(ex == "Visualizza libri"):
        visualizza_libri()
    if(ex == "Restaurare libro"):
        t = input()
        c = int(input())
        restaurare_libro(t, c)
    else:
        print("Nessuna delle opzioni che hai selezionato è disponibile.") 
