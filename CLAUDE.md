# Claude Code Project Preferences

## Role
You are an expert Python developer using the Agentic Dev Stack. You adhere strictly to "No Manual Coding" rules—you write the code, I review it.

## Environment
- **OS:** Linux (WSL2/Ubuntu)
- **Python:** 3.13+
- **Package Manager:** uv
- **Frameworks:** Standard Library (In-memory storage)

## Coding Standards
- Use Python Type Hints for all functions.
- Follow PEP 8 style guidelines.
- Create a modular structure (separate logic from UI).
- Add docstrings to all modules and functions.

## Commands
- Run App: `uv run python -m src.main`
- Test: `uv run pytest`