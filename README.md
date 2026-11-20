# Shopping List Web App 🛒

An academic project created for the **Algorithms and Programming** course in my Systems Analysis and Development degree.

## About the project

This web application is designed to practice programming logic while organizing shopping lists. The web infrastructure was provided by the instructor, while the student team worked on the application logic.

## Technologies

- Python
- Flask
- HTML
- SQLite

## Features implemented in the code

- Registration and login pages
- Creating shopping lists
- Adding items with a name, barcode, price, and quantity
- Viewing list items
- Looking up items by barcode

## How to run

1. Install **Python 3**.
2. Download or clone this repository.
3. Install Flask:

   ```bash
   python -m pip install flask
   ```

4. Start the application:

   ```bash
   python server.py
   ```

5. Visit `http://127.0.0.1:5000` in your browser.

On some systems, use `python3` instead of `python`.

## Project structure

- `main.py`: application logic
- `server.py`: Flask routes
- `shoppinglib/`: users, items, lists, and database modules
- `templates/`: HTML pages
- `static/`: static assets
- `main_not_send.py`: earlier terminal-based exercise preserved for study

## Skills practiced

Conditions, loops, functions, modules, input validation, data structures, web routes, and database persistence.

## Limitations

**Educational use only.** Authentication, session handling, error handling, credential storage, and development server settings need improvement before this could be used in production. Do not reuse real passwords when testing.

A SQLite database file is currently tracked in this repository. Its contents should be reviewed before using this project with real data.
