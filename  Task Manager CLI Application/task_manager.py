"""
Task Manager CLI Application
A command-line task manager that demonstrates Python list operations
"""

from datetime import datetime

# Global task list - stores all tasks as dictionaries
tasks = []


def display_menu():
    """Display the main menu options"""
    print("\n" + "=" * 40)
    print("       TASK MANAGER CLI")
    print("=" * 40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete")
    print("4. Remove Task")
    print("5. Sort Tasks")
    print("6. Search Tasks")
    print("7. Exit")
    print("=" * 40)


def add_task():
    """Add a new task to the task list using append()"""
    print("\n" + "-" * 40)
    print("         ADD NEW TASK")
    print("-" * 40)

    # Get task name
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("❌ Task name cannot be empty!")
        return

    # Get priority (1-5, where 1 is highest)
    while True:
        try:
            priority = int(input("Enter priority (1-5, 1=highest): ").strip())
            if 1 <= priority <= 5:
                break
            else:
                print("❌ Priority must be between 1 and 5!")
        except ValueError:
            print("❌ Please enter a valid number!")

    # Get due date (optional, defaults to today)
    date_input = input("Enter due date (YYYY-MM-DD) or press Enter for today: ").strip()
    if date_input:
        try:
            # Validate date format
            datetime.strptime(date_input, "%Y-%m-%d")
            due_date = date_input
        except ValueError:
            print("❌ Invalid date format! Using today's date.")
            due_date = datetime.now().strftime("%Y-%m-%d")
    else:
        due_date = datetime.now().strftime("%Y-%m-%d")

    # Create task dictionary
    new_task = {
        'name': task_name,
        'complete': False,
        'priority': priority,
        'date': due_date
    }

    # Add task to list using append()
    tasks.append(new_task)

    print(f"\n✅ Task '{task_name}' added successfully!")
    print(f"   Priority: {priority} | Due Date: {due_date}")


def view_tasks():
    """Display all tasks in a formatted table"""
    print("\n" + "-" * 40)
    print("         ALL TASKS")
    print("-" * 40)

    # Check if list is empty (avoid index errors)
    if len(tasks) == 0:
        print("📭 No tasks found! Add a task to get started.")
        return

    # Display header
    print(f"\n{'#':<4} {'Status':<8} {'Priority':<10} {'Due Date':<12} {'Task Name'}")
    print("-" * 70)

    # Loop through tasks with enumerate to get index numbers
    for index, task in enumerate(tasks):
        # Format status with symbols
        status = "✓ Done" if task['complete'] else "○ Todo"

        # Format priority
        priority_str = f"P{task['priority']}"

        # Display task
        print(f"{index:<4} {status:<8} {priority_str:<10} {task['date']:<12} {task['name']}")

    print(f"\nTotal tasks: {len(tasks)}")


def mark_complete():
    """Mark a task as complete by updating its status"""
    print("\n" + "-" * 40)
    print("      MARK TASK COMPLETE")
    print("-" * 40)

    # Check if list is empty
    if len(tasks) == 0:
        print("📭 No tasks found! Add a task first.")
        return

    # Display all tasks with index numbers
    view_tasks()

    # Get task index from user
    try:
        index = int(input("\nEnter task number to mark complete: ").strip())

        # Validate index is within range (avoid index errors!)
        if index < 0 or index >= len(tasks):
            print(f"❌ Invalid task number! Please enter a number between 0 and {len(tasks) - 1}.")
            return

        # Access task using list indexing
        task = tasks[index]

        # Check if already complete
        if task['complete']:
            print(f"ℹ️  Task '{task['name']}' is already marked as complete!")
        else:
            # Update the complete status
            tasks[index]['complete'] = True
            print(f"✅ Task '{task['name']}' marked as complete!")

    except ValueError:
        print("❌ Please enter a valid number!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")


def remove_task():
    """Remove a task using del, pop(), or remove()"""
    print("\n" + "-" * 40)
    print("        REMOVE TASK")
    print("-" * 40)

    # Check if list is empty
    if len(tasks) == 0:
        print("📭 No tasks found! Add a task first.")
        return

    # Display removal options
    print("\nRemove by:")
    print("1. Task Number (using del or pop)")
    print("2. Task Name (using remove)")
    print("3. Cancel")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == '1':
        # Remove by position using del or pop()
        view_tasks()

        try:
            index = int(input("\nEnter task number to remove: ").strip())

            # Validate index
            if index < 0 or index >= len(tasks):
                print(f"❌ Invalid task number! Please enter a number between 0 and {len(tasks) - 1}.")
                return

            # Ask for confirmation
            task_name = tasks[index]['name']
            confirm = input(f"\n⚠️  Are you sure you want to delete '{task_name}'? (yes/no): ").strip().lower()

            if confirm == 'yes' or confirm == 'y':
                # Use pop() to remove and get the removed task
                removed_task = tasks.pop(index)
                print(f"🗑️  Task '{removed_task['name']}' removed successfully using pop()!")

                # Alternative: could use del tasks[index]
                # del tasks[index]
                # print(f"🗑️  Task removed successfully using del!")
            else:
                print("❌ Removal cancelled.")

        except ValueError:
            print("❌ Please enter a valid number!")
        except Exception as e:
            print(f"❌ An error occurred: {e}")

    elif choice == '2':
        # Remove by name using remove()
        view_tasks()

        task_name = input("\nEnter task name to remove: ").strip()

        # Search for task by name
        found = False
        for task in tasks:
            if task['name'].lower() == task_name.lower():
                # Ask for confirmation
                confirm = input(f"\n⚠️  Are you sure you want to delete '{task['name']}'? (yes/no): ").strip().lower()

                if confirm == 'yes' or confirm == 'y':
                    # Use remove() to delete by value
                    tasks.remove(task)
                    print(f"🗑️  Task '{task['name']}' removed successfully using remove()!")
                else:
                    print("❌ Removal cancelled.")

                found = True
                break

        if not found:
            print(f"❌ Task '{task_name}' not found!")

    elif choice == '3':
        print("❌ Removal cancelled.")
    else:
        print("❌ Invalid choice!")


def sort_tasks():
    """Sort tasks using sort() and sorted() methods"""
    print("\n" + "-" * 40)
    print("         SORT TASKS")
    print("-" * 40)

    # Check if list is empty
    if len(tasks) == 0:
        print("📭 No tasks found! Add a task first.")
        return

    # Display sort options
    print("\nSort by:")
    print("1. Priority (Low to High)")
    print("2. Priority (High to Low)")
    print("3. Due Date (Earliest first)")
    print("4. Due Date (Latest first)")
    print("5. Task Name (A-Z)")
    print("6. Task Name (Z-A)")
    print("7. View in Reverse Order")
    print("8. Cancel")

    choice = input("\nEnter choice (1-8): ").strip()

    if choice == '1':
        # Sort by priority (ascending) - permanent change using sort()
        tasks.sort(key=lambda x: x['priority'])
        print("\n✅ Tasks sorted by priority (Low to High)")
        view_tasks()

    elif choice == '2':
        # Sort by priority (descending) - permanent change
        tasks.sort(key=lambda x: x['priority'], reverse=True)
        print("\n✅ Tasks sorted by priority (High to Low)")
        view_tasks()

    elif choice == '3':
        # Sort by date (ascending)
        tasks.sort(key=lambda x: x['date'])
        print("\n✅ Tasks sorted by due date (Earliest first)")
        view_tasks()

    elif choice == '4':
        # Sort by date (descending)
        tasks.sort(key=lambda x: x['date'], reverse=True)
        print("\n✅ Tasks sorted by due date (Latest first)")
        view_tasks()

    elif choice == '5':
        # Sort by name (A-Z)
        tasks.sort(key=lambda x: x['name'].lower())
        print("\n✅ Tasks sorted by name (A-Z)")
        view_tasks()

    elif choice == '6':
        # Sort by name (Z-A)
        tasks.sort(key=lambda x: x['name'].lower(), reverse=True)
        print("\n✅ Tasks sorted by name (Z-A)")
        view_tasks()

    elif choice == '7':
        # Temporary reverse view using sorted() and reversed()
        print("\n✅ Tasks in reverse order (temporary view):")

        # Create a reversed copy without modifying original
        reversed_tasks = list(reversed(tasks))

        # Display reversed tasks
        print(f"\n{'#':<4} {'Status':<8} {'Priority':<10} {'Due Date':<12} {'Task Name'}")
        print("-" * 70)

        for index, task in enumerate(reversed_tasks):
            status = "✓ Done" if task['complete'] else "○ Todo"
            priority_str = f"P{task['priority']}"
            print(f"{index:<4} {status:<8} {priority_str:<10} {task['date']:<12} {task['name']}")

        print("\nNote: Original order unchanged. Use options 1-6 for permanent sorting.")

    elif choice == '8':
        print("❌ Sorting cancelled.")
    else:
        print("❌ Invalid choice!")


def search_tasks():
    """Search for tasks by name using list searching"""
    print("\n" + "-" * 40)
    print("        SEARCH TASKS")
    print("-" * 40)

    # Check if list is empty
    if len(tasks) == 0:
        print("📭 No tasks found! Add a task first.")
        return

    search_term = input("\nEnter search term: ").strip().lower()

    if not search_term:
        print("❌ Search term cannot be empty!")
        return

    # Search through tasks and collect matches
    matches = []
    match_indices = []

    for index, task in enumerate(tasks):
        # Case-insensitive search in task name
        if search_term in task['name'].lower():
            matches.append(task)
            match_indices.append(index)

    # Display results
    if len(matches) == 0:
        print(f"\n❌ No tasks found matching '{search_term}'")
    else:
        print(f"\n✅ Found {len(matches)} task(s) matching '{search_term}':")
        print(f"\n{'#':<4} {'Status':<8} {'Priority':<10} {'Due Date':<12} {'Task Name'}")
        print("-" * 70)

        for i, task in enumerate(matches):
            status = "✓ Done" if task['complete'] else "○ Todo"
            priority_str = f"P{task['priority']}"
            original_index = match_indices[i]
            print(f"{original_index:<4} {status:<8} {priority_str:<10} {task['date']:<12} {task['name']}")


def main():
    """Main program loop"""
    print("\n🎯 Welcome to Task Manager CLI!")

    while True:
        display_menu()

        try:
            choice = input("\nEnter your choice (1-7): ").strip()

            if choice == '1':
                add_task()
            elif choice == '2':
                view_tasks()
            elif choice == '3':
                mark_complete()
            elif choice == '4':
                remove_task()
            elif choice == '5':
                sort_tasks()
            elif choice == '6':
                search_tasks()
            elif choice == '7':
                print("\n👋 Thank you for using Task Manager! Goodbye!")
                break
            else:
                print("\n❌ Invalid choice! Please enter a number between 1-7.")

        except KeyboardInterrupt:
            print("\n\n👋 Program interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")


if __name__ == "__main__":
    main()
