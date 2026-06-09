## 🎯 Key Features

* **Interactive Menu System:** A straightforward, loop-driven prompt system that guides user interaction smoothly.
* **Dynamic Task Enumeration:** Automatically numbers and lists tasks chronologically as they are added.
* **Defensive Input Validation:** Guards against empty string submissions and rejects invalid menu selections to prevent application crashes.
* **Zero Dependencies:** Uses strictly standard Python library structures, requiring no third-party package installations.

---
### Application Execution Flow

```text
--- Welcome to Your Python To-Do List ---

Options:
1. View Tasks
2. Add a Task
3. Exit
Enter your choice (1-3): 2

Enter the task you want to add: Complete documentation
'Complete documentation' has been added to your list.
```

---

## 🛠️ Code Architecture Overview

The codebase is built as a single, lightweight module designed around core clean-coding principles:
* **`main()` Function Isolation:** Keeps variables local and avoids contaminating the global namespace.
* **Deterministic `while True` Loop:** Manages application state and execution lifespan reliably until a user-initiated break occurs.
* **Dynamic Arrays:** Leverages standard Python list structures for continuous in-memory tracking of task strings.

---
