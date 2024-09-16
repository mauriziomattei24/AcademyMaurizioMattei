nome = input("inserisci il nome:")
password = input("inserisci password:")
id =input("inserisci id: ")

nome_corretto = "Maurizio"
password_corretta = "CIAO"
id_corretto = 123

if nome != nome_corretto or password != password_corretta or id != id_corretto:
    print("Account non trovato")
    scelta = input("Vuoi Registrarti?: ")
    if scelta == "Si":
        nuovo_nome = input("inserisci nuovo nome :")
        nuova_password = input("inserisci nuova password :")
        nuovo_id = input("inserisci nuovo id :")
    else:
        print("Esci")
else:
    print("Login avvenuto")
    
    


    