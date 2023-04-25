# Opret et tomt dictionary til at gemme personoplysninger
personer = {}

# Lav en funktion til at tilføje en ny person
def tilføj_person():
    navn = input("Indtast navn: ")
    efternavn = input("Indtast efternavn: ")
    by = input("Indtast by: ")
    postnummer = input("Indtast postnummer: ")
    skole = input("Indtast skole: ")
    klasse = input("Indtast klasse: ")
    alder = input("Indtast alder: ")
    personer[navn] = {
        "Efternavn": efternavn,
        "By": by,
        "Postnummer": postnummer,
        "Skole": skole,
        "Klasse": klasse,
        "Alder": alder
    }

# Lav en loop, der giver mulighed for at tilføje nye personer
while True:
    svar = input("Vil du tilføje en ny person? (ja/nej): ")
    if svar.lower() == "ja":
        tilføj_person()
    else:
        break

# Lav en funktion til at printe personer med en bestemt alder
def print_personer_med_alder(alder):
    print(f"Personer med alder {alder}:")
    for navn, oplysninger in personer.items():
        if oplysninger["Alder"] == alder:
            print(f"{navn} {oplysninger['Efternavn']}")

# Brug funktionen til at printe personer med alder 20
print_personer_med_alder("20")
