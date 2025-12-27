from flask import Flask, render_template
import json

app = Flask(__name__)

# Load items from JSON file
def load_items():
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            return data.get("items", [])
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return []

# Route to display items
@app.route('/items')
def items():
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
