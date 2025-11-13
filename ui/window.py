import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout

def create_main_window():
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('Interview Helper')
    layout = QVBoxLayout()
    label = QLabel('Hello, Interview Helper!')
    layout.addWidget(label)
    window.setLayout(layout)
    window.show()
    sys.exit(app.exec_())
