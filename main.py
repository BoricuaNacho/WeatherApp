import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.cityLabel = QLabel("Enter city name: ", self)
        self.cityInput = QLineEdit(self)
        self.getWeatherButton = QPushButton("Get Weather", self)
        self.temperatureLabel = QLabel("70°F",self)
        self.emojiLabel = QLabel("☀️",self)
        self.descriptionLabel = QLabel("Sunny",self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Weather App")

        vbox = QVBoxLayout()

        vbox.addWidget(self.cityLabel)
        vbox.addWidget(self.cityInput)
        vbox.addWidget(self.getWeatherButton)
        vbox.addWidget(self.temperatureLabel)
        vbox.addWidget(self.emojiLabel)
        vbox.addWidget(self.descriptionLabel)

        self.setLayout(vbox)

        self.cityLabel.setAlignment(Qt.AlignCenter)
        self.cityInput.setAlignment(Qt.AlignCenter)
        self.temperatureLabel.setAlignment(Qt.AlignCenter)
        self.emojiLabel.setAlignment(Qt.AlignCenter)
        self.descriptionLabel.setAlignment(Qt.AlignCenter)

        self.cityLabel.setObjectName("cityLabel")
        self.cityInput.setObjectName("cityInput")
        self.getWeatherButton.setObjectName("getWeatherButton")
        self.temperatureLabel.setObjectName("temperatureLabel")
        self.emojiLabel.setObjectName("emojiLabel")
        self.descriptionLabel.setObjectName("descriptionLabel")

        self.setStyleSheet("""
            QLabel, QPushButton{
                font-family: calibri;               
            }
                           
            QLabel#cityLabel {
                font-size: 40px;
                font-style: italic;
            }
                           
            QLineEdit#cityInput{
                font-size: 40px;
            }               
        
            QPushButton#getWeatherButton{
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperatureLabel{
                font-size: 75px;               
            }
            QLabel#emojiLabel{
                font-size: 100px;
                font-family: Segoe UI emoji;
            }
            QLabel#descriptionLabel{
                font-size: 50px;               
            }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    weatherApp = WeatherApp()
    weatherApp.show()
    sys.exit(app.exec_())


