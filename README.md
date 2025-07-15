# Proyecto Urban Grocers 

Este proyecto automatiza las pruebas de la API de Urban Grocers para validar la creación de **kits de productos**. 
Se realizaron 9 pruebas automatizadas según la lista de comprobación.
---
## 📁 Estructura de archivos

- `configuration.py`: contiene la URL base y las rutas de los endpoints.
- `data.py`: define los cuerpos de solicitud para los usuarios y los kits.
- `sender_stand_request.py`: funciones que envían las solicitudes a la API.
- `create_kit_name_kit_test.py`: contiene las pruebas automatizadas del campo `name` del kit.
- `.gitignore`: evita subir archivos innecesarios al repositorio.
- `README.md`: este archivo.

---

## ▶️ Cómo ejecutar las pruebas

Se debe tener instalado `pytest`.

   pip install pytest

Ejecuta las pruebas con este comando:

pytest create_kit_name_kit_test.py

✅ Lista de pruebas automatizadas
#	Descripción de la prueba	Resultado Esperado
1	Nombre con 1 carácter	201
2	Nombre con 511 caracteres	201
3	Nombre vacío	400
4	Nombre con 512 caracteres	400
5	Nombre con caracteres especiales	201
6	Nombre con espacios	201
7	Nombre con números	201
8	No se envía el parámetro name	400
9	Tipo de dato incorrecto en name (número)	400

📌 Notas
Algunas pruebas están diseñadas para fallar si la API no valida correctamente los datos.

💻 Tecnologías
Python 3.13
Pytest
PyCharm