# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\fakem\Desktop\Temp\Dialog - untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 260)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 220, 400, 40))
        self.buttonBox.setAutoFillBackground(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.combo_class = QtWidgets.QComboBox(Dialog)
        self.combo_class.setGeometry(QtCore.QRect(80, 70, 300, 30))
        self.combo_class.setObjectName("combo_class")
        self.stackedWidget = QtWidgets.QStackedWidget(Dialog)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 110, 400, 111))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.combo_speicifc = QtWidgets.QComboBox(self.page)
        self.combo_speicifc.setGeometry(QtCore.QRect(80, 45, 300, 30))
        self.combo_speicifc.setObjectName("combo_speicifc")
        self.label_5 = QtWidgets.QLabel(self.page)
        self.label_5.setGeometry(QtCore.QRect(0, 50, 70, 20))
        self.label_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.TextEdit_Class = QtWidgets.QPlainTextEdit(self.page_2)
        self.TextEdit_Class.setGeometry(QtCore.QRect(80, 20, 300, 30))
        self.TextEdit_Class.setObjectName("TextEdit_Class")
        self.TextEdit_Specific = QtWidgets.QPlainTextEdit(self.page_2)
        self.TextEdit_Specific.setGeometry(QtCore.QRect(80, 70, 300, 30))
        self.TextEdit_Specific.setObjectName("TextEdit_Specific")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(10, 25, 70, 20))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(10, 75, 70, 20))
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.stackedWidget.addWidget(self.page_2)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 391, 61))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 70, 20))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        self.stackedWidget.setCurrentIndex(0)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_5.setText(_translate("Dialog", "세부 명칭"))
        self.label_2.setText(_translate("Dialog", "클래스"))
        self.label_3.setText(_translate("Dialog", "세부 명칭"))
        self.label.setText(_translate("Dialog", "추가할 기호의 정보를 입력하시오."))
        self.label_4.setText(_translate("Dialog", "클래스"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

