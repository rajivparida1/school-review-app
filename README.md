
#  School Review Web App

A full-stack Flask web application that allows users to submit, view, search, and sort reviews of schools. The reviews are stored in a MySQL database and displayed on a clean, responsive Bootstrap interface.

---

## Features

- Submit school reviews with:
  - School Name
  - Reviewer Name
  - Rating (1–5)
  - Comment
  - Location
- Search reviews by **school name** or **location**
- Sort reviews by:
  - Rating (Low to High)
  - Rating (High to Low)
  - Star icons for rating display
  - Flash messages for user feedback
  - Form validation (required fields & rating range)

---

## Tech Stack

| Layer     | Technology                 |
|---------- |----------------------------|
| Backend   | Python (Flask)             |
| Database  | MySQL                      |
| Frontend  | HTML, CSS, Bootstrap, Jinja2 |
| Config    | `.env` / `config.py` for DB credentials

---

## Project Structure

```
school_review_app/
├── app.py                  # Main Flask application
├── templates/
│   ├── home.html
│   ├── add_review.html     # Review form page
│   └── reviews.html        # Review listing/search page
├── static/
│   └── style.css           # Optional styling
├── config.py               # Database config (imported from env or secure values)
├── .env                    # Hidden file for DB credentials (optional)
├── requirements.txt        # Python dependencies
├── reviews.sql             # SQL schema to create 'reviews' table
```

---

## Installation & Setup

### Prerequisites

- Python 3.10+
- MySQL Server (e.g., XAMPP, WAMP, or standalone)
- `pip` package manager

### Clone the Repository

```bash
git clone https://github.com/rajivparida1/school-review-app.git
cd school-review-app
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Setup MySQL Database

1. Start MySQL server (via XAMPP/WAMP or MySQL Workbench).
2. Open **phpMyAdmin** or your MySQL CLI.
3. Run the SQL script from `reviews.sql`:

```sql
CREATE DATABASE IF NOT EXISTS school_reviews;

USE school_reviews;

CREATE TABLE reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100),
    reviewer_name VARCHAR(100),
    rating INT,
    comment TEXT,
    location VARCHAR(100)
);
```

### Configure Database Connection

Edit `config.py` with your credentials:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_mysql_user',
    'password': 'your_mysql_password',
    'database': 'school_reviews'
}
```

> Avoid hardcoding sensitive data in production; use `.env` + `python-dotenv` instead.

---

## Run the App

```bash
python app.py
```

Then visit `http://127.0.0.1:5000/` in your browser.
