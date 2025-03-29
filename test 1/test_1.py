import random

def igra():
    print("Dobrodošao u igru pogađanja broja!")
    print("Pogađaj broj između 1 i 100.")
    
    # Računanje slučajnog broja između 1 i 100
    tacan_broj = random.randint(1, 100)
    
    pokusaji = 0
    pogodjen = False
    
    # Petlja koja traje dok igrač ne pogodi broj
    while not pogodjen:
        try:
            # Unos broja od strane korisnika
            korisnicki_broj = int(input("Unesi broj: "))
            pokusaji += 1
            
            # Proverava da li je korisnik pogodio broj
            if korisnicki_broj < tacan_broj:
                print("Broj je veći. Pokušaj ponovo.")
            elif korisnicki_broj > tacan_broj:
                print("Broj je manji. Pokušaj ponovo.")
            else:
                pogodjen = True
                print(f"Čestitam! Pogodio si broj {tacan_broj} u {pokusaji} pokušaja.")
        
        except ValueError:
            print("Molim te unesi važeći broj.")
            
if __name__ == "__main__":
    igra()

