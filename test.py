import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget


class HTMLImageApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('HTML Image in PyQt')

        # Create a central widget and set the layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Create a QLabel to display HTML content
        html_label = QLabel(self)
        layout.addWidget(html_label)

        # Set HTML content with an image tag
        html_content = '<html><body><img src="ascii_art.html" alt="Image"></body></html>'
        html_label.setText(html_content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = HTMLImageApp()
    window.show()
    sys.exit(app.exec())
