from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Initialize Database
def init_db():
    conn = sqlite3.connect('trashsync.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pickups (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        user TEXT, 
                        location TEXT, 
                        date TEXT, 
                        status TEXT DEFAULT 'Pending')''')
    conn.execute('''CREATE TABLE IF NOT EXISTS cleaners (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT, 
                        contact TEXT, 
                        status TEXT DEFAULT 'Available')''')
    conn.commit()
    conn.close()

init_db()  # Initialize DB on start

@app.route('/')
def home():
    return jsonify({"message": "Welcome to TrashSync API"})

# Schedule Waste Pickup
@app.route('/schedule', methods=['POST'])
def schedule_pickup():
    data = request.json
    conn = sqlite3.connect('trashsync.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO pickups (user, location, date) VALUES (?, ?, ?)", 
                   (data['user'], data['location'], data['date']))
    
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Pickup Scheduled"}), 201

# View All Scheduled Pickups
@app.route('/pickups', methods=['GET'])
def get_pickups():
    conn = sqlite3.connect('trashsync.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pickups")
    pickups = cursor.fetchall()
    conn.close()
    
    return jsonify(pickups)

# Report Uncollected Trash
@app.route('/report', methods=['POST'])
def report_trash():
    data = request.json
    conn = sqlite3.connect('trashsync.db')
    cursor = conn.cursor()
    
    # Check if the pickup ID exists
    cursor.execute("SELECT * FROM pickups WHERE id = ?", (data['id'],))
    existing_pickup = cursor.fetchone()
    
    if not existing_pickup:
        conn.close()
        return jsonify({"message": "Pickup ID not found"}), 404  # If ID doesn't exist
    
    # Update the status to 'Uncollected'
    cursor.execute("UPDATE pickups SET status = 'Uncollected' WHERE id = ?", (data['id'],))
    conn.commit()
    conn.close()
    
    return jsonify({"message": "Trash Reported"}), 200

if __name__ == '__main__':
    app.run(debug=True)
