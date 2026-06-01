from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from controller.order_controller import OrderController

class OrderView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = OrderController()

        layout = QVBoxLayout()

        # Title
        layout.addWidget(QLabel("ORDER PAGE"))

        # Inputs
        self.customer_id_input = QLineEdit()
        self.customer_id_input.setPlaceholderText("Customer ID")

        self.barcode_label = QLabel("Barcode: (auto-generated)")

        # Buttons
        self.create_order_btn = QPushButton("Create Order")

        # Result label
        self.result = QLabel("")

        # Add to layout
        layout.addWidget(self.customer_id_input)
        layout.addWidget(self.barcode_label)
        layout.addWidget(self.create_order_btn)
        layout.addWidget(self.result)

        self.setLayout(layout)

        # Connect button
        self.create_order_btn.clicked.connect(self.create_order)

        # Styling 
        input_style = """
        QLineEdit {
            background-color: white;
            color: black;
            border: 2px solid #0B1B3B;
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
        }
        """

        self.customer_id_input.setStyleSheet(input_style)

        self.create_order_btn.setStyleSheet("""
        QPushButton {
            background-color: #0B1B3B;
            color: white;
            border-radius: 10px;
            padding: 12px;
        }
        QPushButton:hover {
            background-color: #132B5C;
        }
        """)

        layout.setSpacing(15)
        layout.setContentsMargins(40, 20, 40, 20)

        # Initialize barcode
        self.update_barcode()

    def create_order(self):
        barcode = self.current_barcode
        customer = self.customer_id_input.text().strip()

        if not customer:
            self.result.setText("Enter a customer ID")
            return

        try:
            self.controller.create_order(int(customer), barcode)
            self.result.setText("Order created successfully")

            # Generate next barcode
            self.update_barcode()

        except Exception as e:
            self.result.setText(f"Error: {e}")

    def update_barcode(self):
        barcode = self.controller.get_next_barcode()
        self.current_barcode = barcode
        self.barcode_label.setText(f"Barcode: {barcode}")