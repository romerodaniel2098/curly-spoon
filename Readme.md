
# Gestión de Inventario - Semana 1

Este programa en Python implementa un sistema básico de gestión de inventario. A través de un menú interactivo, el usuario puede añadir, consultar, actualizar, eliminar productos y calcular el valor total del inventario.

---

## Explicación paso a paso

### 1. Función `añadir_producto(inventario, nombre, precio, cantidad)`
- **Objetivo**: Agrega un nuevo producto al inventario si aún no existe.
- **Parámetros**:
  - "inventario": diccionario principal que guarda los productos.
  - "nombre": nombre del producto.
  - "precio": precio unitario del producto.
  - "cantidad": número de unidades disponibles.
- **Proceso**:
  - Verifica si el producto ya existe.
  - Si no existe, lo añade como una tupla "(precio, cantidad)" al diccionario.

---

### 2. Función `consultar_producto(inventario, nombre)`
- **Objetivo**: Muestra la información de un producto específico.
- **Parámetros**:
  - "inventario": el diccionario con todos los productos.
  - "nombre": nombre del producto a buscar.
- **Proceso**:
  - Usa ".get()" para buscar el producto.
  - Si lo encuentra, muestra su precio y cantidad.
  - Si no, indica que el producto no se encuentra.

---

### 3. Función `actualizar_precio(inventario, nombre, nuevo_precio)`
- **Objetivo**: Actualiza el precio de un producto existente.
- **Parámetros**:
  - "inventario": el diccionario de productos.
  - "nombre": producto a actualizar.
  - "nuevo_precio": nuevo valor del producto.
- **Proceso**:
  - Busca el producto y conserva la cantidad actual.
  - Reemplaza la tupla con el nuevo precio y la misma cantidad.

---

### 4. Función `eliminar_producto(inventario, nombre)`
- **Objetivo**: Elimina un producto del inventario si existe.
- **Parámetros**:
  - "inventario": el diccionario que contiene todos los productos.
  - "nombre": producto a eliminar.
- **Proceso**:
  - Verifica si existe y lo elimina con "del".

---

### 5. Función `valor_total_inventario(inventario)`
- **Objetivo**: Calcula el valor total del inventario.
- **Parámetros**:
  - "inventario": el diccionario completo de productos.
- **Proceso**:
  - Multiplica el precio por la cantidad de cada producto.
  - Suma todos los valores y lo imprime.

---

### 6. Función `solicitar_float(mensaje)`
- **Objetivo**: Solicita al usuario un número decimal (float) validado.
- **Proceso**:
  - Pide al usuario un número.
  - Si no es válido, solicita nuevamente.

---

### 7. Función `solicitar_int(mensaje)`
- **Objetivo**: Solicita un número entero validado.
- **Proceso**:
- Similar a "solicitar_float" pero usando "int()".

---

### 8. Función `menu()`
- **Objetivo**: Interfaz principal del programa.
- **Proceso**:
  - Muestra opciones del menú al usuario.
  - Llama a las funciones correspondientes según la opción elegida.
  - Mantiene el programa en bucle hasta que el usuario seleccione salir ("0").

---

## Estructura del Inventario

El inventario es un diccionario donde:
- **Clave**: nombre del producto.
- **Valor**: tupla con el formato "(precio, cantidad)".

Ejemplo:
```python
inventario = {
    "Leche": (2.5, 10),
    "Pan": (1.0, 20)
}
```


