#pedimos al usuario la edad

#edad=int(input("porfavor, ingresa tu edad: "))

#if edad <12:
#    print("eres un niño")
#elif edad >12 and edad <=17:
#    print ("eres un adolescente")
#elif edad >17 and edad <=59: 
#    print ("eres un adulto")
#else:
#    print("eres un adulto mayor.")
    

listasuplements = [
    {
         "product": "creatina",
        "value": 100, 
        "cantidad":10
    },
    {
        "product": "proteina",
        "value": 250,
        "cantidad": 20
    },
    {
        "product": "aminoacidos",
        "value": 80,
        "cantidad": 15
    },
    {
        "product": "mancuernas_de_250_kg",
        "value": 50,
        "cantidad": 100 
    },
]

for suplemento in listasuplements:
    print(f"producto: {suplemento["product"]}, precio:{suplemento["value"]}, cantidad:{suplemento["cantidad"]}")


 