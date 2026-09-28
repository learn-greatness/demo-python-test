# Python Engineering Bug Basics

This is a guided first coding test. The goal is to practice the engineering process: run tests, observe failures, understand code, make the smallest sensible fix, rerun tests, and add edge-case tests.

## Rules
- Python 3.11+
- Standard library only
- Do not rewrite the project from scratch
- Keep changes focused
- You may use Python documentation
- For this exercise, do not use AI/code-generation tools
- You may use print statements, a debugger, and tests

## Run
```bash
python -m unittest discover -s tests -v
```

There are 8 public tests. Fix the code so they pass, then add at least 3 tests of your own.

## Part 1 — Fix the greeting
`src/greetings.py`

`greet(name)` should:
- return `"Hello, <name>!"`
- remove leading/trailing whitespace
- reject an empty name with `ValueError`

## Part 2 — Fix the temperature converter
`src/temperature.py`

`celsius_to_fahrenheit(celsius)` should use:
`F = C × 9/5 + 32`

It must work for 0 and negative values and must not round internally.

## Part 3 — Fix the shopping cart total
`src/cart.py`

`calculate_total(cart)` should sum `price * quantity` for every item. An empty cart returns 0.

## Part 4 — Find the user
`src/users.py`

Implement/fix `find_user_by_id(users, user_id)` so it returns the matching dictionary, or `None` if absent. Do not modify the list.

## Part 5 — Fix the counter
`src/counter.py`

`Counter` starts at 0. `increment()` adds 1, `decrement()` subtracts 1, and `reset()` sets it to 0.

## Part 6 — Add a small feature
`src/tasks.py`

Implement:
```python
add_task(tasks, title)
complete_task(tasks, task_id)
```

A task is `{ "id": 1, "title": "Learn Python", "completed": False }`.

`add_task` adds and returns a new task with a unique ID and incomplete status.
`complete_task` finds by ID, marks completed, returns it, and raises `ValueError` if missing.

## Part 7 — Your own tests
Add at least 3 tests. Include edge cases such as empty input, negative numbers, missing users, repeated operations, whitespace, or invalid IDs.

## Reflection
Create `REFLECTION.md` and briefly answer:
1. Which bug was easiest?
2. Which took the most investigation?
3. What did the failure/error tell you?
4. Did you use print statements or a debugger?
5. What edge case did you add?
6. What did you learn about modifying existing code?
