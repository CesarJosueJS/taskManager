import os
import json
import unittest
import tempfile
from unittest.mock import patch
from io import StringIO

from task_manager import Task, TaskManager


class TestTask(unittest.TestCase):
    def test_task_initialization_default(self):
        task = Task(1, "Comprar leche")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Comprar leche")
        self.assertFalse(task.completed)

    def test_task_initialization_completed(self):
        task = Task(2, "Estudiar Python", completed=True)
        self.assertEqual(task.id, 2)
        self.assertEqual(task.description, "Estudiar Python")
        self.assertTrue(task.completed)

    def test_task_str_representation(self):
        task_pending = Task(1, "Pendiente", completed=False)
        task_done = Task(2, "Hecho", completed=True)

        self.assertEqual(str(task_pending), "[ ] #1: Pendiente")
        self.assertEqual(str(task_done), "[✅] #2: Hecho")


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        # Crear un archivo temporal aislado para no modificar el tasks.json real
        self.temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".json")
        self.temp_file.close()

        self.patcher_file = patch.object(TaskManager, "FILENAME", self.temp_file.name)
        self.patcher_file.start()

        # Silenciar salidas por consola durante los tests y evitar errores de codificación en Windows
        self.patcher_stdout = patch("sys.stdout", new_callable=StringIO)
        self.mock_stdout = self.patcher_stdout.start()

        # Instanciar TaskManager con archivo limpio
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)
        self.manager = TaskManager()

    def tearDown(self):
        self.patcher_stdout.stop()
        self.patcher_file.stop()
        if os.path.exists(self.temp_file.name):
            os.remove(self.temp_file.name)

    def test_initial_state_empty(self):
        self.assertEqual(len(self.manager._tasks), 0)
        self.assertEqual(self.manager._next_id, 1)

    def test_add_task(self):
        self.manager.add_task("Aprender testing")
        self.assertEqual(len(self.manager._tasks), 1)
        self.assertEqual(self.manager._tasks[0].id, 1)
        self.assertEqual(self.manager._tasks[0].description, "Aprender testing")
        self.assertFalse(self.manager._tasks[0].completed)
        self.assertEqual(self.manager._next_id, 2)

        # Verificar persistencia en archivo
        with open(self.temp_file.name, "r") as f:
            data = json.load(f)
            self.assertEqual(len(data), 1)
            self.assertEqual(data[0]["description"], "Aprender testing")

    def test_add_multiple_tasks(self):
        self.manager.add_task("Tarea 1")
        self.manager.add_task("Tarea 2")
        self.assertEqual(len(self.manager._tasks), 2)
        self.assertEqual(self.manager._tasks[0].id, 1)
        self.assertEqual(self.manager._tasks[1].id, 2)
        self.assertEqual(self.manager._next_id, 3)

    def test_complete_task_success(self):
        self.manager.add_task("Tarea a completar")
        self.manager.complete_task(1)
        self.assertTrue(self.manager._tasks[0].completed)

        # Verificar persistencia
        with open(self.temp_file.name, "r") as f:
            data = json.load(f)
            self.assertTrue(data[0]["completed"])

    def test_complete_task_not_found(self):
        self.manager.add_task("Tarea existente")
        self.manager.complete_task(999)
        self.assertIn("Tarea no encontrada: #999", self.mock_stdout.getvalue())
        self.assertFalse(self.manager._tasks[0].completed)

    def test_delete_task_success(self):
        self.manager.add_task("Tarea 1")
        self.manager.add_task("Tarea 2")
        self.manager.delete_task(1)

        self.assertEqual(len(self.manager._tasks), 1)
        self.assertEqual(self.manager._tasks[0].id, 2)

    def test_delete_task_not_found(self):
        self.manager.add_task("Tarea 1")
        self.manager.delete_task(999)
        self.assertIn("Tarea no encontrada: #999", self.mock_stdout.getvalue())
        self.assertEqual(len(self.manager._tasks), 1)

    def test_delete_all_tasks(self):
        self.manager.add_task("Tarea 1")
        self.manager.add_task("Tarea 2")
        self.manager.add_task("Tarea 3")

        self.manager.delete_all_tasks()
        self.assertEqual(len(self.manager._tasks), 0)

        # Verificar persistencia tras borrar todo
        with open(self.temp_file.name, "r") as f:
            data = json.load(f)
            self.assertEqual(data, [])

    def test_list_task_empty(self):
        self.manager.list_task()
        self.assertIn("No hay tareas pendientes", self.mock_stdout.getvalue())

    def test_list_task_with_elements(self):
        self.manager.add_task("Tarea 1")
        self.manager.list_task()
        self.assertIn("[ ] #1: Tarea 1", self.mock_stdout.getvalue())

    def test_load_tasks_existing_file(self):
        initial_data = [
            {"id": 1, "description": "Guardada 1", "completed": False},
            {"id": 5, "description": "Guardada 5", "completed": True}
        ]
        with open(self.temp_file.name, "w") as f:
            json.dump(initial_data, f)

        loaded_manager = TaskManager()
        self.assertEqual(len(loaded_manager._tasks), 2)
        self.assertEqual(loaded_manager._tasks[0].id, 1)
        self.assertEqual(loaded_manager._tasks[1].id, 5)
        self.assertTrue(loaded_manager._tasks[1].completed)
        self.assertEqual(loaded_manager._next_id, 6)


if __name__ == "__main__":
    unittest.main()
