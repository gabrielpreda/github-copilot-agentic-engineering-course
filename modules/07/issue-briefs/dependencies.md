# Trainer Issue — dependency-aware completion

## Title

Capstone: prevent completing blocked tasks

## Body

Some tasks cannot start until other tasks are finished. Let a task name the work it depends on and stop users from completing it too early. Make sure the API does not allow impossible dependency chains.

Before implementation, inspect the current Task API and related issues, clarify dependency validation and completion behavior, and write requirements, a concise specification, and a linked task plan. Build a focused vertical slice on a feature branch. Preserve existing behavior and keep the current in-memory service; do not add a database, UI, or authentication in this exercise.

This is the advanced capstone option. It is not permission to skip clarification or expand scope beyond the trainer-approved answers.
