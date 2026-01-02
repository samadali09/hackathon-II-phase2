<!--
Sync Impact Report
==================
Version change: N/A → 1.0.0 (initial creation)

Modified principles: N/A (new constitution)

Added sections:
- Core Principles section with 4 principles:
  1. I. In-Memory Architecture
  2. II. CLI-First Interface
  3. III. Robust Error Handling
  4. IV. Modular Architecture
- Additional Constraints section
- Development Workflow section

Removed sections: N/A (initial creation)

Templates requiring updates:
- .specify/templates/plan-template.md: ✅ No changes needed (constitution check section is generic)
- .specify/templates/spec-template.md: ✅ No changes needed (user stories section is generic)
- .specify/templates/tasks-template.md: ✅ No changes needed (tasks organization is generic)

Follow-up TODOs: None
-->

# TaskFlow Constitution

## Core Principles

### I. In-Memory Architecture
All application state MUST be stored in-memory using Python dictionaries or lists.
No external database files (SQL, SQLite, or other persistence layers) are permitted
in this phase. Data persists only for the duration of the application session.

Rationale: Simplicity and rapid prototyping focus. Eliminates database setup overhead
and migration complexity.

### II. CLI-First Interface
The application MUST expose all functionality through a pure command-line interface.
All user interactions MUST use clear print statements for output and input() prompts
for user input. No GUI, web interface, or TUI libraries are required.

Rationale: Maximizes portability and minimizes dependencies. CLI is sufficient for
a task management workflow tool.

### III. Robust Error Handling
The application MUST NOT crash on invalid user input. All input validation MUST be
handled gracefully with informative error messages. Numeric inputs MUST be validated
before use, and text inputs MUST be sanitized where appropriate.

Rationale: Ensures reliable user experience. Users should receive actionable feedback
rather than stack traces or unexpected termination.

### IV. Modular Architecture
The application MUST be organized into separate modules with clear separation of concerns:
- Task model: Data structure definitions in `src/models/`
- TaskManager logic: Business logic in `src/services/`
- CLI interaction: User interface in `src/cli/`

Each module MUST be independently testable and documentable.

Rationale: Maintainability and extensibility. Clear boundaries enable independent
development, testing, and future enhancements.

## Additional Constraints

**Technology Stack:**
- Language: Python 3.13+
- Package Manager: uv
- Storage: In-memory (dict/list only)
- Testing: pytest

**Quality Standards:**
- All functions MUST use Python type hints
- All modules and functions MUST include docstrings
- Code MUST follow PEP 8 style guidelines

## Development Workflow

**Implementation Requirements:**
- All code changes MUST follow the Red-Green-Refactor cycle when tests are added
- Each feature implementation MUST have corresponding test coverage
- Code reviews MUST verify compliance with constitution principles

**Run Commands:**
- Run App: `uv run python -m src.main`
- Test: `uv run pytest`

## Governance

This constitution supersedes all other development practices. Amendments require:
1. Documentation of the proposed change
2. Review and approval from project maintainers
3. Migration plan for existing implementations (if applicable)

All development agents MUST verify compliance with these principles before
considering any implementation complete.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
