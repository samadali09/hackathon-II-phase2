# CLI Command Contracts

## Main Menu Interaction

### Input Format

```
Main Menu
1. Add Task
2. View Tasks
3. Update Task
4. Delete Task
5. Mark Complete
6. Exit

Enter your choice (1-6):
```

### Output Format

Clear print statements with no specific structured format required per constitution (human-readable only).

## Command Contracts

### 1. Add Task

**Input Prompts**:
```
Enter task title: <string>
Enter task description (optional): <string>
```

**Success Output**:
```
Task created successfully! ID: <id>
```

**Error Outputs**:
- Empty title: "Error: Title cannot be empty. Please enter a title."

---

### 2. View Tasks

**Input**: None (no parameters)

**Success Output (with tasks)**:
```
Your Tasks:
[ ] 1 - Buy groceries
[X] 2 - Complete report
```

**Success Output (empty)**:
```
No tasks found.
```

---

### 3. Update Task

**Input Prompts**:
```
Enter task ID to update: <number>
Enter new title (press Enter to keep current): <string>
Enter new description (press Enter to keep current): <string>
```

**Success Output**:
```
Task updated successfully!
```

**Error Outputs**:
- Invalid ID: "Error: Task with ID <id> not found."

---

### 4. Delete Task

**Input Prompt**:
```
Enter task ID to delete: <number>
```

**Success Output**:
```
Task deleted successfully!
```

**Error Outputs**:
- Invalid ID: "Error: Task with ID <id> not found."

---

### 5. Mark Complete

**Input Prompt**:
```
Enter task ID to mark as complete: <number>
```

**Success Output**:
```
Task marked as complete!
```

**Error Outputs**:
- Invalid ID: "Error: Task with ID <id> not found."

---

### 6. Exit

**Output**:
```
Goodbye!
```

**Behavior**: Application terminates with exit code 0.

## Common Error Messages

| Scenario | Error Message |
|----------|---------------|
| Non-numeric menu input | "Invalid choice. Please enter a number between 1 and 6." |
| Numeric but out of range | "Invalid choice. Please enter a number between 1 and 6." |
| Non-numeric task ID | "Error: Please enter a valid task ID (a number)." |
| Negative/zero task ID | "Error: Task ID must be a positive number." |
| Task ID not found | "Error: Task with ID <id> not found." |
