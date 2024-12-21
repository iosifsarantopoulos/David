from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTextEdit

class Help(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.layoutUI()
        self.CSS_styling()
        self.Text()
        self.ToWork()

    def initUI(self):
        ## Label ##
        self.help_label = QLabel("Command Panel")

        ## TextEdit ##
        # Αντί για self.help_text = QTextEdit()
        self.help_text = QTextEdit()
        self.help_text.setReadOnly(True)
        self.help_text.setFixedSize(473, 280)

        ## Button ##
        self.help_btn = QPushButton("Done")
        self.help_btn.setFixedSize(100, 30)
        self.help_btn.clicked.connect(lambda x: self.hide())

    def layoutUI(self):
        ## Layout ##
        self.help_layout_0 = QVBoxLayout()

        ## Layout Composition ##
        self.help_layout_0.addWidget(self.help_label, alignment = Qt.AlignLeft)
        self.help_layout_0.addWidget(self.help_text, alignment = Qt.AlignCenter)
        self.help_layout_0.addWidget(self.help_btn, alignment = Qt.AlignRight)

        ## To Work ##
        self.setLayout(self.help_layout_0)

    def CSS_styling(self):
        self.setStyleSheet("""
            QWidget{
                background-color: #f7c600;
            }

            QLabel{
                font-family: impact;
                font-size: 26px;
                color: #333333;
            }
            
            QTextEdit{
                border: 3px solid #333333;
                border-radius: 10px;
                background-color: white;
                color: #333333;
                font-size: 18px;
            }
            
            QScrollBar:vertical {
                background: #f0f0f0; /* Φόντο της scrollbar */
                width: 10px;         /* Πλάτος της scrollbar */
                border: 1px solid #ccc;
                border-radius: 10px; /* Στρογγυλεμένες γωνίες για τη scrollbar */
            }
            
            QScrollBar::handle:vertical {
                background: #888;    /* Χρώμα του "handle" */
                min-height: 20px;    /* Ελάχιστο ύψος */
                border-radius: 5px;  /* Στρογγυλεμένες γωνίες στο handle */
            }
            
            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none; /* Χρώμα της περιοχής πάνω/κάτω από το handle */
                border-radius: 10px; /* Στρογγυλεμένες γωνίες σε αυτές τις περιοχές */
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

    def Text(self):
        self.help_text.setText("·Calculator - Open a Calculator"
                               "\n\n·Recommender - It will recommend to you movies, series and music"
                               "\n\n·Weather - Open a Weather App"
                               "\n\n·Currency Converter - You can input an amount, select currencies, and view real-time conversion result"
                               "\n\n·BMI - You can calculate your BMI"
                               "\n\n·Encrypt - You can encrypt your message (in binary system)"
                               "\n\n·Decrypt - You can decrypt your message (from binary system)")
    def ToWork(self):
        self.setWindowTitle("Help")
        self.setFixedSize(500, 400)

        self.show()