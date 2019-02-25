# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog):
        ProgressDialog.setObjectName("ProgressDialog")
        ProgressDialog.resize(400, 200)
        self.progressBar = QtWidgets.QProgressBar(ProgressDialog)
        self.progressBar.setGeometry(QtCore.QRect(60, 90, 300, 40))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(ProgressDialog)
        self.label.setGeometry(QtCore.QRect(0, 50, 400, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(ProgressDialog)
        QtCore.QMetaObject.connectSlotsByName(ProgressDialog)

    def retranslateUi(self, ProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressDialog.setWindowTitle(_translate("ProgressDialog", "Dialog"))
        self.label.setText(_translate("ProgressDialog", "분석 중"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProgressDialog = QtWidgets.QDialog()
    ui = Ui_ProgressDialog()
    ui.setupUi(ProgressDialog)
    ProgressDialog.show()
    sys.exit(app.exec_())

