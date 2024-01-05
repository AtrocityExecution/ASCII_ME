import sys
import math
from PIL import Image, ImageQt, ImageDraw, ImageEnhance, ImageFilter, UnidentifiedImageError, ImageFont
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
from ascii_magic import AsciiArt, Back


class Gui(QMainWindow):
    width = 1000
    height = 800

    def __init__(self):
        super().__init__()
        uic.loadUi("ascii_me_gui.ui", self)

        self.menu_open = self.findChild(QAction, "actionOpen")
        self.photo = self.findChild(QLabel, "picturePlaceholder")

        self.actionOpen.triggered.connect(self.open_file)
        self.actionQuit.triggered.connect(self.exit_app)
        self.actionSave.triggered.connect(self.save_file)
        self.actionSave_As.triggered.connect(self.save_file)

        self.ascii_me_button.clicked.connect(self.ascii_me)

    def open_file(self):
        global file_name
        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '',
                                                   'Image Files (*.png *.jpg *.bmp *.gif);;All files (*)'
                                                   )

        try:
            Image.open(file_name)
            self.load_image()
        except UnidentifiedImageError:
            print("Invalid file.")
            QMessageBox.information(self, "ERROR", "Unable to open image.")

    def save_file(self):

        save_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '',
                                                   'Image Files (*.png *.jpg *.bmp *.gif);;All files (*))',

                                                   )

        try:
            if save_name:
                finalImage.save(save_name)
                print(f"File saved to: {save_name}!")

        except UnidentifiedImageError:
            print("Invalid file.")
            QMessageBox.information(self, "ERROR", "Unable to save image.")

    def load_image(self):
        self.pixmap = QPixmap(file_name)
        self.photo.setPixmap(self.pixmap)

    def exit_app(self):
        message = QMessageBox.question(self, 'Exit', "Are you sure...")

        if message == QMessageBox.StandardButton.Yes:
            QApplication.instance().exit()

    def ascii_me(self):
        global image, finalImage

        if not file_name:
            return

        def getChar(input):
            return charArray[math.floor(input * interval)]

        density = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`.' "[::-1]
        # density = "$@B^`.' "[::-1]
        charArray = list(density)
        charLength = len(charArray)
        interval = charLength / 256

        scaleFactor = 0.2
        charWidth = 10
        charHeight = 18

        text_file = open("output.txt", "w")
        img = Image.open(file_name).convert("RGB")

        font = ImageFont.truetype("C:\\Windows\\Fonts\\LFAX.TTF", 14)

        width, height = img.size
        img = img.resize(
            (
                int(scaleFactor * width),
                int(scaleFactor * height * (charWidth / charHeight)),
            ), Image.Resampling.NEAREST,
        )

        width, height = img.size
        pix = img.load()
        finalImage = Image.new('RGB', (charWidth * width, charHeight * height), color=(0, 0, 0))
        draw = ImageDraw.Draw(finalImage)
        p_width, p_height = finalImage.size

        print(p_width, p_height)

        for i in range(height):
            for j in range(width):
                r, g, b = pix[j, i]
                h = int(r / 3 + g / 3 + b / 3)
                pix[j, i] = (h, h, h)
                text_file.write(getChar(h))
                draw.text((j * charWidth, i * charHeight), getChar(h), font=font, fill=(r, g, b))

            text_file.write('\n')

        # img.save("output.png")
        finalImage.save('output.png')

        self.a_pixmap = QPixmap('output.png')

        self.photo.setPixmap(self.a_pixmap)


if __name__ == "__main__":
    app = QApplication([])
    GUI_window = Gui()
    GUI_window.show()
    sys.exit(app.exec())
