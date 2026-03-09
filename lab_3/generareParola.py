import random
import string

def genereaza_cuvinte_mnemonice(capitalize_prima_litera=True):
  
    culori = ["alb", "rosu", "verde", "albastru", "galben", "portocaliu"]
    animale = ["caine", "pisica", "sarpel", "maimuta", "leu", "tigru"]
    elemente_naturii = ["copac", "floare", "pamant", "apa", "foc", "vent"]
    ceruri = ["luna", "soare", "starea", "planeta", "cometa", "galaxie"]

    # Selectam cate un cuvant din fiecare set
    cuvant_culoare = random.choice(culori)
    cuvant_animal = random.choice(animale)
    cuvant_element = random.choice(elemente_naturii)
    cuvant_cer = random.choice(ceruri)

    # Aplicam capitalizarea daca este specificat
    if capitalize_prima_litera:
        cuvant_culoare = cuvant_culoare.capitalize()
        cuvant_animal = cuvant_animal.capitalize()
        cuvant_element = cuvant_element.capitalize()
        cuvant_cer = cuvant_cer.capitalize()

    return [cuvant_culoare, cuvant_animal, cuvant_element, cuvant_cer]

def genereaza_parola_puternica(
    lungime,
    cuvinte_mnemonice,
    foloseste_caractere_speciale=True,
    foloseste_cifre=True,
    amesteca_parola=True
):

    caractere_speciale = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if foloseste_caractere_speciale else ""
    cifre = string.digits if foloseste_cifre else ""
    litere = string.ascii_letters  # Include atat litere mici cat si mari

    # Construim o baza pentru parola din cuvinte mnemonice
    parola_baza = ''.join(cuvinte_mnemonice)

    # Daca lungimea dorita este mai mare decat lungimea bazei, adaugam alte caractere
    caractere_suplimentare = litere + caractere_speciale + cifre
    if len(parola_baza) < lungime:
        caractere_ramase = lungime - len(parola_baza)
        parola_baza += ''.join(random.choices(caractere_suplimentare, k=caractere_ramase))

    # Amestecam parola finala daca este specificat
    if amesteca_parola:
        parola_finala = ''.join(random.sample(parola_baza, len(parola_baza)))
    else:
        parola_finala = parola_baza[:lungime]  # Trunchiem la lungimea specificata

    return parola_finala

def main():
    print("Generator de parole puternice folosind mnemonice")

    # Configurarea parolei
    lungime = int(input("Introduceti lungimea parolei: "))
    foloseste_caractere_speciale = input("Doriti sa includeti caractere speciale? (da/nu): ").strip().lower() == 'da'
    foloseste_cifre = input("Doriti sa includeti cifre? (da/nu): ").strip().lower() == 'da'
    capitalize_prima_litera = input("Doriti sa capitalizati prima litera a cuvintelor mnemonice? (da/nu): ").strip().lower() == 'da'
    amesteca_parola = input("Doriti sa amestecati parola generata? (da/nu): ").strip().lower() == 'da'

    # Genereaza cate un cuvant din fiecare set
    cuvinte_mnemonice = genereaza_cuvinte_mnemonice(capitalize_prima_litera=capitalize_prima_litera)
    print(f"Cuvinte mnemonice alese: {' '.join(cuvinte_mnemonice)}")
    
    # Genereaza parola puternica
    parola_puternica = genereaza_parola_puternica(
        lungime,
        cuvinte_mnemonice,
        foloseste_caractere_speciale=foloseste_caractere_speciale,
        foloseste_cifre=foloseste_cifre,
        amesteca_parola=amesteca_parola
    )
    print(f"Parola generata: {parola_puternica}")

if __name__ == "__main__":
    main()