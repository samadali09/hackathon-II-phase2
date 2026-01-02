"""Menu display and input handling for the CLI.

This module handles the main menu display and user input processing.
"""


def display_main_menu() -> None:
    """Display the main menu options."""
    print("\n===== Todo App =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Complete")
    print("6. Exit")
    print("====================")
    print("Enter your choice (1-6): ", end="")


def display_add_task_prompts() -> tuple[str, str]:
    """Display prompts for adding a new task.

    Returns:
        Tuple of (title, description) from user input.
    """
    title = input("Enter task title: ").strip()
    description = input("Enter task description (optional): ").strip()
    return title, description


def display_view_tasks_prompt() -> None:
    """Display header before showing tasks list."""
    print("\nYour Tasks:")


def display_empty_tasks_message() -> None:
    """Display message when no tasks exist."""
    print("No tasks found.")


def display_update_task_prompts() -> tuple[str, str]:
    """Display prompts for updating a task.

    Returns:
        Tuple of (new_title, new_description) from user input.
    """
    new_title = input("Enter new title (press Enter to keep current): ").strip()
    new_description = input("Enter new description (press Enter to keep current): ").strip()
    return new_title, new_description


def display_delete_task_prompt() -> None:
    """Display prompt for deleting a task."""
    print("Enter task ID to delete: ", end="")


def display_mark_complete_prompt() -> None:
    """Display prompt for marking a task complete."""
    print("Enter task ID to mark as complete: ", end="")


def display_task_id_prompt(prompt: str) -> str:
    """Display a custom prompt and return user input.

    Args:
        prompt: The prompt message to display.

    Returns:
        The user's input string.
    """
    print(prompt, end="")
    return input()
