# Library Management System

A command-line library management tool built in Python as part of **Python Accelerator** course. The program simulates core operations of a library system — adding and removing books, tracking copies, lending, restoring, and viewing statistics — all through an interactive text-based menu.

## Why This Project

This project was developed to practice foundational Python concepts in a hands-on, real-world scenario. It covers:

- **Data modeling with dictionaries** — using a dictionary as an in-memory data store to map book titles to their available copies.
- **Input validation and error handling** — leveraging `try/except` blocks and `ValueError` to handle invalid or negative user input gracefully.
- **Modular design** — each operation (add, remove, lend, restore, search, stats) is encapsulated in its own function, keeping the codebase clean and easy to extend.
- **Control flow** — an interactive loop that continuously reads user commands until an exit keyword is entered.

## Features

| Feature | Description |
|---|---|
| **Add books** | Register a new title or increase copies of an existing one |
| **Remove books** | Delete a title from the catalogue entirely |
| **Check availability** | Verify whether at least one copy of a title is available |
| **Lend a book** | Decrease the copy count by one when a book is borrowed |
| **Restore a book** | Increase the copy count after repair or return |
| **View catalogue** | Print every title along with its current copy count |
| **Library statistics** | Display total titles, total copies, and average copies per title |

## How to Run

```bash
python Progetto_Biblioteca.py
```

Once started, the program prompts for a command. Supported commands (in Italian, matching the original spec):

- `Aggiungi libro` — add a book (then enter title and number of copies)
- `Rimuovi libro` — remove a book
- `Verifica disponibilità` — check availability
- `Prendi in prestito` — borrow a book
- `Restaurare libro` — restore copies
- `Visualizza libri` — view catalogue
- `Statistiche` — show library stats
- `Esci` — quit

## Tech Stack

- **Language:** Python 3
- **External dependencies:** None — standard library only

## What I Learned

- How to use Python dictionaries as lightweight data stores.
- Writing defensive code with `try/except` for robust input handling.
- Structuring a program into small, reusable functions.
- Building an interactive CLI loop that maps user input to actions.

## About

Built by me during a Python Accelerator course as a way to solidify core Python fundamentals through a practical, self-contained project.
