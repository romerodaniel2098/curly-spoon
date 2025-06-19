// sistema_interactivo.js

// Captura de datos
let userName = prompt("¿Cuál es tu nombre?");
let userAge = prompt("¿Cuántos años tienes?");

// Expresiones regulares
let nombreValido = /^[a-zA-Z\s]+$/.test(userName);  // Solo letras y espacios
let edadValida = /^\d+$/.test(userAge);             // Solo dígitos

// Validaciones
if (!nombreValido) {
    alert("Error: El nombre debe contener solo letras y no estar vacío.");
    console.error("Nombre inválido: debe contener solo letras.");
} else if (!edadValida) {
    alert("Error: Por favor, ingresa una edad válida con solo números.");
    console.error("Edad inválida: debe contener solo números.");
} else {
    // Convertimos a número
    userAge = Number(userAge);

    if (userAge < 18) {
        alert(`Hola ${userName}, eres menor de edad. ¡Sigue aprendiendo y disfrutando del código!`);
    } else {
        alert(`Hola ${userName}, eres mayor de edad. ¡Prepárate para grandes oportunidades en el mundo de la programación!`);
    }
}