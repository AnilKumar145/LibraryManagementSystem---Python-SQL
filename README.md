# Library Management System

## Overview
The Library Management System is a simple application designed to help manage books in a library. It allows users to add books, issue books to borrowers, return books, and view available books. The project is built using Python and SQLite for the database.

## Features
- **Add Book**: Users can add new books to the library.
- **Issue Book**: Users can issue books to borrowers and mark them as unavailable.
- **Return Book**: Users can return books, making them available again.
- **View Available Books**: Users can view a list of all available books in the library.

## Technologies Used
- **Python**: Programming language for backend logic.
- **SQLite**: Lightweight database for storing book and issue records.


## Setup Instructions

### Prerequisites
- Python 3.x installed on your machine.
- Git installed on your machine.
- A Heroku account (optional for deployment).

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/LibraryManagementSystem.git
   cd LibraryManagementSystem
2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate  # On Windows
   # source venv/bin/activate  # On macOS/Linux
3. Install dependencies:
   pip install -r requirements.txt
4. Run Application using this command:
    python main.py 