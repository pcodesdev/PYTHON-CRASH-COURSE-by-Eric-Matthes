# Task Manager CLI Application

A command-line task manager built with Python that demonstrates essential list operations and data manipulation techniques.

## 📋 Features

- ✅ **Add Tasks** - Create new tasks with name, priority (1-5), and due date
- 👀 **View Tasks** - Display all tasks in a formatted table with status indicators
- ✓ **Mark Complete** - Update task completion status
- 🗑️ **Remove Tasks** - Delete tasks by position or name
- 🔄 **Sort Tasks** - Organize tasks by priority, date, or name
- 🔍 **Search Tasks** - Find tasks by keyword search
- 📊 **View Options** - Display tasks in reverse order or filtered views

## 🎯 Python List Concepts Demonstrated

This project showcases the following Python list operations:

| Operation | Method/Function | Where Used |
|-----------|----------------|------------|
| Adding items | `append()` | Adding new tasks |
| Removing by position | `del`, `pop()` | Removing tasks by index |
| Removing by value | `remove()` | Removing tasks by name |
| Sorting (permanent) | `sort()` | Sorting tasks by priority/date/name |
| Sorting (temporary) | `sorted()` | Temporary sorted views |
| Reversing | `reverse()`, `reversed()` | Reverse order display |
| Indexing | `list[index]` | Accessing and modifying tasks |
| Length | `len()` | Counting tasks, validation |
| Iteration | `for`, `enumerate()` | Displaying and searching tasks |

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd task-manager-cli
   ```

### Running the Application

```bash
python task_manager.py
```

Or on Windows:
```bash
py task_manager.py
```

## 📖 Usage Guide

### Main Menu

When you run the application, you'll see:

```
========================================
       TASK MANAGER CLI
========================================
1. Add Task
2. View All Tasks
3. Mark Task Complete
4. Remove Task
5. Sort Tasks
6. Search Tasks
7. Exit
========================================
```

### Adding a Task

1. Select option `1`
2. Enter task name (e.g., "Buy groceries")
3. Enter priority (1-5, where 1 is highest)
4. Enter due date in YYYY-MM-DD format or press Enter for today

**Example:**
```
Enter task name: Complete Python project
Enter priority (1-5, 1=highest): 1
Enter due date (YYYY-MM-DD) or press Enter for today: 2025-12-05

✅ Task 'Complete Python project' added successfully!
   Priority: 1 | Due Date: 2025-12-05
```

### Viewing Tasks

Select option `2` to see all tasks in a formatted table:

```
#    Status   Priority   Due Date     Task Name
----------------------------------------------------------------------
0    ○ Todo   P1         2025-12-05   Complete Python project
1    ✓ Done   P2         2025-12-03   Buy groceries
2    ○ Todo   P3         2025-12-10   Read documentation

Total tasks: 3
```

### Marking Tasks Complete

1. Select option `3`
2. View the task list
3. Enter the task number to mark complete

### Removing Tasks

Select option `4` and choose:
- **Option 1**: Remove by task number (uses `pop()`)
- **Option 2**: Remove by task name (uses `remove()`)

### Sorting Tasks

Select option `5` and choose from:
1. Priority (Low to High)
2. Priority (High to Low)
3. Due Date (Earliest first)
4. Due Date (Latest first)
5. Task Name (A-Z)
6. Task Name (Z-A)
7. View in Reverse Order (temporary)

### Searching Tasks

1. Select option `6`
2. Enter a search term
3. View matching tasks with their original index numbers

## 🎓 Learning Objectives

This project helps you understand:

- ✅ **List CRUD Operations** - Create, Read, Update, Delete
- ✅ **Data Structures** - Using dictionaries within lists
- ✅ **User Input Handling** - Validation and error handling
- ✅ **Control Flow** - Loops, conditionals, and menu systems
- ✅ **Function Design** - Modular, reusable code
- ✅ **Error Prevention** - Index validation, empty list checks

## 🔧 Code Structure

```
task_manager.py
├── Global Variables
│   └── tasks (list of dictionaries)
├── Functions
│   ├── display_menu()
│   ├── add_task()
│   ├── view_tasks()
│   ├── mark_complete()
│   ├── remove_task()
│   ├── sort_tasks()
│   ├── search_tasks()
│   └── main()
└── Entry Point
    └── if __name__ == "__main__"
```

## 💡 Enhancement Ideas

Want to extend this project? Try adding:

- 📁 **Data Persistence** - Save tasks to JSON file
- 🏷️ **Categories/Tags** - Organize tasks by category
- ⏰ **Due Date Alerts** - Highlight overdue tasks
- ✏️ **Edit Tasks** - Modify existing task details
- 📊 **Statistics** - Show completion rates and analytics
- 🎨 **Color Coding** - Use `colorama` for colored output
- 🆔 **Unique IDs** - Assign permanent IDs to tasks

## 📝 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to fork this project and add your own enhancements!

## 📧 Contact

Created as a portfolio project demonstrating Python list operations.

---

**Happy Task Managing! 🎯**
