import json

with open("archivo.json", "r" ) as archivo:
    carga_de_datos = json.load(archivo)

carga_de_datos["name"] = "camilo"

with open("archivo.json", "w" ) as archivo:
    carga_de_datos = json.load(archivo)


print(json.dump(carga_de_datos, indent=4))