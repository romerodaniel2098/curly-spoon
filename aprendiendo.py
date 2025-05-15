# Importamos las librerías necesarias
import urllib.request  # Para hacer la conexión con la página web (API)
import urllib.parse    # Para codificar correctamente el nombre de la ciudad
import json            # Para convertir la respuesta en un formato que Python entienda

# Esta función se encarga de buscar el clima de una ciudad
def obtener_clima(ciudad, api_key):
    # Codificamos el nombre de la ciudad (por ejemplo: Medellín -> Medell%C3%ADn)
    ciudad_codificada = urllib.parse.quote(ciudad)

    # Construimos el enlace (URL) que se usará para pedir los datos del clima
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad_codificada}&appid={api_key}&units=metric&lang=es"

    # Imprimimos el enlace solo para revisar si está bien construido
    print("\nConsultando clima en:", ciudad)

    try:
        # Abrimos la conexión con la URL
        with urllib.request.urlopen(url) as respuesta:
            # Leemos la respuesta (viene en formato JSON)
            datos = respuesta.read()

            # Convertimos la respuesta JSON en un diccionario de Python
            clima = json.loads(datos)

            # Mostramos algunos datos importantes del clima
            print("\n--- Información del Clima ---")
            print("Ciudad:", clima['name'])
            print("Temperatura:", clima['main']['temp'], "°C")
            print("Clima:", clima['weather'][0]['description'])
            print("Humedad:", clima['main']['humidity'], "%")
            print("Viento:", clima['wind']['speed'], "m/s")

    # Si la ciudad no se encuentra
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print("No se encontró la ciudad. Intenta escribirla correctamente.")
        elif e.code == 401:
            print("API Key no válida o vencida.")
        else:
            print("Error al hacer la solicitud:", e.code)

    # Por si ocurre algún otro error inesperado
    except Exception as e:
        print("Ocurrió un error inesperado:", e)

# --------- Código principal ---------

# Pedimos al usuario que escriba una ciudad
ciudad_usuario = input("Escribe el nombre de la ciudad: ")

# Escribimos nuestra API Key (tú ya la tienes)
mi_api_key = "4ac2e84cf05f015229d7842b309bf2a0"

# Llamamos a la función para mostrar el clima
obtener_clima(ciudad_usuario, mi_api_key)