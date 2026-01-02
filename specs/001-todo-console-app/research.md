# Research: Todo Console App

## Python CLI Best Practices

### Input Validation

**Decision**: Use Python's `try/except` with `int()` conversion for numeric input validation.

Rationale: Python's standard library provides robust exception handling. For menu selection and task ID inputs, wrapping `int()` conversion in try/except catches non-numeric input cleanly. This aligns with constitution principle III (Robust Error Handling).

Alternatives considered:
- Regular expressions - Overkill for simple numeric parsing
- `isdigit()` method - Doesn't handle negative numbers or leading zeros well
- Third-party libraries like `click` or `typer` - Constitution specifies "pure CLI" with standard library

### Task Storage Structure

**Decision**: Use a Python list of Task dataclass instances, with a counter for ID generation.

Rationale:
- List preserves insertion order for display
- Dataclass provides clean type hints and auto-generated methods
- Counter variable enables O(1) ID generation
- Simple and aligns with in-memory architecture requirement

Alternatives considered:
- Dictionary keyed by ID - Enables O(1) lookup but adds complexity
- List of dictionaries - Loses type safety and IDE support
- Named tuple - Immutable, preventing status updates

### Menu System Design

**Decision**: While-loop with input() prompts and clear print statements for output.

Rationale:
- Matches constitution requirement for "pure CLI" with print/input
- Simple to implement and understand
- No external dependencies needed
- Easy to extend with additional menu options

Alternatives considered:
- argparse/click - Adds dependencies, over-engineered for simple menu
- curses/textual - Not "pure CLI" per constitution, platform-specific

## Phase 0 Findings

All technical decisions align with constitution principles:

1. **In-Memory Architecture**: Using Python list - no external storage
2. **CLI-First Interface**: Using print/input - no external CLI libraries
3. **Robust Error Handling**: Using try/except with clear error messages
4. **Modular Architecture**: Separate models/services/cli modules

## Unknowns Resolved

- No [NEEDS CLARIFICATION] markers remained after analysis
- All implementation details determined from spec and constitution
