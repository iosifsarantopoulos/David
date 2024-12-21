from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.layoutUI()
        self.CSS_styling()
        self.ToWork()

    def initUI(self):
        ## LineEdit ##
        self.com_line = QLineEdit()
        self.com_line.setReadOnly(True)

        ## Buttons ##
        self.buttons = {
            "0": QPushButton("0"),
            "1": QPushButton("1"),
            "2": QPushButton("2"),
            "3": QPushButton("3"),
            "4": QPushButton("4"),
            "5": QPushButton("5"),
            "6": QPushButton("6"),
            "7": QPushButton("7"),
            "8": QPushButton("8"),
            "9": QPushButton("9"),
            "C": QPushButton("C"),
            "+": QPushButton("+"),
            "-": QPushButton("-"),
            "*": QPushButton("*"),
            "/": QPushButton("/"),
            ".": QPushButton("."),
            "=": QPushButton("="),
        }

        for key, button in self.buttons.items():
            button.clicked.connect(lambda checked, k=key: self.on_button_click(k))

    def layoutUI(self):
        ## Layouts ##
        self.layout_0 = QVBoxLayout()

        self.layout_1 = QHBoxLayout()
        self.layout_2 = QHBoxLayout()

        self.layout_21 = QVBoxLayout()
        self.layout_22 = QVBoxLayout()
        self.layout_23 = QVBoxLayout()
        self.layout_24 = QVBoxLayout()

        ## Layouts Composition ##
        self.layout_1.addWidget(self.com_line, alignment = Qt.AlignCenter)

        ## Buttons Arrangement ##
        self.layout_21.addWidget(self.buttons["7"])
        self.layout_21.addWidget(self.buttons["4"])
        self.layout_21.addWidget(self.buttons["1"])
        self.layout_21.addWidget(self.buttons["."])

        self.layout_22.addWidget(self.buttons["8"])
        self.layout_22.addWidget(self.buttons["5"])
        self.layout_22.addWidget(self.buttons["2"])
        self.layout_22.addWidget(self.buttons["0"])

        self.layout_23.addWidget(self.buttons["9"])
        self.layout_23.addWidget(self.buttons["6"])
        self.layout_23.addWidget(self.buttons["3"])
        self.layout_23.addWidget(self.buttons["C"])

        self.layout_24.addWidget(self.buttons["+"])
        self.layout_24.addWidget(self.buttons["-"])
        self.layout_24.addWidget(self.buttons["*"])
        self.layout_24.addWidget(self.buttons["/"])
        self.layout_24.addWidget(self.buttons["="])

        ## To Work ##
        self.layout_2.addLayout(self.layout_21)
        self.layout_2.addLayout(self.layout_22)
        self.layout_2.addLayout(self.layout_23)
        self.layout_2.addLayout(self.layout_24)

        self.layout_0.addLayout(self.layout_1)
        self.layout_0.addLayout(self.layout_2)

    def CSS_styling(self):
        ## Nicknames ##
        self.buttons["+"].setObjectName("button")
        self.buttons["-"].setObjectName("button")
        self.buttons["*"].setObjectName("button")
        self.buttons["/"].setObjectName("button")
        self.buttons["="].setObjectName("button")
        self.buttons["C"].setObjectName("button")

        ## CSS Styling ##
        self.setStyleSheet("""
            QWidget{
                background-color: #f7c600;
            }

            QLineEdit{
                font-family: impact;
                font-size: 26px;
                border: 2px solid #333333;
                border-radius: 10px;
                background-color: white;
                color: #333333;
                width: 450px;
                height:40px;
            }

            QPushButton{
                border: 5px solid #333333;
                border-radius: 20px;
                font-size: 26px;
                font-family: impact;
                color: white;
                    background-color: #333333;
                }

                QPushButton:pressed{
                    background-color: #474954;
                }

                #button{
                    border: 5px solid #e07a5f;
                    border-radius: 20px;
                    font-size: 26px;
                    font-family: impact;
                    color: white;
                    background-color: #e07a5f;
                }

                #button:pressed{
                    background-color: #ed9985;
                }
                """)

    def on_button_click(self, key):
        current_text = self.com_line.text()

        if key == "C":
            self.com_line.clear()
        elif key == "=":
            try:
                result = str(eval(current_text.replace(",", ".")))
                self.com_line.setText(result)
            except Exception as e:
                self.com_line.setText("Error")
        else:
            # Προσθήκη στο κείμενο
            self.com_line.setText(current_text + key)

    def ToWork(self):
        self.setWindowTitle("Calculator")
        self.setFixedSize(500, 400)
        self.setLayout(self.layout_0)
        self.show()

