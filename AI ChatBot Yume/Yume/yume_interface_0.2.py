import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QColor, QPalette, QBrush, QTextCharFormat, QFontDatabase

from yume import get_response


class ChatInterface(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Yume")
        self.setGeometry(0, 0, 1920, 1080)

        # Load the background image
        self.background_image = QPixmap("solo leveling 1920x1080.png")
        self.background_label = QLabel(self)
        self.background_label.setPixmap(self.background_image)
        self.background_label.setGeometry(0, 0, 1920, 1080)
        self.background_label.lower()  # Ensure the background image is behind other widgets

        # Create layout
        layout = QVBoxLayout()

        # Create a label for the tag
        self.tag_label = QLabel("Yume is Summoned!", self)
        (self.tag_label.setStyleSheet
         ("font-size: 24px; border: none; color: white; background-color: rgba(0, 0, 0, 100);"))
        layout.addWidget(self.tag_label)  # Add the tag label to the layout

        # Create chat area with larger font size
        self.chat_area = QTextEdit()
        self.chat_area.setReadOnly(True)
        (self.chat_area.setStyleSheet
         ("background-color: rgba(0, 0, 0, 100); font-size: 18px; color: purple; border: none;"))  # Increased font size
        layout.addWidget(self.chat_area)

        # Create user input field with larger font size
        self.user_input = QLineEdit()
        self.user_input.returnPressed.connect(self.send_message)
        (self.user_input.setStyleSheet
         ("background-color: rgba(0, 0, 0, 100); font-size: 18px; color: purple; border: none;"))  # Increased font size
        layout.addWidget(self.user_input)

        # Create send button with larger font size
        self.send_button = QPushButton("Send")
        self.send_button.clicked.connect(self.send_message)
        (self.send_button.setStyleSheet
         ("background-color: rgba(0, 0, 0, 100); font-size: 18px; color: red; border: none;"))  # Increased font size
        layout.addWidget(self.send_button)

        self.setLayout(layout)

    def send_message(self):
        message = self.user_input.text().lower()
        self.display_message(message, "Otaku")
        self.user_input.clear()
        # Simulate processing the message
        response = get_response(message)
        self.display_message(response, "Yume")
        # Check if the message is "goodbye"
        if message == "goodbye":
            self.display_message("Sayonara", "Yume")
            self.close()  # Close the application

    def display_message(self, message, sender):
        # Define colors for different senders
        color_map = {
            "Otaku": Qt.violet,  # Color for Otaku messages
            "Yume": Qt.green  # Color for Yume messages
        }

        # Create a QTextCharFormat object for the sender's color
        format = QTextCharFormat()
        format.setForeground(QColor(color_map[sender]))

        # Append the message to the chat area with the specified format
        cursor = self.chat_area.textCursor()
        cursor.insertText(f"{sender}: {message}\n", format)
        self.chat_area.setTextCursor(cursor)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    chat_interface = ChatInterface()
    chat_interface.show()
    sys.exit(app.exec_())
