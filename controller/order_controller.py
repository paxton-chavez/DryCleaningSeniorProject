from database.db_manager import DBManager
from PyQt6.QtWidgets import QInputDialog

class OrderController:
    def __init__(self):
        self.db = DBManager()

    def get_order_by_barcode(self, barcode):
        return self.db.get_order_by_barcode(barcode)
    
    def get_next_barcode(self):
        return self.db.get_next_barcode()

    def mark_order_picked_up(self, barcode):
        return self.db.mark_order_picked_up(barcode)
    
    def get_orders_by_customer(self, customer_id):
        return self.db.get_orders_by_customer(customer_id)
    
    def create_order(self, customer_id, barcode):
        return self.db.create_order(customer_id, barcode)
    
    def create_customer(self, last_name, phone_number):
        return self.db.create_customer(last_name, phone_number)
    