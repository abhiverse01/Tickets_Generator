import sqlite3


# Connect to your SQLite DB
def connect_db():
    conn = sqlite3.connect('ticket_database.db')
    return conn


# Create table if it doesn't exist
def create_table_if_not_exists(conn):
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id TEXT PRIMARY KEY,
            location TEXT NOT NULL,
            date TEXT NOT NULL,
            image_path TEXT NOT NULL
        );
    """)
    conn.commit()


# Add ticket details into DB
def add_ticket(conn, ticket_id, location, date, image_path):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tickets (id, location, date, image_path) VALUES (?, ?, ?, ?);",
                   (ticket_id, location, date, image_path))
    conn.commit()


# Get ticket details from DB
def get_ticket(conn, ticket_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets WHERE id = ?;", (ticket_id,))
    return cursor.fetchone()


# Get all ticket details to be retrieved when the user wants
def get_all_tickets(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tickets;")
    return cursor.fetchall()
