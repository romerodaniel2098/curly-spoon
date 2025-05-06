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
         "product": "Creatina",
        "value": 100, 
        "cantidad":10
    },
    {
        "product": "Proteina",
        "value": 250,
        "cantidad": 20
    },
    {
        "product": "Aminoacidos",
        "value": 80,
        "cantidad": 15
    },
    {
        "product": "Mancuernas_de_250_kg",
        "value": 50,
        "cantidad": 100 
    },
    {
        "product": "Banda elastica",
        "value": 20,
        "cantidad":100
    },
]

for suplement in listasuplements:
    print(f"product:{suplement["product" ]} value:{suplement["value" ]}, quantity:{suplement["cantidad" ]} ")


 