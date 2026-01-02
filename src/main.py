"""Main entry point for the Todo Console App.

This module provides the CLI interface for managing todo tasks.
Uses the `rich` library for enhanced UI/UX.
"""

import time

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

from src.cli.menu import (
    display_add_task_prompts,
    display_delete_task_prompt,
    display_main_menu,
    display_mark_complete_prompt,
    display_task_id_prompt,
    display_update_task_prompts,
    display_view_tasks_prompt,
)
from src.cli.validation import validate_menu_choice, validate_task_id
from src.services.task_manager import TaskManager

# Initialize rich console with custom theme
console = Console(
    theme=Theme(
        {
            "success": "bold green",
            "error": "bold red",
            "warning": "yellow",
            "info": "cyan",
        }
    )
)


def show_success_message(message: str) -> None:
    """Display a success message in a styled panel."""
    panel = Panel(
        Text(message, style="bold green"),
        box=box.HEAVY,
        style="green",
        expand=False,
    )
    console.print(panel)


def show_error_message(message: str) -> None:
    """Display an error message in red text."""
    console.print(f"[bold red]{message}[/bold red]")


def create_task_table(tasks: list) -> Table:
    """Create a rich table for displaying tasks.

    Args:
        tasks: List of Task objects to display.

    Returns:
        A configured Table object.
    """
    table = Table(
        show_header=True,
        header_style="bold cyan",
        box=box.ROUNDED,
        show_lines=True,
        title="[bold]Your Tasks[/bold]",
        title_justify="left",
    )

    # Define columns
    table.add_column("ID", width=6, justify="center", style="bold")
    table.add_column("Title", width=30, style="white")
    table.add_column("Status", width=12, justify="center")
    table.add_column("Description", width=40, style="dim")

    # Add rows with color logic
    for task in tasks:
        # Color logic: Green for Completed, Yellow for Pending
        if task.status == "Completed":
            status_style = "[bold green]Completed[/bold green]"
        else:
            status_style = "[bold yellow]Pending[/bold yellow]"

        table.add_row(
            str(task.id),
            task.title,
            status_style,
            task.description if task.description else "-",
        )

    return table


def handle_add_task(manager: TaskManager) -> None:
    """Handle adding a new task with loading spinner."""
    title, description = display_add_task_prompts()

    if not title:
        show_error_message("Title cannot be empty. Please enter a title.")
        return

    # Show loading spinner
    with console.status("[bold yellow]Creating task...", spinner="dots"):
        time.sleep(1.0)  # Fake delay for UX

    task = manager.add_task(title, description)
    show_success_message(f"Task created successfully! ID: {task.id}")


def handle_view_tasks(manager: TaskManager) -> None:
    """Handle viewing all tasks in a formatted table."""
    display_view_tasks_prompt()
    tasks = manager.list_tasks()

    if not tasks:
        panel = Panel(
            Text("No tasks found.", style="bold yellow"),
            box=box.HEAVY,
            style="yellow",
            expand=False,
        )
        console.print(panel)
        return

    # Display tasks in a rich table
    table = create_task_table(tasks)
    console.print(table)


def handle_update_task(manager: TaskManager) -> None:
    """Handle updating an existing task with loading spinner."""
    task_id_str = display_task_id_prompt("Enter task ID to update: ")
    task_id = validate_task_id(task_id_str)
    if task_id is None:
        return

    if manager.get_task(task_id) is None:
        show_error_message(f"Task with ID {task_id} not found.")
        return

    new_title, new_description = display_update_task_prompts()

    # Show loading spinner
    with console.status("[bold yellow]Updating task...", spinner="dots"):
        time.sleep(1.0)  # Fake delay for UX

    success = manager.update_task(task_id, new_title, new_description)
    if success:
        show_success_message("Task updated successfully!")
    else:
        show_error_message(f"Task with ID {task_id} not found.")


def handle_delete_task(manager: TaskManager) -> None:
    """Handle deleting a task with loading spinner."""
    task_id_str = display_task_id_prompt("Enter task ID to delete: ")
    task_id = validate_task_id(task_id_str)
    if task_id is None:
        return

    if manager.get_task(task_id) is None:
        show_error_message(f"Task with ID {task_id} not found.")
        return

    # Show loading spinner
    with console.status("[bold yellow]Deleting task...", spinner="dots"):
        time.sleep(1.0)  # Fake delay for UX

    success = manager.delete_task(task_id)
    if success:
        show_success_message("Task deleted successfully!")
    else:
        show_error_message(f"Task with ID {task_id} not found.")


def handle_mark_complete(manager: TaskManager) -> None:
    """Handle marking a task as complete with loading spinner."""
    task_id_str = display_task_id_prompt("Enter task ID to mark as complete: ")
    task_id = validate_task_id(task_id_str)
    if task_id is None:
        return

    task = manager.get_task(task_id)
    if task is None:
        show_error_message(f"Task with ID {task_id} not found.")
        return

    if task.status == "Completed":
        show_error_message(f"Task {task_id} is already completed.")
        return

    # Show loading spinner
    with console.status("[bold yellow]Marking task as complete...", spinner="dots"):
        time.sleep(1.0)  # Fake delay for UX

    success = manager.mark_complete(task_id)
    if success:
        show_success_message("Task marked as complete!")
    else:
        show_error_message(f"Task with ID {task_id} not found.")


def display_enhanced_menu() -> None:
    """Display the main menu in a styled panel."""
    menu_content = """
[bold cyan]1.[/bold cyan] Add Task       - Create a new todo task
[bold cyan]2.[/bold cyan] View Tasks     - View all your tasks
[bold cyan]3.[/bold cyan] Update Task    - Modify an existing task
[bold cyan]4.[/bold cyan] Delete Task    - Remove a task
[bold cyan]5.[/bold cyan] Mark Complete  - Mark a task as done
[bold cyan]6.[/bold cyan] Exit           - Quit the application

[yellow]Enter your choice (1-6):[/yellow] """

    panel = Panel(
        Text(menu_content, justify="left"),
        title="[bold cyan]Todo App Dashboard[/bold cyan]",
        subtitle="[dim]Manage your tasks efficiently[/dim]",
        box=box.HEAVY,
        style="blue",
        expand=False,
        padding=(1, 2),
    )
    console.print(panel)


def run_app() -> None:
    """Run the main application loop with enhanced UI."""
    manager = TaskManager()

    while True:
        display_enhanced_menu()
        choice_str = input()
        choice = validate_menu_choice(choice_str)

        if choice is None:
            continue

        if choice == 1:
            handle_add_task(manager)
        elif choice == 2:
            handle_view_tasks(manager)
        elif choice == 3:
            handle_update_task(manager)
        elif choice == 4:
            handle_delete_task(manager)
        elif choice == 5:
            handle_mark_complete(manager)
        elif choice == 6:
            console.print("\n[bold green]Goodbye![/bold green]")
            break


def main() -> None:
    """Entry point for the application."""
    console.clear()
    run_app()


if __name__ == "__main__":
    main()
