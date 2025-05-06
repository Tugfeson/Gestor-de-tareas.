#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from taskmanager import TaskManager
from task import Task

class ConsoleUI:
    """
    Interfaz de usuario para la consola.
    """
    
    def __init__(self):
        self.task_manager = TaskManager()
        self.priority_options = ["alta", "normal", "baja"]
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_header(self, title):
        self.clear_screen()
        print("=" * 50)
        print(f"{title:^50}")
        print("=" * 50)
        print()
    
    def print_task(self, index, task):
         status = "[✓]" if task.completed else "[ ]"
         priority_symbol = {
             "alta": "⚠️ ",
             "normal": "• ",
             "baja": "- "
         }.get(task.priority.lower(), "• ")
         print(f"{index + 1}. {status} {priority_symbol}{task.title} ({task.category})")  # +1 aquí
    
    def display_tasks(self, tasks=None, show_details=False):
        if tasks is None:
            tasks = self.task_manager.get_tasks()
        if not tasks:
            print("No hay tareas que mostrar.")
            return
        for i, task in enumerate(tasks):
            self.print_task(i, task)
            if show_details:
                print(f"   Descripción: {task.description}")
                print(f"   Creada: {task.created_at}")
                if task.completed:
                    print(f"   Completada: {task.completed_at}")
                print()
    
    def add_task_menu(self):
        self.print_header("AÑADIR NUEVA TAREA")
        title = input("Título de la tarea: ").strip()
        if not title:
            print("El título no puede estar vacío.")
            return
        description = input("Descripción (opcional): ").strip()
        print("\nPrioridad:")
        for i, option in enumerate(self.priority_options):
            print(f"{i+1}. {option}")
        priority_choice = input(f"Seleccione prioridad (1-{len(self.priority_options)}): ").strip()
        priority = self.priority_options[1]
        try:
            choice = int(priority_choice)
            if 1 <= choice <= len(self.priority_options):
                priority = self.priority_options[choice-1]
        except ValueError:
            pass
        category = input("Categoría (por defecto 'general'): ").strip() or "general"
        task = Task(title, description, priority, category)
        self.task_manager.add_task(task)
        print("\n¡Tarea añadida con éxito!")
        input("\nPresione Enter para continuar...")
    
    def complete_task_menu(self):
        self.print_header("COMPLETAR TAREA")
        tasks = self.task_manager.get_tasks(filter_completed=False)
        if not tasks:
            print("No hay tareas pendientes para completar.")
            input("\nPresione Enter para continuar...")
            return
        self.display_tasks(tasks)
        task_index = input("\nIndique el número de la tarea a completar (o 'c' para cancelar): ").strip()
        if task_index.lower() == 'c':
            return
        try:
            index = int(task_index)
            if self.task_manager.complete_task(index):
                print("\n¡Tarea marcada como completada!")
            else:
                print("\nÍndice de tarea no válido.")
        except ValueError:
            print("\nPor favor, introduzca un número válido.")
        input("\nPresione Enter para continuar...")
    
    def view_tasks_menu(self):
        while True:
            self.print_header("VER TAREAS")
            print("Filtros:")
            print("1. Todas las tareas")
            print("2. Tareas pendientes")
            print("3. Tareas completadas")
            print("4. Filtrar por categoría")
            print("5. Filtrar por prioridad")
            print("6. Volver al menú principal")
            choice = input("\nElija una opción: ").strip()
            if choice == '1':
                self.print_header("TODAS LAS TAREAS")
                self.display_tasks(show_details=True)
            elif choice == '2':
                self.print_header("TAREAS PENDIENTES")
                tasks = self.task_manager.get_tasks(filter_completed=False)
                self.display_tasks(tasks, show_details=True)
            elif choice == '3':
                self.print_header("TAREAS COMPLETADAS")
                tasks = self.task_manager.get_tasks(filter_completed=True)
                self.display_tasks(tasks, show_details=True)
            elif choice == '4':
                category = input("\nIntroduzca la categoría a filtrar: ").strip()
                self.print_header(f"TAREAS - CATEGORÍA: {category.upper()}")
                tasks = self.task_manager.get_tasks(category=category)
                self.display_tasks(tasks, show_details=True)
            elif choice == '5':
                print("\nPrioridades disponibles:")
                for i, priority in enumerate(self.priority_options):
                    print(f"{i+1}. {priority}")
                priority_choice = input("Seleccione prioridad: ").strip()
                try:
                    index = int(priority_choice) - 1
                    if 0 <= index < len(self.priority_options):
                        priority = self.priority_options[index]
                        self.print_header(f"TAREAS - PRIORIDAD: {priority.upper()}")
                        tasks = self.task_manager.get_tasks(priority=priority)
                        self.display_tasks(tasks, show_details=True)
                except ValueError:
                    print("Selección no válida")
            elif choice == '6':
                break
            else:
                print("Opción no válida.")
            input("\nPresione Enter para continuar...")
    
    def edit_task_menu(self):
        self.print_header("EDITAR TAREA")
        self.display_tasks()
        task_index = input("\nIndique el número de la tarea a editar (o 'c' para cancelar): ").strip()
        if task_index.lower() == 'c':
            return
        try:
            index = int(task_index)
            if not (0 <= index < len(self.task_manager.tasks)):
                print("\nÍndice de tarea no válido.")
                input("\nPresione Enter para continuar...")
                return
            task = self.task_manager.tasks[index]
            self.print_header(f"EDITANDO TAREA: {task.title}")
            print(f"Deje en blanco para mantener el valor actual.\n")
            title = input(f"Título [{task.title}]: ").strip() or None
            description = input(f"Descripción [{task.description}]: ").strip()
            if description == "":
                description = ""
            else:
                description = description or None
            print("\nPrioridad actual:", task.priority)
            print("Opciones de prioridad:")
            for i, option in enumerate(self.priority_options):
                print(f"{i+1}. {option}")
            priority_choice = input(f"Seleccione nueva prioridad (1-{len(self.priority_options)}, o Enter para mantener): ").strip()
            priority = None
            if priority_choice:
                try:
                    choice = int(priority_choice)
                    if 1 <= choice <= len(self.priority_options):
                        priority = self.priority_options[choice-1]
                except ValueError:
                    pass
            category = input(f"Categoría [{task.category}]: ").strip() or None
            if self.task_manager.update_task(index, title, description, priority, category):
                print("\n¡Tarea actualizada con éxito!")
            else:
                print("\nError al actualizar la tarea.")
        except ValueError:
            print("\nPor favor, introduzca un número válido.")
        input("\nPresione Enter para continuar...")
    
    def delete_task_menu(self):
        self.print_header("ELIMINAR TAREA")
        self.display_tasks()
        task_index = input("\nIndique el número de la tarea a eliminar (o 'c' para cancelar): ").strip()
        if task_index.lower() == 'c':
            return
        try:
            index = int(task_index)
            if 0 <= index < len(self.task_manager.tasks):
                confirmation = input(f"¿Está seguro de eliminar la tarea '{self.task_manager.tasks[index].title}'? (s/n): ").strip().lower()
                if confirmation == 's':
                    if self.task_manager.remove_task(index):
                        print("\n¡Tarea eliminada con éxito!")
                    else:
                        print("\nError al eliminar la tarea.")
                else:
                    print("\nOperación cancelada.")
            else:
                print("\nÍndice de tarea no válido.")
        except ValueError:
            print("\nPor favor, introduzca un número válido.")
        input("\nPresione Enter para continuar...")
    
    def run(self):
        while True:
            self.print_header("GESTOR DE TAREAS")
            print("1. Ver tareas")
            print("2. Añadir tarea")
            print("3. Completar tarea")
            print("4. Editar tarea")
            print("5. Eliminar tarea")
            print("0. Salir")
            choice = input("\nElija una opción: ").strip()
            if choice == '1':
                self.view_tasks_menu()
            elif choice == '2':
                self.add_task_menu()
            elif choice == '3':
                self.complete_task_menu()
            elif choice == '4':
                self.edit_task_menu()
            elif choice == '5':
                self.delete_task_menu()
            elif choice == '0':
                print("\n¡Gracias por usar el Gestor de Tareas!")
                break
            else:
                print("\nOpción no válida. Presione Enter para continuar...")
                input()