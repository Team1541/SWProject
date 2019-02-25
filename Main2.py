# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 690))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ImageView = QtWidgets.QGraphicsView(self.centralwidget)
        self.ImageView.setGeometry(QtCore.QRect(10, 10, 1056, 594))
        self.ImageView.setObjectName("ImageView")
        self.PageNum = QtWidgets.QLabel(self.centralwidget)
        self.PageNum.setGeometry(QtCore.QRect(530, 565, 20, 20))
        self.PageNum.setAlignment(QtCore.Qt.AlignCenter)
        self.PageNum.setObjectName("PageNum")
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setGeometry(QtCore.QRect(510, 565, 20, 20))
        self.Prev.setObjectName("Prev")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(550, 565, 20, 20))
        self.Next.setObjectName("Next")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1066, 0, 20, 700))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 615, 120, 30))
        font = QtGui.QFont()
        font.setFamily("굴림")
        font.setPointSize(10)
        self.checkBox.setFont(font)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.FileName = QtWidgets.QLabel(self.centralwidget)
        self.FileName.setGeometry(QtCore.QRect(20, 20, 191, 21))
        self.FileName.setFrameShape(QtWidgets.QFrame.Box)
        self.FileName.setTextFormat(QtCore.Qt.AutoText)
        self.FileName.setObjectName("FileName")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(1090, 45, 200, 494))
        self.listView.setObjectName("listView")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1090, 543, 200, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1090, 590, 200, 45))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(1090, 10, 200, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_2.setLineWidth(1)
        self.label_2.setMidLineWidth(1)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.PageNum.setText(_translate("MainWindow", "11"))
        self.Prev.setText(_translate("MainWindow", "<"))
        self.Next.setText(_translate("MainWindow", ">"))
        self.checkBox.setText(_translate("MainWindow", "인식된 심볼 가림"))
        self.FileName.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "도면 선택"))
        self.pushButton.setText(_translate("MainWindow", "도면 인식"))
        self.label_2.setText(_translate("MainWindow", " 인식 결과"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

