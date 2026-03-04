##raccolta richieste clienti
'''
#leggere il file
import csv

with open("requests.csv","r" ) as f:
    reader = csv.DictReader(f)
    requests = list(reader)

#print(requests)

#validare i dati

for row in requests:
    try:
        if "@" in row["email"] and \
        int(row["eta"]) >= 18 and \
        row["nome"].strip() != "":
            row["valid_row"] = True
        else:
            row["valid_row"] = False

    except Exception as e:
        row["valid_row"] = False
        row["error"] = e

    #print(row)

#filtro richieste scartate

valid_requests = []
for r in requests:
    if r["valid_row"] == True:
        valid_requests.append(r)

#for vr in valid_requests:
#    print(vr)

#sanificazione dati

for vr in valid_requests:
    vr["id"] = vr["id"].strip()
    vr["nome"] =" ".join(vr["nome"].strip().title().split())
    vr["email"] = vr["email"].strip().lower()
    vr["eta"] = vr["eta"].strip()
    vr["servizio"] = " ".join(vr["servizio"].strip().title().split())
    vr.pop("valid_row")
    #print(vr)

#aggiungere campo categoria eta

#test
#valid_requests[0]["eta"] = "dieci"

for vr in valid_requests:
    try:
        if int(vr["eta"]) >= 40:
            vr["categoria"] = "Senior"
        elif int(vr["eta"]) >= 26:
            vr["categoria"] = "Adult"
        elif int(vr["eta"]) >= 18:
            vr["categoria"] = "Junior"

    except Exception as e:
        print(f" request {vr["id"]}: error {e}")

for r in valid_requests:
    print(r)


n_requests = len(valid_requests)
print(n_requests)
#organizzare i dati
#valid_requests ok

#set servizi richiesti
services_list = []

for vr in valid_requests:
    services_list.append(vr["servizio"])

distinct_services = set(services_list)
#print(distinct_services)

#conteggio richieste per servizio (dict)


count_services = [0] * len(distinct_services)
dict_count_services = {}
for i in range(len(distinct_services)):

    for vr in valid_requests:
        if vr["servizio"] == list(distinct_services)[i]:
            count_services[i] +=1
    dict_count_services[list(distinct_services)[i]] = count_services[i]
#print(count_services)
print(dict_count_services)


request_objects = []
for vr in valid_requests:
    request = Request(
        id = vr["id"],
        nome = vr["nome"],
        email = vr["email"],
        eta = vr["eta"],
        servizio = vr["servizio"],
        categoria = vr["categoria"]
    )
    request_objects.append(request)

for r in request_objects:
    print(r.nome)
'''

import csv

class Request:

    def __init__(self, id, nome, email, eta, servizio, categoria):
        self.id = id
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio
        self.categoria = categoria
        self.valid_row = True
        self.error = None



class Validator:
    def __init__(self):
        pass

    def validate(self):
        try:

            if "@" in self.email and int(self.eta) >= 18 and self.nome.strip() != "":
                self.valid_row = True
            else:
                self.valid_row = False

        except Exception as e:
            self.valid_row = False
            self.error = e

    def sanitize(self):
        self.id = self.id.strip()
        self.nome = " ".join(self.nome.strip().title().split())
        self.email = self.email.strip().lower()
        self.eta = self.eta.strip()
        self.servizio = " ".join(self.servizio.strip().title().split())


    def add_categoria(self):
        try:
            if int(self.eta) >= 40:
                self.categoria = "Senior"
            elif int(self.eta) >= 26:
                self.categoria = "Adult"
            elif int(self.eta) >= 18:
                self.categoria = "Junior"

        except Exception as e:
            print(f" request {self.id}: error {e}")


class Pipeline:
    def __init__(self):
        pass

    def import_csv(self):
        with open("requests.csv", "r") as f:
            reader = csv.DictReader(f)
            requests = list(reader)
        return requests




###CODICE

#import and validate
requests = Pipeline().import_csv()
#print(requests)
valid_requests = []
for r in requests:
    value = Validator(r).validate()
    valid_requests.append(value)
#sanification
sanitized_requests = []
for r in valid_requests:
    r.Validator().sanitize()
    sanitized_requests.append(r)

#add category
complete_requests = []
for r in sanitized_requests:
    r.Validator().add_categoria()
    complete_requests.append(r)

#object trasnformation
request_objects = []
for r in complete_requests:
    r = Request(
        id=r["id"],
        nome=r["nome"],
        email=r["email"],
        eta=r["eta"],
        servizio=r["servizio"],
        categoria=r["categoria"]
    )
    request_objects.append(r)


print(request_objects)

n_requests = len(request_objects)
print(n_requests)
#organizzare i dati
#valid_requests ok

#set servizi richiesti
services_list = []

for r in request_objects:
    services_list.append(r.servizio)

distinct_services = set(services_list)
#print(distinct_services)

#conteggio richieste per servizio (dict)

count_services = [0] * len(distinct_services)
dict_count_services = {}
for i in range(len(distinct_services)):

    for r in request_objects:
        if r.servizio == list(distinct_services)[i]:
            count_services[i] +=1
    dict_count_services[list(distinct_services)[i]] = count_services[i]
#print(count_services)
print(dict_count_services)


