from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # потрібно для flash-повідомлень

GUESTS_FILE = 'guests.json'

def load_guests():
    if not os.path.exists(GUESTS_FILE):
        return []
    with open(GUESTS_FILE, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_guests(guests):
    with open(GUESTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(guests, f, indent=4, ensure_ascii=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        if not name or not message:
            flash('Ім\'я та повідомлення не можуть бути порожніми.')
            return redirect(url_for('index'))

        new_entry = {
            'name': name,
            'message': message,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        guests = load_guests()
        guests.append(new_entry)
        save_guests(guests)

        return redirect(url_for('index'))

    guests = load_guests()
    return render_template('index.html', guests=guests)

if __name__ == '__main__':
    app.run(debug=True)