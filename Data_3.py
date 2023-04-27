import json

# Opretter en JSON fil med informationer
data = {
    "navn": "John",
    "efternavn": "Doe",
    "alder": 30
}

with open("min_json_fil.json", "w") as f:
    json.dump(data, f)

# Hent en JSON fil fra nettet
with open("User list(1).json", "r") as f:
    user_list = json.load(f)

# Hent en bestemt information fra de to filer
navn = user_list[0]["fornavn"]
alder = data["alder"]

print("Navn:", navn)
print("Alder:", alder)

# Skriv en bestemt information til de to filer
data["alder"] = 31

with open("min_json_fil.json", "w") as f:
    json.dump(data, f)

user_list[0]["alder"] = 25

with open("User list(1).json", "w") as f:
    json.dump(user_list, f)
