# Importamos lo que necesitamos
import urllib.request  # Para conectarnos a internet y pedir información
import urllib.parse    # Para escribir bien el nombre de la ciudad en la URL
import json            # Para entender la respuesta que nos da la página

# Función que busca el clima de una ciudad
def obtener_clima(ciudad, api_key):
    # Codificamos el nombre de la ciudad (por si tiene acentos o espacios)
    ciudad_codificada = urllib.parse.quote(ciudad)

    # Creamos el enlace con la ciudad y nuestra clave secreta (API Key)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad_codificada}&appid={api_key}&units=metric&lang=es"

    print(f"\nBuscando el clima en: {ciudad}...")

    try:
        # Pedimos los datos a la página
        with urllib.request.urlopen(url) as respuesta:
            # Leemos lo que nos respondió la página
            datos = respuesta.read()

            # Convertimos esos datos a un formato que Python entiende
            clima = json.loads(datos)

            # Mostramos la información importante
            print("\n--- Clima Actual ---")
            print("Ciudad:", clima['name'])
            print("Temperatura:", clima['main']['temp'], "°C")
            print("Estado del cielo:", clima['weather'][0]['description'])
            print("Humedad:", clima['main']['humidity'], "%")
            print("Viento:", clima['wind']['speed'], "m/s")
            print(f"País: {clima["sys"]["country"]}")


    # Si escribimos mal la ciudad o hay un problema con la API
    except urllib.error.HTTPError as error:
        if error.code == 404:
            print("Ciudad no encontrada. Revisa el nombre.")
        elif error.code == 401:
            print("API Key incorrecta o vencida.")
        else:
            print("Error al consultar el clima. Código de error:", error.code)

    # Para otros errores inesperados
    except Exception as error:
        print("Ocurrió un error:", error)

# ---------- Código principal ----------

# Pedimos al usuario que escriba una ciudad
ciudad_usuario = input("¿De qué ciudad quieres saber el clima? ")

# Escribe aquí tu API Key de OpenWeather (debes tener una)
mi_api_key = "4ac2e84cf05f015229d7842b309bf2a0"

# Llamamos a la función para mostrar el clima
obtener_clima(ciudad_usuario, mi_api_key)