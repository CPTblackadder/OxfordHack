from PyQt5.QtGui import QIcon
import sys
from PyQt5.QtWidgets import (QWidget, QToolTip,
    QPushButton, QApplication, QDesktopWidget, QFileDialog, QLabel,  QHBoxLayout, QVBoxLayout, )
from PyQt5.QtGui import QFont, QPixmap

import fight


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

        self.infotext = QLabel(self)
        self.infotext.setText("Choose images to fight!")


        self.image1 = QLabel(self)
        self.image2 = QLabel(self)
        blnk = QPixmap("blank1.jpg")
        self.image1.setPixmap(blnk)
        self.image2.setPixmap(blnk)


        hboxTop = QHBoxLayout()
        hboxTop.addStretch(1)
        hboxTop.addWidget(self.infotext)


        hboxBottom = QHBoxLayout()
        hboxBottom.addStretch(1)
        hboxBottom.addWidget(loadbutton)
        hboxBottom.addWidget(imgtwobut)
        hboxBottom.addWidget(imgonebut)

        hboxImages = QHBoxLayout()
        hboxImages.addStretch(1)
        hboxImages.addWidget(self.image1)
        hboxImages.addWidget(self.image2)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hboxTop)
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
            self.setWinner(fight.main(self.first_image, self.second_image))


    def openImageFile2(self, button):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image 2", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.second_image = fileName
            self.image2.setPixmap(QPixmap(self.second_image))

    def openImageFile1(self, button):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image 1", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            self.first_image = fileName
            self.image1.setPixmap(QPixmap(self.first_image))

    def setWinner(self, winner):
        if winner == fight.IMAGE1:
            self.infotext.setText("First Image won!")
        else:
            self.infotext.setText("Second Image won!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.exit(app.exec_())