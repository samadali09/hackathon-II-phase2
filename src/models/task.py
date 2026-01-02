"""Task model for the Todo Console App.

This module defines the Task dataclass representing a single todo item.
"""


from dataclasses import dataclass
from typing import Literal


TaskStatus = Literal["Pending", "Completed"]


@dataclass(frozen=True)
class Task:
    """Represents a single todo task.

    Attributes:
        id: Unique identifier for the task (auto-assigned by TaskManager).
        title: Brief description of the task (required, non-empty).
        description: Detailed notes about the task (optional, can be empty).
        status: Current state of the task (either "Pending" or "Completed").
    """

    id: int
    title: str
    description: str
    status: TaskStatus

    def __post_init__(self) -> None:
        """Validate task attributes after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty")

        if self.title and len(self.title) > 200:
            raise ValueError("Task title cannot exceed 200 characters")

        if self.description and len(self.description) > 1000:
            raise ValueError("Task description cannot exceed 1000 characters")

        if self.status not in ("Pending", "Completed"):
            raise ValueError(f"Invalid status: {self.status}. Must be 'Pending' or 'Completed'")

    def to_display(self) -> str:
        """Return display string with status indicator.

        Returns:
            String in format "[X] ID - Title" for completed or "[ ] ID - Title" for pending.
        """
        indicator = "X" if self.status == "Completed" else " "
        return f"[{indicator}] {self.id} - {self.title}"
