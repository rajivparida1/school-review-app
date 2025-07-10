from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import DB_CONFIG

app = Flask(__name__)
app.secret_key = 'D3v3ndr@131069'

def get_db_connection():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def home():
    return render_template('home.html', active_page='home')

@app.route('/add-review', methods=['GET', 'POST'])
def add_review():
    if request.method == 'POST':
        school = request.form.get('school_name')
        reviewer = request.form.get('reviewer_name')
        rating = request.form.get('rating', type=int)
        comment = request.form.get('comment')
        location = request.form.get('location')

        if not all([school, reviewer, comment, location]) or not (1 <= rating <= 5):
            return "Invalid input! All fields are required and rating must be between 1 and 5."

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reviews (school_name, reviewer_name, rating, comment, location) VALUES (%s, %s, %s, %s, %s)",
            (school, reviewer, rating, comment, location)
        )
        conn.commit()
        conn.close()
        flash('Review submitted successfully!')
        return redirect(url_for('add_review'))

    return render_template('add_review.html', active_page='add_review')

@app.route('/reviews')
def reviews():
    query = request.args.get('q', '').strip()
    sort_by = request.args.get('sort', 'low_rating')

    conn = get_db_connection()
    cursor = conn.cursor()

    base_query = "SELECT * FROM reviews"
    filters = []
    params = []

    if query:
        filters.append("(school_name LIKE %s OR location LIKE %s)")
        params.extend([f"%{query}%", f"%{query}%"])

    if filters:
        base_query += " WHERE " + " AND ".join(filters)

    # Sort handling
    if sort_by == 'high_rating':
        base_query += " ORDER BY rating DESC"
    else:  # 'low_rating' or default
        base_query += " ORDER BY rating ASC"

    cursor.execute(base_query, tuple(params))
    reviews = cursor.fetchall()
    conn.close()

    if not reviews:
        flash("No reviews found for your search.")

    return render_template('reviews.html', reviews=reviews, query=query, sort_by=sort_by, active_page='reviews')

if __name__ == '__main__':
    app.run(debug=True)
