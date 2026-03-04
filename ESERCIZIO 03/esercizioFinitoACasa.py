import csv
import json

class Request:

    def __init__(self, id, nome, email, eta, servizio, categoria):
        self.id = id
        self.nome = nome
        self.email = email
        self.eta = eta
        self.servizio = servizio
        self.categoria = categoria


class Validator:

    def validate(self):
        try:

            if "@" in self["email"] and int(self["eta"]) >= 18 and self["nome"].strip() != "":
                self["valid_row"] = True
            else:
                self["valid_row"] = False

        except Exception as e:
            self["valid_row"] = False
            self["error"] = e

        return self

    def sanitize(self):
        self["id"] = self["id"].strip()
        self["nome"] = " ".join(self["nome"].strip().title().split())
        self["email"] = self["email"].strip().lower()
        self["eta"] = self["eta"].strip()
        self["servizio"] = " ".join(self["servizio"].strip().title().split())
        return self

    def add_categoria(self):
        try:
            if int(self["eta"]) >= 40:
                self["categoria"] = "Senior"
            elif int(self["eta"]) >= 26:
                self["categoria"] = "Adult"
            elif int(self["eta"]) >= 18:
                self["categoria"] = "Junior"

        except Exception as e:
            print(f" request {self["id"]}: error {e}")

        return self


class Pipeline:
    def __init__(self):
        pass

    def import_csv(self):
        with open("requests.csv", "r") as f:
            reader = csv.DictReader(f)
            requests = list(reader)
        return requests


    def export_json(self):
        with open("output.json", "w", newline = "") as f:
            writer = json.dump(self,f, indent = 4)




###Main
#import and validate
requests = Pipeline().import_csv()
for r in requests:
    print(r)

valid_requests = []
for r in requests:
    value = Validator.validate(r)
    valid_requests.append(value)

#filter
filtered_requests = []
for r in valid_requests:
    if r["valid_row"] == True:
        filtered_requests.append(r)

#sanification
sanitized_requests = []
for r in filtered_requests:
    value = Validator.sanitize(r)
    sanitized_requests.append(value)

#add category
complete_requests = []
for r in sanitized_requests:
    value = Validator.add_categoria(r)
    complete_requests.append(value)

for r in complete_requests:
    print(r)

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

for r in request_objects:
    print(r.nome)

request_dicts = [obj.__dict__ for obj in request_objects]

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

Pipeline.export_json(request_dicts)


