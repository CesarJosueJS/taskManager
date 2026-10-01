import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

# Conectamos con el endpoint de Google Gemini usando la librería de OpenAI
client = OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

def create_simple_tasks(description):
    if not client.api_key:
        return ["Error: La API key de Gemini no está configurada en el archivo .env."]

    try:
        prompt = f"""Desglosa la siguiente tarea compleja en una lista de 3 a 5 subtareas simples y accionables.

Tarea: {description}

Formato de respuesta:
- Subtarea 1
- Subtarea 2
- Subtarea 3
- etc.

Responde solo con la lista de subtareas, una por línea, empezando cada línea con un guión."""

        params = {
            "model": "gemini-3.5-flash-lite",
            "messages": [
                {"role": "system", "content": "Eres un asistente experto en gestión de tareas que ayuda a dividir tareas complejas en pasos simples y accionables."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 300
        }

        response = client.chat.completions.create(**params)
        content = response.choices[0].message.content.strip()

        subtasks = []
        for line in content.split("\n"):
            line = line.strip()
            if line and line.startswith("-"):
                subtask = line[1:].strip()
                if subtask:
                    subtasks.append(subtask)

        return subtasks if subtasks else ["Error: No se han podido generar las subtareas."]

    except Exception as e:
        return [f"Error: {e}"]
