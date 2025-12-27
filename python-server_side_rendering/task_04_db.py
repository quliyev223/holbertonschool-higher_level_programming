from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Path to the SQLite database
DB_FILE = 'products.db'

# Sample data for JSON
products_json = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
    {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
]

# Sample data for CSV
CSV_FILE = 'products.csv'
if not os.path.exists(CSV_FILE):
    # Create CSV file with sample data if it does not exist
    with open(CSV_FILE, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "category", "price"])
        writer.writeheader()
        writer.writerows(products_json)

# Function to create and populate SQLite database
def create_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    cursor.execute('DELETE FROM Products')  # Clear table before inserting
    # Insert sample data
    cursor.executemany('''
        INSERT INTO Products (id, name, category, price)
        VALUES (:id, :name, :category, :price)
    ''', products_json)
    conn.commit()
    conn.close()

# Initialize the database
create_database()

# Function to fetch products from SQLite
def get_products_from_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row  # Return rows as dictionaries
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]  # Convert rows to list of dicts
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return []

# Function to fetch products from CSV
def get_products_from_csv():
    try:
        with open(CSV_FILE, newline='') as f:
            reader = csv.DictReader(f)
            return [row for row in reader]
    except Exception as e:
        print(f"CSV error: {e}")
        return []

# Flask route to display products
@app.route('/products')
def products():
    source = request.args.get('source', 'json').lower()  # Get data source from query param
    if source == 'json':
        data = products_json
    elif source == 'csv':
        data = get_products_from_csv()
    elif source == 'sql':
        data = get_products_from_db()
    else:
        return "Wrong source", 400  # Invalid source error

    # Render the template with the product data
    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
