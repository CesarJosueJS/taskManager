# TaskManager 📝

Un gestor de tareas inteligente desarrollado en Python que permite crear, gestionar y completar tareas de forma eficiente. Incluye integración con IA para descomponer tareas complejas en subtareas más simples y accionables.

## 🚀 Características principales

- **Gestión básica de tareas**: Crear, listar, completar y eliminar tareas
- **Persistencia de datos**: Las tareas se guardan automáticamente en un archivo JSON
- **IA integrada**: Usa OpenAI GPT para descomponer tareas complejas en subtareas simples
- **Interfaz de línea de comandos**: Menú interactivo fácil de usar
- **Pruebas unitarias**: Suite completa de tests para garantizar la funcionalidad

## 🛠️ Tecnologías utilizadas

- **Python 3.13+**: Lenguaje principal
- **OpenAI API**: Para la funcionalidad de IA
- **JSON**: Almacenamiento de datos
- **unittest**: Framework de testing
- **python-dotenv**: Gestión de variables de entorno

## 📁 Estructura del proyecto

```
TaskManager/
├── main.py                 # Punto de entrada principal con menú interactivo
├── task_manager.py         # Lógica principal del gestor de tareas
├── ai_service.py          # Integración con OpenAI para descomponer tareas
├── test_task_manager.py   # Suite de pruebas unitarias
├── requirements.txt       # Dependencias del proyecto
├── tasks.json            # Archivo de persistencia de tareas
└── README.md             # Documentación del proyecto
```

## 🔧 Instalación y configuración

### Prerrequisitos

- Python 3.13 o superior
- API Key de OpenAI (opcional, solo para funciones de IA)

### Pasos de instalación

1. **Clona el repositorio**:
   ```bash
   git clone https://github.com/mouredev/taskmanager.git
   cd taskmanager
   ```

2. **Crea un entorno virtual**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En macOS/Linux
   # o
   .venv\Scripts\activate     # En Windows
   ```

3. **Instala las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la API de OpenAI** (opcional):
    - Crea un archivo `.env` en el directorio raíz
    - Añade tu API key:
      ```
      OPENAI_API_KEY=tu-api-key-aquí
      ```

## 🎮 Uso del programa

### Ejecutar la aplicación

```bash
python main.py
```

### Menú principal

El programa presenta un menú interactivo con las siguientes opciones:

1. **Añadir tarea**: Crear una nueva tarea simple
2. **Añadir tarea compleja (con IA)**: Usar IA para descomponer una tarea compleja
3. **Listar tareas**: Mostrar todas las tareas con su estado
4. **Completar tarea**: Marcar una tarea como completada
5. **Eliminar tarea**: Eliminar una tarea del sistema
6. **Salir**: Cerrar la aplicación

### Ejemplos de uso

#### Añadir una tarea simple
```
Elige una opción: 1
Descripción de la tarea: Comprar leche
Tarea añadida: Comprar leche
```

#### Añadir una tarea compleja con IA
```
Elige una opción: 2
Descripción de la tarea compleja: Organizar una fiesta de cumpleaños
```
La IA descompondrá esta tarea en subtareas como:
- Hacer lista de invitados
- Reservar lugar para la celebración
- Planificar el menú y comprar comida
- Decorar el espacio
- Coordinar actividades y entretenimiento

## 🧪 Pruebas

El proyecto incluye una suite completa de pruebas unitarias que cubren toda la funcionalidad principal.

### Ejecutar las pruebas

```bash
python -m unittest test_task_manager.py -v
```

### Cobertura de pruebas

Las pruebas cubren:
- ✅ Añadir tareas
- ✅ Eliminar tareas existentes
- ✅ Manejo de tareas inexistentes
- ✅ Listar tareas
- ✅ Completar tareas

## 📂 Persistencia de datos

Las tareas se almacenan automáticamente en el archivo `tasks.json` con la siguiente estructura:

```json
[
    {
        "id": 1,
        "description": "Descripción de la tarea",
        "completed": false
    }
]
```

## 🤖 Funcionalidad de IA

La integración con OpenAI permite:

- **Descomposición inteligente**: Convierte tareas complejas en 3-5 subtareas accionables
- **Manejo de errores**: Gestión robusta de fallos en la API
- **Configuración flexible**: Funciona sin IA si no se configura la API key

### Ejemplo de descomposición de IA

**Entrada**: "Aprender Python"

**Salida**:
- Instalar Python y configurar el entorno de desarrollo
- Estudiar los conceptos básicos (variables, tipos de datos, estructuras de control)
- Practicar con ejercicios de programación básica
- Crear un proyecto pequeño para aplicar lo aprendido
- Revisar y refactorizar el código creado

## 🔒 Seguridad

- Las API keys se gestionan a través de variables de entorno
- No se almacenan credenciales en el código fuente
- Manejo seguro de errores en las llamadas a la API

## 🚧 Limitaciones conocidas

- La funcionalidad de IA requiere conexión a internet
- Las tareas se almacenan en texto plano (sin encriptación)
- No hay funcionalidad de backup automático

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Para contribuir:

1. Fork del repositorio
2. Crea una rama para tu feature (`git checkout -b feature/nueva-caracteristica`)
3. Commit de tus cambios (`git commit -am 'Añadir nueva característica'`)
4. Push a la rama (`git push origin feature/nueva-caracteristica`)
5. Crea un Pull Request

## 📋 Roadmap

### Próximas características

- [ ] Interfaz gráfica de usuario (GUI)
- [ ] Categorías de tareas
- [ ] Fechas de vencimiento
- [ ] Recordatorios
- [ ] Exportar/importar tareas
- [ ] Búsqueda y filtrado avanzado
- [ ] Estadísticas de productividad

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👨‍💻 Autor

Desarrollado por [MoureDev](https://github.com/mouredev)

---

## 📞 Soporte

Si encuentras algún problema o tienes sugerencias:

- Abre un [issue](https://github.com/mouredev/taskmanager/issues)
- Contacta al desarrollador a través de [Twitter](https://twitter.com/mouredev)

---

*Proyecto desarrollado con 💙 en Python*