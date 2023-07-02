from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, \
    QMessageBox, QDateEdit, QTextEdit, QHBoxLayout, QFrame
from db import connect_db, add_ticket, get_ticket, get_all_tickets
from ticket import generate_ticket
from PyQt5.QtCore import QDate
from PyQt5.QtGui import QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Travel Manager")
        self.setFixedSize(700, 500)

        self.conn = connect_db()

        self.layout = QVBoxLayout()

        # Add a title on the homepage
        self.layout.addWidget(QLabel("Welcome to the Travel Manager"))

        self.homepage_button = QPushButton("Go to Tickets")
        self.homepage_button.clicked.connect(self.load_tickets_frame)
        self.layout.addWidget(self.homepage_button)

        # Footer
        self.footer = QLabel("Developed by: Abhishek Shah | Developed Year: 2023")
        self.layout.addWidget(self.footer)

        # Ticket frame (initially hidden)
        self.ticket_frame = QFrame()
        self.ticket_frame.setFrameShape(QFrame.StyledPanel)
        self.ticket_frame.hide()
        self.ticket_layout = QVBoxLayout(self.ticket_frame)

        self.ticket_layout.addWidget(QLabel("Ticket ID:"))
        self.id_input = QLineEdit()
        self.ticket_layout.addWidget(self.id_input)

        self.ticket_layout.addWidget(QLabel("Location:"))
        self.location_input = QLineEdit()
        self.ticket_layout.addWidget(self.location_input)

        self.ticket_layout.addWidget(QLabel("Date:"))
        self.date_input = QDateEdit(QDate.currentDate())
        self.ticket_layout.addWidget(self.date_input)

        self.generate_button = QPushButton("Generate Ticket")
        self.generate_button.clicked.connect(self.generate_ticket_action)
        self.ticket_layout.addWidget(self.generate_button)

        self.view_all_button = QPushButton("View All Tickets")
        self.view_all_button.clicked.connect(self.view_all_tickets_action)
        self.ticket_layout.addWidget(self.view_all_button)

        self.tickets_display = QTextEdit()
        self.tickets_display.setReadOnly(True)
        self.ticket_layout.addWidget(self.tickets_display)

        self.layout.addWidget(self.ticket_frame)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)

    def load_tickets_frame(self):
        self.homepage_button.hide()
        self.ticket_frame.show()

    def generate_ticket_action(self):
        ticket_id = self.id_input.text()
        location = self.location_input.text()
        date = self.date_input.text()

        if not ticket_id or not location or not date:
            QMessageBox.warning(self, "Input Error", "All fields must be filled!")
            return

        image_path = generate_ticket(ticket_id, location, date)
        add_ticket(self.conn, ticket_id, location, date, image_path)

        QMessageBox.information(self, "Success", f"Ticket {ticket_id} has been generated successfully!")

    def view_all_tickets_action(self):
        tickets = get_all_tickets(self.conn)

        tickets_text = "\n".join(
            [f"ID: {ticket[0]}, Location: {ticket[1]}, Date: {ticket[2]}, Image Path: {ticket[3]}" for ticket in
             tickets])

        self.tickets_display.setPlainText(tickets_text)
