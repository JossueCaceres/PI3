// Ejemplo educativo: Encender y apagar tres LEDs secuencialmente
// Este sketch prende cada LED por un segundo, uno tras otro
// Objetivo: entender cómo controlar salidas digitales en Arduino

// Definimos los pines digitales en los que conectaremos los LEDs
const int led1 = 2; // LED 1 conectado al pin digital 2
const int led2 = 3; // LED 2 conectado al pin digital 3
const int led3 = 4; // LED 3 conectado al pin digital 4

void setup() {
  // Inicializamos los pines de los LEDs como salidas
  pinMode(led1, OUTPUT); // Pin 2 como salida
  pinMode(led2, OUTPUT); // Pin 3 como salida
  pinMode(led3, OUTPUT); // Pin 4 como salida
  // (No es necesario inicializar los pines de las resistencias; éstas van en serie con el LED)
}

void loop() {
  // Encendemos el LED 1 y apagamos los demás
  digitalWrite(led1, HIGH); // Encender LED 1
  digitalWrite(led2, LOW);  // Apagar LED 2
  digitalWrite(led3, LOW);  // Apagar LED 3
  delay(1000);              // Espera 1 segundo

  // Encendemos el LED 2 y apagamos los demás
  digitalWrite(led1, LOW);  // Apagar LED 1
  digitalWrite(led2, HIGH); // Encender LED 2
  digitalWrite(led3, LOW);  // Apagar LED 3
  delay(1000);              // Espera 1 segundo

  // Encendemos el LED 3 y apagamos los demás
  digitalWrite(led1, LOW);  // Apagar LED 1
  digitalWrite(led2, LOW);  // Apagar LED 2
  digitalWrite(led3, HIGH); // Encender LED 3
  delay(1000);              // Espera 1 segundo
  // El ciclo se repite indefinidamente
}