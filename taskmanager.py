#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
from task import Task

class TaskManager:
    """
    Gestiona la colección de tareas y la persistencia de datos.
    """
    
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()
    
    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        return len(self.tasks) - 1
    
    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_tasks()
            return True
        return False
    
    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].complete()
            self.save_tasks()
            return True
        return False
    
    def get_tasks(self, filter_completed=None, category=None, priority=None):
        filtered_tasks = self.tasks
        if filter_completed is not None:
            filtered_tasks = [t for t in filtered_tasks if t.completed == filter_completed]
        if category:
            filtered_tasks = [t for t in filtered_tasks if t.category.lower() == category.lower()]
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority.lower() == priority.lower()]
        return filtered_tasks
    
    def update_task(self, index, title=None, description=None, priority=None, category=None):
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            if title:
                task.title = title
            if description is not None:
                task.description = description
            if priority:
                task.priority = priority
            if category:
                task.category = category
            self.save_tasks()
            return True
        return False
    
    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as file:
                    tasks_data = json.load(file)
                    self.tasks = [Task.from_dict(task_data) for task_data in tasks_data]
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Error al cargar el archivo de tareas: {e}")
                self.tasks = []
    
    def save_tasks(self):
        tasks_data = [task.to_dict() for task in self.tasks]
        with open(self.filename, 'w', encoding='utf-8') as file:
            json.dump(tasks_data, file, indent=2, ensure_ascii=False)