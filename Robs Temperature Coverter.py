import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QWidget

class TemperatureConverter(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the user interface
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Temperature Converter")
        self.setFixedSize(400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Font configuration
        font = QFont("Arial", 12)

        # QLineEdit widget
        self.temperature_entry = QLineEdit(self)
        self.temperature_entry.setPlaceholderText("Enter temperature")
        self.temperature_entry.setFont(font)
        self.temperature_entry.setStyleSheet("padding: 5px;")
        layout.addWidget(self.temperature_entry)

        # QComboBox widget
        self.unit_combo_box = QComboBox(self)
        self.unit_combo_box.setFont(font)
        self.unit_combo_box.addItems(["Celsius", "Fahrenheit"])
        layout.addWidget(self.unit_combo_box)

        # QPushButton widget
        self.convert_button = QPushButton("Convert", self)
        self.convert_button.setFont(font)
        self.convert_button.setStyleSheet("""
            QPushButton {
                padding: 5px;
                background-color: #64B5F6;
                border: 1px solid #1E88E5;
                border-radius: 4px;
                color: white;
            }
            QPushButton:hover {
                background-color: #42A5F5;
            }
            QPushButton:pressed {
                background-color: #1E88E5;
            }
        """)
        self.convert_button.clicked.connect(self.convert_temperature)
        layout.addWidget(self.convert_button)

        # QLabel widget
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setFont(font)
        layout.addWidget(self.result_label)

    def convert_temperature(self):
        try:
            input_temperature = float(self.temperature_entry.text())
            input_unit = self.unit_combo_box.currentText()

            if input_unit == "Celsius":
                output_temperature = (input_temperature * 9/5) + 32
                output_unit = "°F"
            else:
                output_temperature = (input_temperature - 32) * 5/9
                output_unit = "°C"

            self.result_label.setText(f"{output_temperature:.2f} {output_unit}")

        except ValueError:
            self.result_label.setText("Invalid input")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    temperature_converter = TemperatureConverter()
    temperature_converter.show()
    sys.exit(app.exec_())
