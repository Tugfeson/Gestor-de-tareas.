#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

class Task:
    """
    Clase que representa una tarea individual.
    
    Esta clase encapsula toda la información relacionada con una tarea,
    incluyendo su estado, metadatos y métodos para manipularla.
    """
    
    def __init__(self, title, description="", priority="normal", category="general", completed=False):
        self.title = title
        self.description = description
        self.priority = priority
        self.category = category
        self.completed = completed
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.completed_at = None
    
    def complete(self):
        self.completed = True
        self.completed_at = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "category": self.category,
            "completed": self.completed,
            "created_at": self.created_at,
            "completed_at": self.completed_at
        }
    
    @classmethod
    def from_dict(cls, data):
        task = cls(
            title=data["title"],
            description=data["description"],
            priority=data["priority"],
            category=data["category"],
            completed=data["completed"]
        )
        task.created_at = data["created_at"]
        task.completed_at = data["completed_at"]
        return task