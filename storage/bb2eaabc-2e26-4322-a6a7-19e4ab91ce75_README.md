# README - Semáforo simple con Arduino UNO

## Objetivo didáctico
Este proyecto permite aprender a controlar LEDs desde Arduino, simulando el funcionamiento básico de un semáforo. Podrás practicar el uso de salidas digitales, entender el papel de las resistencias y familiarizarte con el conexionado básico.

---

## Instrucciones paso a paso

1. **Preparar los materiales:**  
   - 1 Arduino UNO  
   - 1 Protoboard  
   - 3 LEDs (rojo, amarillo, verde)  
   - 3 resistencias (220Ω – 330Ω)  
   - Jumpers

2. **Coloca los LEDs** en la protoboard, separados para evitar cortocircuitos.  
   - Recuerda: La pata larga del LED es el positivo (ánodo).

3. **Conecta una resistencia** a cada LED desde el cátodo (pata corta) hacia la barra negativa de la protoboard.

4. **Une la barra negativa al GND** del Arduino con un jumper.

5. **Conecta la pata larga** de cada LED a los pines digitales 2, 3 y 4 del Arduino (cada uno con un jumper).

6. **Carga el sketch.ino en el Arduino** desde el IDE de Arduino.

7. **Observa** cómo los LEDs se encienden uno a uno, simulando el ciclo de un semáforo.

---

## Tip práctico

- **Muy importante:** Asegúrate de no conectar las dos patas del LED al mismo riel, y revisa siempre que la resistencia vaya en serie con el LED, nunca en paralelo. Esto evitará daños tanto a los LEDs como al Arduino.

---

### Componentes usados (insert SQL):

INSERT INTO componentes (nombre, cantidad) VALUES
('Arduino UNO', 1),
('Protoboard', 1),
('LED', 3),
('Resistencia', 3),
('Jumpers', 6);

---

¡Listo! Con estos pasos armarás un circuito claro, sencillo y útil para aprender los fundamentos de electrónica y Arduino.