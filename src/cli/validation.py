"""Input validation helpers for the CLI.

This module provides validation functions for user inputs.
"""


from typing import Optional


def validate_task_id(value: str) -> Optional[int]:
    """Validate and parse a task ID input.

    Args:
        value: The string input from the user.

    Returns:
        The validated integer task ID, or None if invalid.
    """
    try:
        task_id = int(value)
        if task_id <= 0:
            print("Error: Task ID must be a positive number.")
            return None
        return task_id
    except ValueError:
        print("Error: Please enter a valid task ID (a number).")
        return None


def validate_menu_choice(value: str, max_choice: int = 6) -> Optional[int]:
    """Validate and parse a menu choice input.

    Args:
        value: The string input from the user.
        max_choice: The maximum valid choice number (default 6).

    Returns:
        The validated integer choice, or None if invalid.
    """
    try:
        choice = int(value)
        if choice < 1 or choice > max_choice:
            print(f"Invalid choice. Please enter a number between 1 and {max_choice}.")
            return None
        return choice
    except ValueError:
        print(f"Invalid choice. Please enter a number between 1 and {max_choice}.")
        return None
