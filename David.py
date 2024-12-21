import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QRadioButton, QPushButton,
                             QLabel, QListWidget, QLineEdit, QTextEdit)
from calculator import Calculator
from help import Help


class David(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.layoutUI()
        self.CSS_styling()
        self.ToWork()


    def initUI(self):
        ## Labels ##
        self.david_label = QLabel("David")
        self.quest_label = QLabel("Your Question")
        self.notes_label = QLabel("Notes")

        ## TextEdits-LineEdits ##
        self.david_edit = QTextEdit()
        self.david_edit.setReadOnly(True)

        self.notes_edit = QTextEdit()

        self.quest_edit = QLineEdit()
        self.quest_edit.setPlaceholderText("Your Command...")

        self.david_edit.setFixedSize(480, 600)
        self.notes_edit.setFixedSize(350, 480)

        ## Buttons ##
        self.done_btn = QPushButton("Done")
        self.done_btn.clicked.connect(self.Done)

        self.help_btn = QPushButton("Help")
        self.help_btn.clicked.connect(self.Help)

        self.done_btn.setFixedSize(100, 30)
        self.help_btn.setFixedSize(100, 30)

    def layoutUI(self):
        ## Layouts ##
        self.layout_0 = QHBoxLayout()
        self.layout_1 = QVBoxLayout()
        self.layout_2 = QVBoxLayout()
        self.layout_21 = QVBoxLayout()
        self.layout_22 = QVBoxLayout()
        self.layout_23 = QHBoxLayout()

        ## Layouts Composition ##
        self.layout_1.addWidget(self.david_label, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.layout_1.addWidget(self.david_edit, alignment = Qt.AlignLeft)

        self.layout_21.addWidget(self.quest_label, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.layout_21.addWidget(self.quest_edit, alignment = Qt.AlignLeft | Qt.AlignBottom)

        self.layout_22.addWidget(self.notes_label, alignment = Qt.AlignTop | Qt.AlignLeft)
        self.layout_22.addWidget(self.notes_edit, alignment = Qt.AlignLeft)

        self.layout_23.addWidget(self.done_btn, alignment = Qt.AlignLeft)
        self.layout_23.addWidget(self.help_btn, alignment = Qt.AlignRight)

        self.layout_2.setSpacing(10)

        ## To Work ##

        self.layout_2.addLayout(self.layout_21)
        self.layout_2.addLayout(self.layout_22)
        self.layout_2.addLayout(self.layout_23)

        self.layout_0.addLayout(self.layout_1, stretch=3)
        self.layout_0.addLayout(self.layout_2, stretch=2)

    def CSS_styling(self):
        ## Nicknames ##
        self.david_edit.setObjectName("david_edit")
        self.notes_edit.setObjectName("notes_edit")

        ## CSS Styling ##

        self.setStyleSheet("""
            QWidget{
                background-color: #f7c600;
            }

            QLabel{
                font-family: impact;
                font-size: 26px;
                color: #333333;
            }

            QLineEdit{
                font-family: calibri;
                font-size: 15px;
                border: 2px solid #333333;
                border-radius: 10px;
                background-color: white;
                color: #333333;
                width: 350px;
                height:30px;
            }

            QTextEdit{
                border: 3px solid #333333;
                border-radius: 10px;
                background-color: white;
                color: #333333;
                font-size: 18px;
            }

            #david_edit{
                width: 700px;
                height: 100px;
            }
            QScrollBar:vertical {
                background: #f0f0f0; /* Φόντο της κάθετης scrollbar */
                width: 10px;        /* Πλάτος της scrollbar */
                border: 3px solid #ccc;
            }

            QScrollBar::handle:vertical {
                background: #888;   /* Χρώμα του "χειριστηρίου" (handle) */
                min-height: 20px;   /* Ελάχιστο ύψος */
                border-radius: 10px; /* Στρογγυλεμένες γωνίες */
            }

            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: #ccc; /* Χρώμα για τα κουμπιά πάνω/κάτω (προαιρετικά) */
                height: 0px;      /* Απενεργοποίηση των κουμπιών */
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none; /* Χρώμα της περιοχής πάνω/κάτω από το handle */
            }

            QPushButton{
                border: 2px solid #333333;
                border-radius: 10px;
                font-size: 26px;
                font-family: impact;
                color: white;
                background-color: #333333;
            }

            QPushButton:pressed {
                background-color: #474954;
            }
        """)


    def Done(self):
        self.quest_edit_text = self.quest_edit.text()
        self.quest_edit_text.lower()

        if self.quest_edit_text == "calculator" or self.quest_edit_text == "calc":
            self.calc = Calculator()

            if self.result == "":
                self.result = self.result + "Calculator Open"
            else:
                self.result = self.result + "\nCalculator Open"
            self.david_edit.setText(self.result)
            self.quest_edit.clear()

        else:
            if self.result == "":
                self.result = self.result + "Error"
            else:
                self.result = self.result +"\nError"

            self.david_edit.setText(self.result)
            self.quest_edit.clear()
    def Help(self):
        self.help = Help()

        if self.result == "":
            self.result = self.result + "Help Open"
        else:
            self.result = self.result + "\nHelp Open"

        self.david_edit.setText(self.result)
    def ToWork(self):
        self.setFixedSize(900, 700)
        self.setWindowTitle("David")

        self.result = ""

        self.setLayout(self.layout_0)
        self.show()


if __name__ == "__main__":
    app = QApplication([])
    quiz = David()
    sys.exit(app.exec_())

