# Data Model: Todo Console App

## Task Entity

### Overview

The `Task` entity represents a single todo item managed by the application. It is the core data structure for the entire system.

### Attributes

| Attribute | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `id` | int | Yes | Auto-increment | Unique identifier for the task |
| `title` | str | Yes | N/A | Brief description of the task (non-empty) |
| `description` | str | No | "" | Detailed notes about the task (optional) |
| `status` | str | No | "Pending" | Current state of the task |

### Status Values

The `status` field is restricted to the following values:

| Status | Description |
|--------|-------------|
| `"Pending"` | Task has not been completed yet |
| `"Completed"` | Task has been finished |

### Validation Rules

1. **ID Validation**:
   - Must be a positive integer (>= 1)
   - Must exist in the task list to be valid for operations

2. **Title Validation**:
   - Must be a non-empty string after stripping whitespace
   - Maximum length: 200 characters (reasonable CLI display limit)

3. **Description Validation**:
   - Optional field
   - Can be empty string
   - Maximum length: 1000 characters (reasonable limit)

4. **Status Validation**:
   - Must be exactly "Pending" or "Completed"
   - Case-sensitive (stored as Title Case)

### Relationships

- **Storage**: Tasks are stored in an in-memory Python list
- **ID Generation**: Uses an integer counter that increments for each new task
- **No external references**: No foreign keys or references to external entities

### State Transitions

```
Created with "Pending" status
         |
         v
    [Pending] --mark_complete()--> [Completed]
         |
         v
    (can be deleted at any time)
```

## TaskManager Service

### Overview

The `TaskManager` class encapsulates all business logic for task operations.

### Data Structure

```python
tasks: list[Task]      # In-memory list of Task instances
next_id: int           # Counter for auto-incrementing IDs
```

### Methods

| Method | Parameters | Returns | Description |
|--------|------------|---------|-------------|
| `add_task(title, description)` | title: str, description: str | Task | Creates new task with auto-ID |
| `list_tasks()` | None | list[Task] | Returns all tasks |
| `get_task(task_id)` | task_id: int | Task or None | Finds task by ID |
| `update_task(task_id, title, description)` | task_id: int, title: str, description: str | bool | Updates task if exists |
| `delete_task(task_id)` | task_id: int | bool | Removes task if exists |
| `mark_complete(task_id)` | task_id: int | bool | Sets status to "Completed" |
