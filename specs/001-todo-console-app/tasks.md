# Tasks: Todo Console App

**Input**: Design documents from `/specs/001-todo-console-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project directory structure per plan.md (src/, src/models/, src/services/, tests/unit/)
- [x] T002 Create src/__init__.py (empty package marker)
- [x] T003 [P] Create src/models/__init__.py (empty package marker)
- [x] T004 [P] Create src/services/__init__.py (empty package marker)
- [x] T005 [P] Create tests/__init__.py (empty package marker)
- [x] T006 [P] Create tests/unit/__init__.py (empty package marker)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**CRITICAL**: No user story work can begin until this phase is complete

### Tests for Foundational (if tests requested) ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for Foundational

- [x] T007 [P] Create Task dataclass in src/models/task.py with id, title, description, status attributes
- [x] T008 [P] Add Task dataclass validation (title non-empty, status enum values)
- [x] T009 Create TaskManager class in src/services/task_manager.py with tasks list and next_id counter
- [x] T010 [P] [Foundational] Implement TaskManager.add_task() method (auto-increments ID, defaults to "Pending")
- [x] T011 [P] [Foundational] Implement TaskManager.list_tasks() method (returns all tasks)
- [x] T012 [P] [Foundational] Implement TaskManager.get_task() method (finds task by ID)
- [x] T013 [P] [Foundational] Implement TaskManager.update_task() method (updates title/description, preserves on empty)
- [x] T014 [P] [Foundational] Implement TaskManager.delete_task() method (removes task by ID)
- [x] T015 [P] [Foundational] Implement TaskManager.mark_complete() method (sets status to "Completed")

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 6 - Navigate Main Menu (Priority: P1) 🎯 MVP ENABLER

**Goal**: Users can navigate between different operations through a main menu (enables all other features)

**Independent Test**: Run the app, verify main menu displays all 6 options, test invalid input handling

### Tests for User Story 6 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 6

- [x] T016 [P] [US6] Create main menu display function in src/cli/menu.py (prints options 1-6)
- [x] T017 [P] [US6] Create menu input handler in src/cli/menu.py (validates 1-6, shows error on invalid)
- [x] T018 [P] [US6] Create main application loop in src/main.py (while True, show menu, process input)
- [x] T019 [US6] Implement exit option (prints "Goodbye!", exits with code 0)

**Checkpoint**: Main menu working - all user operations now accessible

---

## Phase 4: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Users can create new tasks by providing a title and optional description

**Independent Test**: Run app, select "Add Task", enter title and description, verify task appears in list

### Tests for User Story 1 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 1

- [x] T020 [P] [US1] Create CLI add task prompts in src/cli/add_task.py (prompt for title, description)
- [x] T021 [P] [US1] Add title validation (non-empty after strip) with error message
- [x] T022 [US1] Connect add task CLI to TaskManager.add_task() in src/main.py
- [x] T023 [US1] Add success confirmation output ("Task created successfully! ID: <id>")

**Checkpoint**: User Story 1 complete - users can create tasks

---

## Phase 5: User Story 2 - View Task List (Priority: P1) 🎯 MVP

**Goal**: Users can see all their tasks with completion status indicators

**Independent Test**: Run app, select "View Tasks", verify tasks display with [X]/[ ] status

### Tests for User Story 2 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 2

- [x] T024 [P] [US2] Create CLI view task display in src/cli/view_tasks.py (format: "[X]/[ ] ID - Title")
- [x] T025 [US2] Handle empty list case (display "No tasks found.")
- [x] T026 [US2] Connect view task CLI to TaskManager.list_tasks() in src/main.py

**Checkpoint**: User Story 2 complete - users can view tasks with status indicators

---

## Phase 6: User Story 3 - Mark Tasks Complete (Priority: P1) 🎯 MVP

**Goal**: Users can mark tasks as completed

**Independent Test**: Create task, mark complete, verify status changes to [X] in task list

### Tests for User Story 3 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 3

- [x] T027 [P] [US3] Create CLI mark complete prompts in src/cli/mark_complete.py (prompt for task ID)
- [x] T028 [P] [US3] Add task ID validation (positive integer, must exist)
- [x] T029 [US3] Connect mark complete CLI to TaskManager.mark_complete() in src/main.py
- [x] T030 [US3] Add success output ("Task marked as complete!")

**Checkpoint**: User Story 3 complete - users can complete tasks

---

## Phase 7: User Story 4 - Update Task Details (Priority: P2)

**Goal**: Users can modify the title or description of existing tasks

**Independent Test**: Create task, update title, verify changes appear in task list

### Tests for User Story 4 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 4

- [x] T031 [P] [US4] Create CLI update task prompts in src/cli/update_task.py (prompt for ID, new title, new description)
- [x] T032 [P] [US4] Add task ID validation (positive integer, must exist)
- [x] T033 [US4] Implement empty input handling (preserve original value when Enter pressed)
- [x] T034 [US4] Connect update task CLI to TaskManager.update_task() in src/main.py
- [x] T035 [US4] Add success output ("Task updated successfully!")

**Checkpoint**: User Story 4 complete - users can update task details

---

## Phase 8: User Story 5 - Delete Tasks (Priority: P2)

**Goal**: Users can remove tasks they no longer need

**Independent Test**: Create task, delete it, verify it no longer appears in task list

### Tests for User Story 5 ⚠️

> Tests are NOT explicitly requested in spec.md - skipping

### Implementation for User Story 5

- [x] T036 [P] [US5] Create CLI delete task prompts in src/cli/delete_task.py (prompt for task ID)
- [x] T037 [P] [US5] Add task ID validation (positive integer, must exist)
- [x] T038 [US5] Connect delete task CLI to TaskManager.delete_task() in src/main.py
- [x] T039 [US5] Add success output ("Task deleted successfully!")

**Checkpoint**: User Story 5 complete - users can delete tasks

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T040 [P] Add input validation helper functions in src/cli/validation.py (validate_task_id, validate_menu_choice)
- [ ] T041 [P] Create pytest configuration in pyproject.toml or pytest.ini
- [ ] T042 [P] Add unit tests for Task dataclass in tests/unit/test_task.py
- [ ] T043 [P] Add unit tests for TaskManager in tests/unit/test_task_manager.py
- [ ] T044 Verify all CLI commands work from quickstart.md validation
- [ ] T045 Final end-to-end test: Add task → View → Update → Mark Complete → Delete

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3-8)**: All depend on Foundational phase completion
  - User stories can proceed in parallel after Phase 2
  - US6 (Menu) enables other stories but doesn't block them
- **Polish (Phase 9)**: Depends on all user stories being complete

### User Story Dependencies

- **User Story 6 (Menu)**: Can start after Foundational - enables navigation to all operations
- **User Story 1 (Add)**: Can start after Foundational - independent
- **User Story 2 (View)**: Can start after Foundational - independent
- **User Story 3 (Mark Complete)**: Can start after Foundational - independent
- **User Story 4 (Update)**: Can start after Foundational - independent
- **User Story 5 (Delete)**: Can start after Foundational - independent

### Within Each User Story

- Model first (Task dataclass - Phase 2)
- Service next (TaskManager methods - Phase 2)
- CLI last (src/main.py integration - user story phases)
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel (T001-T006)
- All Foundational tasks marked [P] can run in parallel (T007-T008, T010-T015)
- All CLI module creation tasks marked [P] can run in parallel
- Once Foundational phase completes, all user stories can start in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Create CLI modules for US1 in parallel:
Task: "Create CLI add task prompts in src/cli/add_task.py"
Task: "Add title validation with error message"

# Then integrate in main:
Task: "Connect add task CLI to TaskManager.add_task() in src/main.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 + Menu Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (Task + TaskManager)
3. Complete Phase 3: User Story 6 (Main Menu)
4. Complete Phase 4: User Story 1 (Add Task)
5. **STOP and VALIDATE**: Test adding tasks independently
6. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 6 (Menu) → App has navigation
3. Add User Story 1 (Add) → Test independently → MVP!
4. Add User Story 2 (View) → Test independently
5. Add User Story 3 (Mark Complete) → Test independently
6. Add User Story 4 (Update) → Test independently
7. Add User Story 5 (Delete) → Test independently
8. Polish phase → Finalize

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together (Task T001-T015)
2. Once Foundational is done:
   - Developer A: User Story 6 (Menu) - T016-T019
   - Developer B: User Story 1 (Add) - T020-T023
   - Developer C: User Story 2 (View) - T024-T026
3. Then:
   - Developer A: User Story 3 (Mark Complete) - T027-T030
   - Developer B: User Story 4 (Update) - T031-T035
   - Developer C: User Story 5 (Delete) - T036-T039
4. Team completes Polish phase together - T040-T045

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence

**Total Tasks**: 45
**Completed Tasks**: 40 (Phase 1-4 + Phase 3-8 + Phase 9 validation)
**Remaining Tasks**: 5 (Phase 9: pytest config, unit tests, final validation)
