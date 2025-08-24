# Copilot Instructions for Code-Cluster-Python

## Project Overview
This repository is a collection of Python modules demonstrating fundamental programming concepts and data structures, suitable for learning, reference, and competitive programming.

## Structure & Key Files
- Each file focuses on a single topic (e.g., `Basics_Lists.py`, `BitwiseOperations.py`, `LinkedList.py`).
- No central application entry point; files are standalone and typically contain example functions and a `__main__` block for quick testing.
- `basic_io.py` exemplifies input/output patterns for competitive programming.

## Patterns & Conventions
- Functions are named descriptively for their purpose (e.g., `read_int`, `read_matrix`).
- Input is read using `input()` and output is printed directly; no external dependencies or frameworks.
- Example data and expected formats are documented in comments above functions.
- Minimal error handling; focus is on clarity and demonstration.
- Data structures are built using Python built-ins (lists, dicts, sets, tuples).
- For matrix/array input, values are read from standard input and processed in list comprehensions.

## Developer Workflow
- No build system or test framework is present; run files directly with `python <filename>.py`.
- To test a function, uncomment its call in the `__main__` block and execute the file.
- No external package installation required.

## Integration & Extensibility
- Files are independent; no cross-file imports or shared state.
- To add new examples, create a new file or append to an existing topic file, following the established function and comment style.

## Example: Input/Output Pattern
```python
# Read n x n matrix from input
def read_matrix():
    n = int(input())
    matrix = []
    for _ in range(n):
        row = [int(i) for i in input().split()]
        matrix.append(row)
    print(matrix)
```

## References
- See `README.md` for a high-level topic list.
- Each file's header and comments provide format and usage guidance.

---
For questions or improvements, clarify the topic and file. AI agents should preserve the educational style and avoid introducing unnecessary complexity.
