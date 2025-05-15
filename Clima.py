import urllib.request
import urllib.parse
import json

def obtener_clima(ciudad, api_key):
    ciudad_codificada = urllib.parse.quote(ciudad)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad_codificada}&appid={api_key}&units=metric&lang=es"

    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            jsonData = json.loads(data)
            
            print("\n--- Resultado del clima ---")
            print(f"Ciudad: {jsonData['name']}")
            print(f"Temperatura: {jsonData['main']['temp']}°C")
            print(f"Descripción: {jsonData['weather'][0]['description']}")
            print(f"Humedad: {jsonData['main']['humidity']}%")
            print(f"Viento: {jsonData['wind']['speed']} m/s")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("Ciudad no encontrada.")
        elif e.code == 401:
            print("API Key inválida o no autorizada.")
        else:
            print(f"Error HTTP: {e.code}")
    except Exception as e:
        print("Ocurrió un error:", e)

# Solicitar datos al usuario
ciudad = input("Ingrese la ciudad: ")

# Llamar a la función
obtener_clima(ciudad, api_key)