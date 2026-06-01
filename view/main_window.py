from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout,
    QVBoxLayout, QPushButton, QStackedWidget, QLabel
)
from PyQt6.QtCore import Qt

from view.customer_view import CustomerView
from view.order_view import OrderView
from view.pickup_view import PickupView


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dry Cleaning System")
        self.setMinimumSize(1000, 600)

        # CENTRAL WIDGET
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout()
        central_widget.setLayout(main_layout)

        # SIDEBAR
        sidebar_layout = QVBoxLayout()

        self.btn_customers = QPushButton("Customers")
        self.btn_orders = QPushButton("Orders")
        self.btn_pickup = QPushButton("Pickup")

        self.button_style = """
        QPushButton {
            background-color: #0B1B3B;
            color: white;
            border-radius: 12px;
            padding: 12px;
            font-size: 14px;
        }
        QPushButton:hover {
            background-color: #132B5C;
        }
        """

        self.btn_customers.setStyleSheet(self.button_style)
        self.btn_orders.setStyleSheet(self.button_style)
        self.btn_pickup.setStyleSheet(self.button_style)

        sidebar_layout.addWidget(self.btn_customers)
        sidebar_layout.addWidget(self.btn_orders)
        sidebar_layout.addWidget(self.btn_pickup)
        sidebar_layout.addStretch()

        sidebar_container = QWidget()
        sidebar_container.setLayout(sidebar_layout)
        sidebar_container.setFixedWidth(200)
        sidebar_layout.setSpacing(10)
        sidebar_layout.setContentsMargins(10, 20, 10, 10)
        sidebar_container.setStyleSheet("""
        background-color: #5FA8D3;
        """)
        sidebar_layout.setSpacing(25)
        sidebar_layout.setContentsMargins(20, 40, 20, 20)

        # STACKED PAGES
        self.stack = QStackedWidget()

        # PAGES
        self.customer_page = CustomerView()
        self.order_page = OrderView()
        self.pickup_page = PickupView()

        # ADD PAGES TO STACK
        self.stack.addWidget(self.customer_page)  # index 0
        self.stack.addWidget(self.order_page)     # index 1
        self.stack.addWidget(self.pickup_page)    # index 2

        self.stack.setStyleSheet("""
            background-color: #F8FAFC;
        """)

        # MAIN CONTENT CONTAINER 
        content_container = QWidget()
        content_layout = QVBoxLayout()
        content_container.setLayout(content_layout)

        # TITLE 
        self.title = QLabel("Wow! Dry Cleaners")
        self.title.setStyleSheet("""
            color: #0B1B3B;
            font-size: 32px;
            font-weight: bold;
            padding: 30px;
            background-color: #F8FAFC;
        """)

        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # ADD TITLE + STACK 
        content_layout.addWidget(self.title)
        content_layout.addWidget(self.stack)

        # ADD TO MAIN LAYOUT 
        main_layout.addWidget(sidebar_container)
        main_layout.addWidget(content_container)

        # BUTTON CONNECTIONS 
        self.btn_customers.clicked.connect(lambda: self.set_active(0))
        self.btn_orders.clicked.connect(lambda: self.set_active(1))
        self.btn_pickup.clicked.connect(lambda: self.set_active(2))

        # DEFAULT PAGE 
        self.stack.setCurrentIndex(0)
        self.set_active(0)
    
    def set_active(self, index):
        self.stack.setCurrentIndex(index)

        #  RESET ALL BUTTON STYLES
        self.btn_customers.setStyleSheet(self.button_style)
        self.btn_orders.setStyleSheet(self.button_style)
        self.btn_pickup.setStyleSheet(self.button_style)

        self.button_style = """
        QPushButton {
            background-color: #0B1B3B;
            color: white;
            border-radius: 15px;
            padding: 20px;
        }
        QPushButton:hover {
            background-color: #132B5C;
        }
        """

        # HIGHLIGHT ACTIVE BUTTON
        active_style = self.button_style + """
        QPushButton {
            background-color: #0B1B3B;
            color: white;
        }
        """

        if index == 0:
            self.btn_customers.setStyleSheet(active_style)
        elif index == 1:
            self.btn_orders.setStyleSheet(active_style)
        elif index == 2:
            self.btn_pickup.setStyleSheet(active_style)