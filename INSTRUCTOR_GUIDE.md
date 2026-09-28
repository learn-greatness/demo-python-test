# Instructor Guide

Use this **before** the main assessment. Ideally demonstrate the debugging workflow on a tiny example, then let her work independently.

## Suggested live demonstration

Use:
```python
def total(numbers):
    result = 0
    for number in numbers:
        result = number
    return result
```

Run `total([1, 2, 3])`. Walk through the state: `0 -> 1 -> 2 -> 3`. Explain that the code does exactly what it says, but not what we intended. Then fix it together.

Teach this loop:
```text
Requirement -> Run code/tests -> Observe failure -> Form hypothesis -> Inspect code -> Smallest fix -> Run again -> Edge case -> Regression test
```

The key lesson: **get evidence before guessing.**

## What to tell her
> Your job isn't to make the code look nicer. Understand what is broken, make it behave according to the requirements, and prove it with tests.

Do not tell her which files contain bugs.

## Observe
Good signs: runs tests first; reads failures; makes small changes; reruns tests; uses debugger/prints when confused; checks edge cases; can explain fixes.

Warning signs: rewrites everything; changes tests to pass; adds random conditions; cannot explain fixes; never runs code; ignores errors; copies solutions without understanding.

## If she gets stuck
Level 1: “What does the failing test expect?”
Level 2: “What does the current code actually return?”
Level 3: “Can you run the function with the same input?”
Level 4: “What is the smallest change that makes behavior match the requirement?”

## Time
45–75 minutes. This is deliberately much easier than the main assessment.

## What it measures
Basic Python syntax, functions, loops, conditionals, lists/dicts, a simple class, debugging, testing, and modifying existing code. It intentionally avoids DSA, Big-O, advanced OOP, async, databases, and frameworks.
