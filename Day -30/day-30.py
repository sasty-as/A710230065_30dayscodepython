import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class TemperatureConverter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Konversi Suhu Celcius")
        self.setGeometry(100, 100, 300, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Celcius input
        celcius_layout = QHBoxLayout()
        celcius_label = QLabel("Celcius")
        self.celcius_input = QLineEdit()
        celcius_layout.addWidget(celcius_label)
        celcius_layout.addWidget(self.celcius_input)
        layout.addLayout(celcius_layout)

        # Convert button
        self.convert_button = QPushButton("Konversi Suhu")
        self.convert_button.clicked.connect(self.convert_temperature)
        layout.addWidget(self.convert_button)

        # Results
        self.fahrenheit_result = QLineEdit()
        self.fahrenheit_result.setReadOnly(True)
        self.kelvin_result = QLineEdit()
        self.kelvin_result.setReadOnly(True)
        self.reamur_result = QLineEdit()
        self.reamur_result.setReadOnly(True)

        layout.addWidget(QLabel("Fahrenheit"))
        layout.addWidget(self.fahrenheit_result)
        layout.addWidget(QLabel("Kelvin"))
        layout.addWidget(self.kelvin_result)
        layout.addWidget(QLabel("Reamur"))
        layout.addWidget(self.reamur_result)

    def convert_temperature(self):
        try:
            celcius = float(self.celcius_input.text())
            fahrenheit = (celcius * 9/5) + 32
            kelvin = celcius + 273.15
            reamur = celcius * 4/5

            self.fahrenheit_result.setText(f"{fahrenheit:.2f}")
            self.kelvin_result.setText(f"{kelvin:.1f}")
            self.reamur_result.setText(f"{reamur:.1f}")
        except ValueError:
            self.fahrenheit_result.setText("Error")
            self.kelvin_result.setText("Error")
            self.reamur_result.setText("Error")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemperatureConverter()
    window.show()
    sys.exit(app.exec_())