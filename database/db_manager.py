import sqlite3

class DBManager:
    def __init__(self, db_path="database/dry_cleaning.db"):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_order(self, customer_id, barcode):
        query = """
        INSERT INTO orders (customer_id, barcode, status)
        VALUES (?, ?, 'processing')
        """
        self.cursor.execute(query, (customer_id, barcode))
        self.conn.commit()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            phone_number TEXT
        )
        """)

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_id INTEGER,
            barcode TEXT,
            status TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(customer_id) REFERENCES customers(id)
        )
        """)
        self.conn.commit()

    def create_customer(self, last_name, phone_number):
        self.cursor.execute("""
        INSERT INTO customers (last_name, phone_number)
        VALUES (?, ?)
        """, (last_name, phone_number))
        self.conn.commit()

    def get_next_barcode(self):
        query = "SELECT MAX(id) FROM orders"
        self.cursor.execute(query)
        result = self.cursor.fetchone()[0]

        next_id = 1 if result is None else result + 1
        return str(next_id).zfill(6)

    def get_order_by_barcode(self, barcode):
        query = """
        SELECT * FROM orders
        WHERE barcode = ?
        """
        self.cursor.execute(query, (barcode,))
        return self.cursor.fetchone()

    def mark_order_picked_up(self, barcode):
        query = """
        UPDATE orders
        SET status = 'picked_up'
        WHERE barcode = ?
        """
        self.cursor.execute(query, (barcode,))
        self.conn.commit()
        return self.cursor.rowcount > 0
    
    def get_orders_by_customer(self, customer_id):
        query = """
        SELECT * FROM orders
        WHERE customer_id = ?
        ORDER BY created_at DESC
        """