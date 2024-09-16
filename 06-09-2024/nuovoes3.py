def decoratore(funz):
    def wrapper(stringa):
        print(f"Sto analizzando la stringa {stringa}")
        risultato = funz(stringa)  
        print(f"Stringa compressa: {risultato}")
        return risultato
    return wrapper


@decoratore
def comprimi_stringa(stringa):
    for i in stringa:
        conteggio = stringa.count(i)
        if conteggio > 1:
            stringa_compressa = stringa.replace(i*conteggio, i + str(conteggio))
    return stringa_compressa if len(stringa_compressa) < len(stringa) else stringa

comprimi_stringa("ciaaao")