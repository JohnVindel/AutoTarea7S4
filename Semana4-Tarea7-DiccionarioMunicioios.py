#*****Examen, Ejercicio 5 - Diccionario de Municipios*****#

municipios = {
    "Cortes": "San Pedro Sula",
    "Copan": "Santa Rosa de Copan",
    "Francisco Morazan": "Tegucigalpa",
    "Intibuca": "La Esperanza",
    "Comayagua": "Comayagua"
}

try:
    intro = input("Ingrese el Municipio: ")
    print("El Municipio es {} y tiene como cabecera a {}.".format(intro, format(municipios[intro], )))
except KeyError:
    print ("El municipio que ingreso no existe")