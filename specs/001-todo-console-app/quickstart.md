# Quickstart: Todo Console App

## Prerequisites

- Python 3.13 or higher
- uv package manager

## Installation

The project uses uv for dependency management. No external dependencies are required beyond Python's standard library.

## Running the App

```bash
uv run python -m src.main
```

## Running Tests

```bash
uv run pytest
```

## Project Structure

```
src/
├── main.py           # Application entry point
├── models/
│   └── task.py       # Task dataclass definition
└── services/
    └── task_manager.py  # Task CRUD operations

tests/
└── unit/
    ├── test_task.py
    └── test_task_manager.py
```

## Usage Flow

1. Run the application
2. Select an option from the main menu (1-6)
3. Follow the prompts for your selected operation
4. Return to the main menu or exit

## First-Time Setup

No additional setup required. The application creates tasks in-memory and they persist until you exit.
