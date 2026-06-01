from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel

class CustomerView(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        #INPUTS
        self.last_name_input = QLineEdit()
        self.last_name_input.setPlaceholderText("Last Name")

        self.phone_number_input = QLineEdit()
        self.phone_number_input.setPlaceholderText("Phone Number")

        # CREATE BUTTON
        self.create_btn = QPushButton("Create Customer")

        # RESULT LABEL
        self.result = QLabel("")

        # ADD TO LAYOUT
        layout.addWidget(self.last_name_input)
        layout.addWidget(self.phone_number_input)
        layout.addWidget(self.create_btn)
        layout.addWidget(self.result)

        self.setLayout(layout)

        #STYLES
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

        self.last_name_input.setStyleSheet(input_style)
        self.phone_number_input.setStyleSheet(input_style)

        self.create_btn.setStyleSheet("""
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