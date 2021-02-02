# Tarea Nro 3: Desarrollo de GUIs

## Problema

Desarrolle un programa con la siguiente interfaz.

Aplicar pruebas unitarias a las operaciones que realiza la calculadora.

Recomendación: Separe la lógica de la solución de cálculos a una clase independiente de la interfaz.

### Resultado

El diseño de mi calculadora difiere un poco al original, ademas del mismo funcionanmientos, se planteo que le usuario pueda escribir toda una operación compleja, y dando uso de la potente función `eval` que provee **Python**, se intenta evaluar la expresión, en el caso de poder se muestra el resultado y en caso de no poder evaluarla se muestra un `ERROR`.

#### Ejecutar pruebas unitarias

Desde el directorio raiz, ejecutamos en la tarminal

```bash
python -m unittest discover .\tests\
```
