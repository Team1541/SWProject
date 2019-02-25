import os
os.environ['DISPLAY'] = 'localhost:0.0'

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QThread
import shutil as sh
from PIL import Image, ImageQt

class GUI(object):
    def __init__(self):
        self.files = 0
        self.files_list = list()
        self.dir = './TEMP'
        self.model = QtGui.QStandardItemModel()
        self.Page = 1
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1300, 650))
        MainWindow.setMaximumSize(QtCore.QSize(1300, 650))
        MainWindow.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setWindowTitle("도면 인식")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1090, 590, 200, 45))
        self.pushButton.setObjectName("pushButton")

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(1090, 45, 200, 494))
        self.listView.setObjectName("listView")

        self.ImageView = QtWidgets.QGraphicsView(self.centralwidget)
        self.ImageView.setGeometry(QtCore.QRect(10, 45, 1056, 594))
        self.ImageView.setObjectName("ImageView")
        self.scene = QtWidgets.QGraphicsScene()
        self.ImageView.setScene(self.scene)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 1058, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(1)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
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
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(1066, 0, 20, 700))
        self.line.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.PageNum = QtWidgets.QLabel(self.centralwidget)
        self.PageNum.setGeometry(QtCore.QRect(530, 600, 20, 20))
        self.PageNum.setAlignment(QtCore.Qt.AlignCenter)
        self.PageNum.setObjectName("PageNum")
        self.Prev = QtWidgets.QPushButton(self.centralwidget)
        self.Prev.setGeometry(QtCore.QRect(510, 600, 20, 20))
        self.Prev.setObjectName("Prev")
        self.Next = QtWidgets.QPushButton(self.centralwidget)
        self.Next.setGeometry(QtCore.QRect(550, 600, 20, 20))
        self.Next.setObjectName("Next")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1090, 543, 200, 45))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton.pressed.connect(self._Btn_Diagram)
        self.pushButton_2.pressed.connect(self._Btn_Select)
        self.Prev.pressed.connect(self._Btn_Prev)
        self.Next.pressed.connect(self._Btn_Next)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "도면 인식"))
        self.label.setText(_translate("MainWindow", "미리 보기"))
        self.label_2.setText(_translate("MainWindow", "도면 목록"))
        self.PageNum.setText(_translate("MainWindow", "-"))
        self.Prev.setText(_translate("MainWindow", "<"))
        self.Next.setText(_translate("MainWindow", ">"))
        self.pushButton_2.setText(_translate("MainWindow", "도면 선택"))

    def _Btn_Diagram(self):
        ##
        ProgressDialog = QtWidgets.QDialog()
        ui = Ui_ProgressDialog()
        ui.setupUi(ProgressDialog, self.files)
        ProgressDialog.exec_()
        ui.th.exit(0)
        # ui = Ui_MainWindow_2()
        # ui.setupUi(self.MainWindow)
        # self.MainWindow.show()

    def _Btn_Select(self):
        Dialog = QtWidgets.QFileDialog
        temp_files = Dialog.getOpenFileNames()
        for val in temp_files[0]:
            file_name = val.split("/")[-2] + "/" + val.split("/")[-1];
            if file_name in self.files_list:
                continue
            if os.path.isdir(self.dir + file_name.split("/")[0]) == False:
                os.mkdir(self.dir + file_name.split("/")[0])
            sh.copy2(val,self.dir + file_name)
            if self.files == 1:
                self._Refresh_image()
            self.files+=1
            self.files_list.append(file_name)
            temp = QtGui.QStandardItem(file_name)
            #temp.setCheckable(True)
            self.model.appendRow(temp)
        self.listView.setModel(self.model)
        #self.listView.clicked.connect(self._clk_listview)

    def _Btn_Prev(self):
        if self.Page == 1:
            return
        self.Page -=1
        self._Refresh_image()

    def _Btn_Next(self):
        if self.Page == self.files:
            return
        self.Page += 1
        self._Refresh_image()

    def _Refresh_image(self):
        self.PageNum.setText(str(self.Page))
        img = Image.open(self.dir + self.files_list[self.Page-1])
        self.ImgQ = ImageQt.ImageQt(img)
        # if Image.is
        #     Dialog = QtWidgets.QDialog()
        #     ui = Ui_Dialog()
        #     ui.setupUi(Dialog, "Not Image")
        #     Dialog.exec_()
        #     return
        self.scene.clear()
        self.scene.addPixmap(QtGui.QPixmap.fromImage(self.ImgQ))
        self.scene.update()
    def init_window(self):
        import sys
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        self.app.exec_()
    def setdir(self, TEMP):
        self.dir  = TEMP + '/TEMP/'

class Ui_MainWindow_2(object):
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
        self.scene = QtWidgets.QGraphicsScene()
        self.ImageView.setScene(self.scene)
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
        self.PageNum.setText(_translate("MainWindow", "1"))
        self.Prev.setText(_translate("MainWindow", "<"))
        self.Next.setText(_translate("MainWindow", ">"))
        self.checkBox.setText(_translate("MainWindow", "인식된 심볼 가림"))
        self.FileName.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "파일 내보내기"))
        self.pushButton.setText(_translate("MainWindow", "전체 내보내기"))
        self.label_2.setText(_translate("MainWindow", " 인식 결과"))

class Ui_ProgressDialog(object):
    def setupUi(self, ProgressDialog,files):
        ProgressDialog.setObjectName("ProgressDialog")
        ProgressDialog.setWindowModality(QtCore.Qt.WindowModal)
        ProgressDialog.setEnabled(True)
        ProgressDialog.resize(400, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgressDialog.sizePolicy().hasHeightForWidth())
        ProgressDialog.setSizePolicy(sizePolicy)
        ProgressDialog.setModal(True)
        self.Dialog = ProgressDialog
        self.progressBar = QtWidgets.QProgressBar(ProgressDialog)
        self.progressBar.setGeometry(QtCore.QRect(60, 90, 300, 40))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(ProgressDialog)
        self.label.setGeometry(QtCore.QRect(0, 50, 400, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.retranslateUi(ProgressDialog)
        self.th = Thread(files)
        self.th.start()
        self.th.Progress_value.connect(self.progressBar.setValue)
        self.progressBar.valueChanged.connect(self.fslot)
        QtCore.QMetaObject.connectSlotsByName(ProgressDialog)

    def retranslateUi(self, ProgressDialog):
        _translate = QtCore.QCoreApplication.translate
        ProgressDialog.setWindowTitle(_translate("ProgressDialog", "Dialog"))
        self.label.setText(_translate("ProgressDialog", "분석 중"))

    @pyqtSlot()
    def fslot(self):
        if self.progressBar.value() == 100:
            self.th.exit(0)
            self.Dialog.done(0)
            True
        False

class Thread(QThread):
    Progress_value = QtCore.pyqtSignal(int)
    def __init__(self, files):
        QThread.__init__(self)
        self.files = files
        self.mutex = QtCore.QMutex()
        self.cnt = 0
        self.cond = QtCore.QWaitCondition()
        self._status = True
    def __del__(self):
        self.wait()

    def run(self):
        while True:
            self.mutex.lock()
            if not self._status:
                self.cond.wait(self.mutex)
            if self.cnt == 100:
                self.mutex.unlock()
                break
            self.cnt += 1
            self.Progress_value.emit(self.cnt)
            self.msleep(10)
            self.mutex.unlock()
    @property
    def status(self):
        return self._status

class Ui_Dialog(object):
    def setupUi(self, Dialog, Msg="Error"):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(300, 150))
        Dialog.setMaximumSize(QtCore.QSize(300, 150))
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(120, 90, 70, 40))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 280, 60))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog, Msg)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog, Msg):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "ERROR"))
        self.label.setText(_translate("Dialog", Msg))
=======
import matplotlib
os.environ['DISPLAY'] = 'localhost:1.0'
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.plot(np.arange(100))
plt.show()

>>>>>>> origin/master
