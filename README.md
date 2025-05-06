# Gestor de Tareas en Consola 📝

Un sistema para administrar tareas desde la terminal, con prioridades, categorías y persistencia en JSON.

## Características ✨
- ✅ Crear, editar, eliminar y marcar tareas como completadas
- 🔍 Filtrar por: categorías, prioridad (alta/normal/baja) y estado (completadas/pendientes)
- 💾 Guardado automático en archivo JSON (`tasks.json`)
- 🕒 Registro de fechas de creación y finalización

## Requisitos Previos ⚙️
- Python 3.6 o superior
- No se requieren librerías externas

## Estructura del Proyecto 📂
```bash
├── task.py          # Modelo de datos (Clase Task)
├── task_manager.py  # Lógica de almacenamiento (Clase TaskManager)
├── console_ui.py    # Interfaz de usuario (Clase ConsoleUI)
└── main.py          # Punto de entrada principal
```

## Ejemplo de Uso 🖥️
```bash
Menú principal
1. Ver tareas
2. Añadir tarea
3. Completar tarea
4. Editar tarea
5. Eliminar tarea
0. Salir

# Añadir tarea
Título: Revisar documentación
Descripción: Revisar cambios en la API
Prioridad: 2 (normal)
Categoría: Trabajo

# Ver tareas
1. [ ] • Revisar documentación (Trabajo)

```
## Instalación 📥
1. Clona el repositorio o descarga los archivos:
   ```bash
   git clone https://github.com/tu-usuario/gestor-tareas.git
   cd gestor-tareas  
