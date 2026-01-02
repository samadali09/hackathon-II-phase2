"""TaskManager service for the Todo Console App.

This module provides the TaskManager class that encapsulates all business logic
for task CRUD operations using in-memory storage.
"""

from typing import Optional

from src.models.task import Task, TaskStatus


class TaskManager:
    """Manages task operations with in-memory storage.

    Attributes:
        tasks: List of Task instances stored in memory.
        next_id: Counter for auto-incrementing task IDs.
    """

    def __init__(self) -> None:
        """Initialize the TaskManager with empty task list and ID counter."""
        self.tasks: list[Task] = []
        self.next_id: int = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """Create a new task with auto-generated ID.

        Args:
            title: Brief description of the task (required).
            description: Detailed notes about the task (optional).

        Returns:
            The newly created Task instance.
        """
        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            status="Pending",
        )
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self) -> list[Task]:
        """Return all tasks in insertion order.

        Returns:
            List of all Task instances.
        """
        return self.tasks.copy()

    def get_task(self, task_id: int) -> Optional[Task]:
        """Find a task by its ID.

        Args:
            task_id: The unique identifier of the task to find.

        Returns:
            The Task instance if found, None otherwise.
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def update_task(
        self, task_id: int, title: str | None = None, description: str | None = None
    ) -> bool:
        """Update task title and/or description.

        If title or description is None or empty string, the original value is preserved.

        Args:
            task_id: The unique identifier of the task to update.
            title: New title for the task (if provided and non-empty).
            description: New description for the task (if provided).

        Returns:
            True if task was found and updated, False otherwise.
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        new_title = task.title
        new_description = task.description

        if title is not None and title.strip():
            new_title = title

        if description is not None:
            new_description = description

        updated_task = Task(
            id=task.id,
            title=new_title,
            description=new_description,
            status=task.status,
        )

        # Remove old task and add updated one
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.tasks.append(updated_task)
        return True

    def delete_task(self, task_id: int) -> bool:
        """Remove a task by its ID.

        Args:
            task_id: The unique identifier of the task to delete.

        Returns:
            True if task was found and deleted, False otherwise.
        """
        original_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        return len(self.tasks) < original_count

    def mark_complete(self, task_id: int) -> bool:
        """Mark a task as completed.

        Args:
            task_id: The unique identifier of the task to complete.

        Returns:
            True if task was found and updated, False otherwise.
        """
        task = self.get_task(task_id)
        if task is None:
            return False

        completed_task = Task(
            id=task.id,
            title=task.title,
            description=task.description,
            status="Completed",
        )

        # Remove old task and add completed one
        self.tasks = [t for t in self.tasks if t.id != task_id]
        self.tasks.append(completed_task)
        return True

    def count_tasks(self) -> int:
        """Return the total number of tasks.

        Returns:
            Number of tasks in the manager.
        """
        return len(self.tasks)
