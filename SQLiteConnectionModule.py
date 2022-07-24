import sqlite3

# DB Connection
conn = sqlite3.connect("Proyect Client Management/CRM.db")
c = conn.cursor()

c.execute("""
    CREATE TABLE if not exists crm (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        name TEXT NOT NULL,
        telephone FLOAT NOT NULL,
        brand TEXT NOT NULL
    );
""")
conn.commit()