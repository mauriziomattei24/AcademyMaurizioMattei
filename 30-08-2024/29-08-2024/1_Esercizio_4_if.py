nome = input("inserisci il nome:")
password = input("inserisci password:")

nome_corretto = "Maurizio"
password_corretta = "CIAO"
domanda_sicurezza_corretta = "Micio"


if nome != nome_corretto or password != password_corretta:
    print("Account non trovato")
    scelta = input("Vuoi Registrarti?: ")
    if scelta == "Si":
        nuovo_nome = input("inserisci nuovo nome :")
        nuova_password = input("inserisci nuova password :")
    elif scelta == "No":
        scelta_recupera_password = input("Imposta nuova password?")
        if scelta_recupera_password == "Si":
            domanda_sicurezza = input("Qual è il nome del tuo primo gatto?")
            if domanda_sicurezza == domanda_sicurezza_corretta:
                password_aggiornata = input("aggiornare password:")
                if len(password_aggiornata) > 8:
                    print("password valida")
                    print("Benvenuto")
                else:
                    print("password troppo corta")
            else:
                print("Risposta sbagliata")
        else:
            print("Errore Login")
    else:
        print("Esci")
else:
    print("Login avvenuto")
    