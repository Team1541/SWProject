# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def __init__(self):
        import json
        self.current_page = 0
        self.current_sub_page= 0
        self.file_list = []
        with open('Config.json') as file:
            self.Config = json.load(file)
        self.Symbol_list = None
        self.current_listview = None
        self.current_imageview = None
        self.current_size = None
        self.current_name = None
        self.current_type = None
        self._img = "img"
        self.selected_index = 0
        self.classes = None
        self.ratio = 1
        self.Image_Result = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 690)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 10, 1300, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.FirstWindow = QtWidgets.QWidget(self.page)
        self.FirstWindow.setGeometry(QtCore.QRect(320, 10, 960, 600))
        self.FirstWindow.setObjectName("FirstWindow")
        self.F_ImageView = QtWidgets.QGraphicsView(self.FirstWindow)
        self.F_ImageView.setGeometry(QtCore.QRect(0, 30, 960, 540))
        self.F_ImageView.setObjectName("F_ImageView")
        self.textLabel2 = QtWidgets.QLabel(self.FirstWindow)
        self.textLabel2.setGeometry(QtCore.QRect(0, 0, 121, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.textLabel2.setFont(font)
        self.textLabel2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabel2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabel2.setLineWidth(1)
        self.textLabel2.setMidLineWidth(1)
        self.textLabel2.setTextFormat(QtCore.Qt.PlainText)
        self.textLabel2.setScaledContents(False)
        self.textLabel2.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel2.setObjectName("textLabel2")
        self.F_filesize = QtWidgets.QLabel(self.FirstWindow)
        self.F_filesize.setGeometry(QtCore.QRect(750, 571, 210, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.F_filesize.setFont(font)
        self.F_filesize.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.F_filesize.setFrameShadow(QtWidgets.QFrame.Plain)
        self.F_filesize.setLineWidth(1)
        self.F_filesize.setMidLineWidth(1)
        self.F_filesize.setTextFormat(QtCore.Qt.PlainText)
        self.F_filesize.setScaledContents(False)
        self.F_filesize.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.F_filesize.setObjectName("F_filesize")
        self.F_filename = QtWidgets.QLabel(self.FirstWindow)
        self.F_filename.setGeometry(QtCore.QRect(0, 571, 480, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.F_filename.setFont(font)
        self.F_filename.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.F_filename.setFrameShadow(QtWidgets.QFrame.Plain)
        self.F_filename.setLineWidth(1)
        self.F_filename.setMidLineWidth(1)
        self.F_filename.setTextFormat(QtCore.Qt.PlainText)
        self.F_filename.setScaledContents(False)
        self.F_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.F_filename.setObjectName("F_filename")
        self.F_filetype = QtWidgets.QLabel(self.FirstWindow)
        self.F_filetype.setGeometry(QtCore.QRect(490, 571, 240, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.F_filetype.setFont(font)
        self.F_filetype.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.F_filetype.setFrameShadow(QtWidgets.QFrame.Plain)
        self.F_filetype.setLineWidth(1)
        self.F_filetype.setMidLineWidth(1)
        self.F_filetype.setTextFormat(QtCore.Qt.PlainText)
        self.F_filetype.setScaledContents(False)
        self.F_filetype.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.F_filetype.setObjectName("F_filetype")

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath(self.Config['dir_working'])
        # model.setRootPath(QtCore.QDir.homePath())
        self.F_treeview = QtWidgets.QTreeView(self.page)
        self.F_treeview.setGeometry(QtCore.QRect(20, 10, 280, 300))
        self.F_treeview.setObjectName("F_treeview")
        self.F_treeview.setModel(self.model)
        # self.F_treeview.setRootIndex(model.index(QtCore.QDir.homePath()))
        self.F_treeview.setRootIndex(self.model.index(self.Config['dir_working']))

        self.F_listwidget = QtWidgets.QListWidget(self.page)
        self.F_listwidget.setGeometry(QtCore.QRect(20, 330, 280, 250))
        self.F_listwidget.setObjectName("F_listwidget")

        self.textLabel1 = QtWidgets.QLabel(self.page)
        self.textLabel1.setGeometry(QtCore.QRect(20, 310, 280, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.textLabel1.setFont(font)
        self.textLabel1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabel1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabel1.setLineWidth(1)
        self.textLabel1.setMidLineWidth(1)
        self.textLabel1.setTextFormat(QtCore.Qt.PlainText)
        self.textLabel1.setScaledContents(False)
        self.textLabel1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel1.setObjectName("textLabel1")
        self.pushButton = QtWidgets.QPushButton(self.page)
        self.pushButton.setGeometry(QtCore.QRect(20, 580, 280, 40))
        self.pushButton.setObjectName("pushButton")

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.textLabel4 = QtWidgets.QLabel(self.page_2)
        self.textLabel4.setGeometry(QtCore.QRect(20, 10, 280, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.textLabel4.setFont(font)
        self.textLabel4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabel4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabel4.setLineWidth(1)
        self.textLabel4.setMidLineWidth(1)
        self.textLabel4.setTextFormat(QtCore.Qt.PlainText)
        self.textLabel4.setScaledContents(False)
        self.textLabel4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.textLabel4.setObjectName("textLabel4")
        self.S_listwidget = QtWidgets.QListWidget(self.page_2)
        self.S_listwidget.setGeometry(QtCore.QRect(20, 40, 280, 500))
        self.S_listwidget.setObjectName("S_listwidget")

        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.page_2)
        self.stackedWidget_2.setGeometry(QtCore.QRect(320, 10, 960, 600))
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.sub_page_1 = QtWidgets.QWidget()
        self.sub_page_1.setObjectName("sub_page_1")
        self.S1_filename = QtWidgets.QLabel(self.sub_page_1)
        self.S1_filename.setGeometry(QtCore.QRect(180, 570, 300, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.S1_filename.setFont(font)
        self.S1_filename.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S1_filename.setFrameShadow(QtWidgets.QFrame.Plain)
        self.S1_filename.setLineWidth(1)
        self.S1_filename.setMidLineWidth(1)
        self.S1_filename.setTextFormat(QtCore.Qt.PlainText)
        self.S1_filename.setScaledContents(False)
        self.S1_filename.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.S1_filename.setObjectName("S1_filename")
        self.S1_filetype = QtWidgets.QLabel(self.sub_page_1)
        self.S1_filetype.setGeometry(QtCore.QRect(490, 570, 240, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.S1_filetype.setFont(font)
        self.S1_filetype.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S1_filetype.setFrameShadow(QtWidgets.QFrame.Plain)
        self.S1_filetype.setLineWidth(1)
        self.S1_filetype.setMidLineWidth(1)
        self.S1_filetype.setTextFormat(QtCore.Qt.PlainText)

        self.S1_filetype.setScaledContents(False)
        self.S1_filetype.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.S1_filetype.setObjectName("S1_filetype")
        self.S1_checkbox = QtWidgets.QCheckBox(self.sub_page_1)
        self.S1_checkbox.setGeometry(QtCore.QRect(0, 570, 178, 28))
        self.S1_checkbox.setObjectName("S1_checkbox")

        self.textLabel3_3 = QtWidgets.QLabel(self.sub_page_1)
        self.textLabel3_3.setGeometry(QtCore.QRect(0, 0, 121, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.textLabel3_3.setFont(font)
        self.textLabel3_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textLabel3_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textLabel3_3.setLineWidth(1)
        self.textLabel3_3.setMidLineWidth(1)
        self.textLabel3_3.setTextFormat(QtCore.Qt.PlainText)
        self.textLabel3_3.setScaledContents(False)
        self.textLabel3_3.setAlignment(QtCore.Qt.AlignCenter)
        self.textLabel3_3.setObjectName("textLabel3_3")
        self.S1_ImageView = QtWidgets.QGraphicsView(self.sub_page_1)
        self.S1_ImageView.setGeometry(QtCore.QRect(0, 30, 960, 540))
        self.S1_ImageView.setAutoFillBackground(False)
        self.S1_ImageView.setObjectName("S1_ImageView")
        self.S1_filesize = QtWidgets.QLabel(self.sub_page_1)
        self.S1_filesize.setGeometry(QtCore.QRect(750, 570, 210, 28))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.S1_filesize.setFont(font)
        self.S1_filesize.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.S1_filesize.setFrameShadow(QtWidgets.QFrame.Plain)
        self.S1_filesize.setLineWidth(1)
        self.S1_filesize.setMidLineWidth(1)
        self.S1_filesize.setTextFormat(QtCore.Qt.PlainText)
        self.S1_filesize.setScaledContents(False)
        self.S1_filesize.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.S1_filesize.setObjectName("S1_filesize")
        self.stackedWidget_2.addWidget(self.sub_page_1)
        self.sub_page_2 = QtWidgets.QWidget()
        self.sub_page_2.setObjectName("sub_page_2")
        self.S2_tableWidget = QtWidgets.QTableWidget(self.sub_page_2)
        self.S2_tableWidget.setGeometry(QtCore.QRect(0, 30, 960, 540))
        self.S2_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.S2_tableWidget.setShowGrid(True)
        self.S2_tableWidget.setColumnCount(4)
        self.S2_tableWidget.setObjectName("S2_tableWidget")
        self.S2_tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(140, 140, 140))
        self.S2_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(140, 140, 140))
        self.S2_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(140, 140, 140))
        self.S2_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setBackground(QtGui.QColor(140, 140, 140))
        self.S2_tableWidget.setHorizontalHeaderItem(3, item)
        self.S2_tableWidget.horizontalHeader().setVisible(True)
        self.S2_tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.S2_tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.S2_tableWidget.horizontalHeader().setStretchLastSection(False)
        self.stackedWidget_2.addWidget(self.sub_page_2)
        self.page_2_output = QtWidgets.QPushButton(self.page_2)
        self.page_2_output.setGeometry(QtCore.QRect(20, 560, 130, 40))
        self.page_2_output.setObjectName("page_2_output")
        self.page_2_change = QtWidgets.QPushButton(self.page_2)
        self.page_2_change.setGeometry(QtCore.QRect(170, 560, 130, 40))
        self.page_2_change.setObjectName("page_2_change")

        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1300, 21))
        self.menubar.setObjectName("menubar")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave_Directory = QtWidgets.QAction(MainWindow)
        self.actionSave_Directory.setObjectName("actionSave_Directory")
        self.actionChange_Directory = QtWidgets.QAction(MainWindow)
        self.actionChange_Directory.setObjectName("actionChange_Directory")
        self.menuSettings.addAction(self.actionSave_Directory)
        self.menuSettings.addAction(self.actionChange_Directory)
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(self.current_page)
        self.stackedWidget_2.setCurrentIndex(self.current_sub_page)
        self.current_listview = self.F_listwidget
        self.current_imageview = self.F_ImageView
        self.current_name = self.F_filename
        self.current_size = self.F_filesize
        self.current_type = self.F_filetype

        #self.S1_ImageView.dragEnterEvent()
        self.F_treeview.clicked.connect(self.select_file)
        self.F_listwidget.clicked.connect(self.select_list_file_index)
        self.pushButton.clicked.connect(self.btn_recog_clicked)
        self.S_listwidget.clicked.connect(self.select_list_file_index)
        self.S1_checkbox.stateChanged.connect(self.checkboxState)
        self.page_2_change.clicked.connect(self.btn_change_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textLabel2.setText(_translate("MainWindow", "Preview"))
        self.F_filesize.setText(_translate("MainWindow", "Preview"))
        self.F_filename.setText(_translate("MainWindow", "filename"))
        self.F_filetype.setText(_translate("MainWindow", "Preview"))
        self.textLabel1.setText(_translate("MainWindow", "File list"))
        self.pushButton.setText(_translate("MainWindow", "도면 인식"))
        self.textLabel4.setText(_translate("MainWindow", "File list"))
        self.S1_filename.setText(_translate("MainWindow", "filename"))
        self.S1_filetype.setText(_translate("MainWindow", "filetype"))
        self.S1_checkbox.setText(_translate("MainWindow", "Hide Detected Symbols"))
        self.textLabel3_3.setText(_translate("MainWindow", "Preview"))
        self.S1_filesize.setText(_translate("MainWindow", "filesize"))
        item = self.S2_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Image"))
        item = self.S2_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Class"))
        item = self.S2_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Specific"))
        item = self.S2_tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Remarks"))

        self.S2_tableWidget.setColumnWidth(0, 50)
        self.S2_tableWidget.setColumnWidth(1, 150)
        self.S2_tableWidget.setColumnWidth(2, 200)
        self.S2_tableWidget.setColumnWidth(3, 550)
        self.page_2_output.setText(_translate("MainWindow", "Extract"))
        self.page_2_change.setText(_translate("MainWindow", "Change View"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.actionSave_Directory.setText(_translate("MainWindow", "Save Directory"))
        self.actionChange_Directory.setText(_translate("MainWindow", "Change Directory"))


    def set_config(self):
        import os
        path = self.Config['dir_save']
        try:
            if not (os.path.isdir(path)):
                os.makedirs(os.path.join(path))
        except OSError as e:
            if e.errno != e.errno.EEXIST:
                print("Failed to create directory!!!!!")
                raise

    def select_file(self, index):
        from PIL import Image
        temp = {}
        info = self.model.fileInfo(index)
        temp['name'] = info.fileName()
        if not temp['name'].lower().endswith(('.jpg', '.jpeg')):
            self.error_dialog("ONLY JPG FILE")
            return
        temp['path'] = info.filePath()
        img = Image.open(temp['path'])
        temp['img'] = img
        temp['size'] = str(img.size[0]) + "x" + str(img.size[1])
        if self.list_check(self.file_list,name=temp['name']) == 0:
            self.file_list.append(temp)
            item = QtWidgets.QListWidgetItem(temp['name'])
            self.F_listwidget.addItem(item)
            self.F_listwidget.repaint()
        self.set_image_view(len(self.file_list)-1)

    def list_check(self, list, name):
        for item in list:
            if name == item['name']:
                return 1
        return 0


    def select_list_file_index(self,index):
        self.selected_index = index.row()

        if self.current_page == 0: #Image View
            self.set_image_view(self.selected_index)
        else:
            if self.current_sub_page == 0:
                self.set_image_view(self.selected_index)
            else:
                self.set_table_view(self.selected_index)

    def set_image_view(self, index):
        from PIL import ImageQt
        file = self.file_list[index]
        self.current_name.setText(file['name'])
        self.current_size.setText(file['size'])
        self.current_type.setText(file['path'])
        scene = self.current_imageview.scene()
        scene.clear()
        img = file['img']
        imgQ = ImageQt.ImageQt(img)
        imgQ = imgQ.scaled(950, 530, QtCore.Qt.KeepAspectRatio)
        item = QtWidgets.QGraphicsPixmapItem(QtGui.QPixmap.fromImage(imgQ))
        item.setZValue(-1)
        scene.addItem(item)
        scene.update()
        if self.current_page == 1:
            Color = [QtCore.Qt.red, QtCore.Qt.blue, QtCore.Qt.green]
            symbols = self.Symbol_list[index]
            for symbol in symbols:
                coord = symbol['coord']
                self.ratio = imgQ.size().width() / img.size[0]
                ratio = self.ratio
                coord = QtCore.QRectF(coord[0]*ratio,coord[1]*ratio,(coord[2]-coord[0])*ratio,(coord[3]-coord[1])*ratio)
                rect_item = GraphicsItem(coord)
                rect_item.setPen(Color[symbol['type']])
                rect_item.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
                rect_item.setZValue(0)
                scene.addItem(rect_item)
        scene.update()
        #self.current_imageview.viewport().update()


    def set_table_view(self,index):
        from operator import itemgetter
        from copy import deepcopy
        self.S2_tableWidget.clearContents()

        def item_make(string, flag):
            _item = QtWidgets.QTableWidgetItem(string)
            if flag is True:
                _item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled)
            else:
                _item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            return _item
        from PIL import ImageQt
        table = self.S2_tableWidget
        file = self.file_list[index]
        symbols = self.Symbol_list[index]
        img = file['img']
        Remarks = file['path']
        cnt = 0
        table.setRowCount(0)

        temp_list = deepcopy(symbols)
        temp_list = sorted(temp_list, key=lambda k : "".join(k['detail']),reverse=True)

        for item in temp_list:
            table.insertRow(cnt)
            table.setRowHeight(cnt, 50)
            type = self.classes[item['type']]
            if item['detail'] is not None:
                detail = "".join(item['detail'])
            else:
                detail = "None"
            croped_img = img.crop(item['coord'])
            imgQ = ImageQt.ImageQt(croped_img)
            imgQ = imgQ.scaled(50, 50, QtCore.Qt.KeepAspectRatio)
            image = QtWidgets.QLabel()
            image.setPixmap(QtGui.QPixmap.fromImage(imgQ))
            table.setCellWidget(cnt, 0, image)
            table.setItem(cnt, 1, item_make(type, False))
            table.setItem(cnt, 2, item_make(detail, True))
            table.setItem(cnt, 3, item_make(Remarks, False))
            cnt += 1

        #self.S2_tableWidget.cellChanged.connect(select_table)


    def btn_change_clicked(self):
        if self.current_sub_page == 1:
            self.set_image_view(self.selected_index)
            self.current_sub_page = 0
        else:
            self.set_table_view(self.selected_index)
            self.current_sub_page = 1
        self.stackedWidget_2.setCurrentIndex(self.current_sub_page)


    def btn_recog_clicked(self):
        if len(self.file_list) == 0:
            self.error_dialog("SELECT FILE")
            return
        self.get_symbol(self.file_list)
        for i in self.file_list:
            item = QtWidgets.QListWidgetItem(i['name'])
            self.S_listwidget.addItem(item)
        self.S_listwidget.repaint()
        self.current_imageview = self.S1_ImageView
        self.current_listview = self.S_listwidget
        self.current_page = 1
        self.current_name = self.S1_filename
        self.current_type = self.S1_filetype
        self.current_size = self.S1_filesize
        self.set_image_view(0)
        self.stackedWidget.setCurrentIndex(1)



    def get_symbol(self, file_list):
        import DLModule
        temp_list = []
        for item in file_list:
            temp_list.append(item['path'])
        self.Symbol_list, self.classes = DLModule.main(temp_list)


    def checkboxState(self):
        for item in self.current_imageview.scene().items():
            if type(item) is GraphicsItem:
                if self.S1_checkbox.isChecked() == True:
                    item.fill()
                elif  item.old_Pen is None:
                    self.S1_checkbox.setChecked(False)
                    return
                else:
                    item.change()






    def error_dialog(self, msg=None):
        dialog = QtWidgets.QMessageBox()
        dialog.setIcon(QtWidgets.QMessageBox.Warning)
        dialog.setText(msg)
        dialog.setWindowTitle("ERROR")
        retval = dialog.exec_()

    def set_config(self):
        import os
        path = self.Config['dir_save']
        try:
            if not (os.path.isdir(path)):
                os.makedirs(os.path.join(path))
        except OSError as e:
            if e.errno != e.errno.EEXIST:
                print("Failed to create directory!!!!!")
                raise

class GraphicsItem(QtWidgets.QGraphicsRectItem):
    def __init__(self, parent=None):
        QtWidgets.QGraphicsRectItem.__init__(self,parent)
        self.old_Brush = None
        self.old_Pen = None

    def fill(self):
        self.old_Blush = self.brush()
        self.old_Pen = self.pen()
        self.setBrush(QtCore.Qt.white)
        self.setPen(QtCore.Qt.white)

    def change(self):
        self.setBrush(self.old_Blush)
        self.setPen(self.old_Pen)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

