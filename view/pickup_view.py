from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel
from controller.order_controller import OrderController


class PickupView(QWidget):
    def __init__(self):
        super().__init__()

        self.controller = OrderController()

        layout = QVBoxLayout()

        # INPUT
        self.barcode_input = QLineEdit()
        self.barcode_input.setPlaceholderText("Scan or enter barcode")

        # BUTTONS
        self.lookup_btn = QPushButton("Lookup Order")
        self.pickup_btn = QPushButton("Mark Picked Up")

        # RESULT LABEL 
        self.result = QLabel("")

        # ADD TO LAYOUT
        layout.addWidget(QLabel("PICKUP PAGE"))
        layout.addWidget(self.barcode_input)
        layout.addWidget(self.lookup_btn)
        layout.addWidget(self.pickup_btn)
        layout.addWidget(self.result)

        self.setLayout(layout)

        # APPLY STYLES
        input_style = """
        QLineEdit {
            background-color: white;
            color: black;
            border: 2px solid #0B1B3B;
            border-radius: 8px;
            padding: 10px;
            font-size: 14px;
        }
        QLineEdit::placeholder {
            color: gray;
        }
        """

        self.barcode_input.setStyleSheet(input_style)

        button_style = """
        QPushButton {
            background-color: #0B1B3B;
            color: white;
            border-radius: 10px;
            padding: 12px;
        }
        QPushButton:hover {
            background-color: #132B5C;
        }
        """

        self.lookup_btn.setStyleSheet(button_style)
        self.pickup_btn.setStyleSheet(button_style)

        self.result.setStyleSheet("""
            color: #0B1B3B;
            font-size: 14px;
        """)

        layout.setSpacing(15)
        layout.setContentsMargins(40, 20, 40, 20)


        # CONNECTIONS
        self.lookup_btn.clicked.connect(self.lookup)
        self.pickup_btn.clicked.connect(self.pickup)

    def lookup(self):
        barcode = self.barcode_input.text().strip()

        order = self.controller.get_order_by_barcode(barcode)

        if not order:
            self.result.setText("Not found")
            return

        self.result.setText(f"Status: {order[3]}")

    def pickup(self):
        barcode = self.barcode_input.text().strip()

        success = self.controller.mark_order_picked_up(barcode)

        self.result.setText("Picked up" if success else "Failed")