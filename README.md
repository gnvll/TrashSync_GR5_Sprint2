# TrashSync - Smart Waste Management System

TrashSync is a simple waste management system that allows users to schedule trash pickups, track pickup statuses, and report uncollected trash.

This project is built with:
- Python (Flask) - Backend API
- SQLite - Lightweight database
- HTML, CSS, JavaScript - Frontend

## Features
- Schedule a trash pickup
- View scheduled pickups
- Report uncollected trash
- RESTful API for easy integration

---

## Installation & Setup

### Prerequisites
- Python 3.10+ installed
- VS Code (or any IDE)
- Postman (for API testing)

### How to Install & Run the Project

1. Clone the repository:
```sh
git clone https://github.com/YOUR_USERNAME/TrashSync.git
cd TrashSync
```

2. Create a virtual environment & activate it:
```sh
python -m venv env          # Windows
env\Scripts\activate

python -m venv env          # Mac/Linux
source env/bin/activate
```

3. Install dependencies:
```sh
pip install flask sqlite3
```
 
4. Initialize the database:
```sh
python database.py
```

5. Start the Flask server:
```sh
python server.py
```

6. Open `index.html` in your browser:
- Right-click → Open with Live Server  

## API Documentation

The backend provides RESTful APIs for scheduling and reporting waste pickups.

### POST /schedule - Schedule a Pickup 
**Request:**
```json
{
 "user": "John Doe",
 "location": "123 Main St",
 "date": "2025-02-27"
}
```

**Response:**
```json
{"message": "Pickup Scheduled"}
```

### GET /pickups - Retrieve All Pickups
**Response:**
```
[
    [1, "John Doe", "123 Main St", "2025-02-27", "Pending"]
]
```

### POST /report - Report Uncollected Trash:
**Request:**
```json
{
    "id": 1
}
```

**Response:**
```json
{"message": "Trash Reported"}
```

## Frontend Usage

The frontend is a simple HTML+CSS+JS webpage that allows users to:
* Schedule trash pickups
* Report uncollected trash
* View scheduled pickups

To use the frontend:
1. Open index.html in  browser
2. Fill out the "Schedule Pickup" form and submit
3. The pickup should appear in the list
4. To report an issue, enter the Pickup ID in the "Report Trash" form and submit

## Testing Instructions

Use Postman to test the API:

1. Start Flask Server:
python server.py

2. Test Endpoints in Postman:
* POST /schedule - Add a pickup
* GET /pickups - View pickups
* POST /report - Report a pickup

Confirm changes via GET /pickups
