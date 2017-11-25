import cognitive_face as CF

from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QDesktopWidget, QFileDialog, QLabel,  QHBoxLayout, QVBoxLayout, )
from PyQt5.QtGui import QFont, QPixmap

class Window(QWidget):
    def __init__(self):
        self.first_image = ""
        self.second_image = ""
        self.firstload = True
        super().__init__()
        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')
        loadbutton = QPushButton('GO!', self)
        loadbutton.setToolTip('This is a <b>QPushButton</b> widget')
        loadbutton.resize(loadbutton.sizeHint())
        loadbutton.clicked.connect(lambda: self.load(loadbutton))

        imgonebut = QPushButton('Load first image!', self)
        imgonebut.setToolTip('This is a <b>QPushButton</b> widget')
        imgonebut.resize(loadbutton.sizeHint())
        imgonebut.move(100, 100)
        imgonebut.clicked.connect(lambda: self.openImageFile1(imgonebut))


        imgtwobut = QPushButton('Load second image!', self)
        imgtwobut.setToolTip('This is a <b>QPushButton</b> widget')
        imgtwobut.resize(loadbutton.sizeHint())
        imgtwobut.move(200, 200)
        imgtwobut.clicked.connect(lambda: self.openImageFile2(imgtwobut))


        image1 = QLabel(self)
        image2 = QLabel(self)
        blank = QPixmap("heman.jpg")
        image1.setPixmap(blank)
        image2.setPixmap(blank)



        hboxBottom = QHBoxLayout()
        hboxBottom.addStretch(1)
        hboxBottom.addWidget(loadbutton)
        hboxBottom.addWidget(imgtwobut)
        hboxBottom.addWidget(imgonebut)

        hboxImages = QHBoxLayout()
        hboxImages.addStretch(1)
        hboxImages.addWidget(image1)
        hboxImages.addWidget(image2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hboxImages)

        vbox.addLayout(hboxBottom)

        self.setLayout(vbox)


        self.setGeometry(500, 500, 1000, 800)
        self.setWindowTitle('Who Would Win?!')
        self.setWindowIcon(QIcon('web.png'))
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def load(self, loadbutton):
        if self.first_image == "" or self.second_image == "":
            print("Images not loaded!")
        else:
            run(self.first_image, self.second_image)

    def openImageFile2(self, button):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image 2", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.second_image = fileName
            pixmap = QPixmap(self.second_image)

            print(self)

    def openImageFile1(self, button):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image 1", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.first_image = fileName
            pixmap = QPixmap(self.first_image)
            print(self)


def run(image1, image2):
    """
    Takes in two image urls
    :param image1:
    :param image2:
    :return:
    """
    KEY = '8b9d5cf6d62e4b5d9436f59acd5e0ba4'  # Replace with a valid subscription key (keeping the quotes in place).
    CF.Key.set(KEY)

    BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'  # Replace with your regional Base URL
    CF.BaseUrl.set(BASE_URL)

    
    

    print(image1, image2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())