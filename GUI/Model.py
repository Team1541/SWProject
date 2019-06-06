
#from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from GUI.insert_dialog import Ui_Dialog
from GUI import UI
class MainWindow(QMainWindow, UI.Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)
        QShortcut(QKeySequence("Ctrl+A"), self).activated.connect(self.Add_symbol)

        self.dclass = None
        self.dspec = None
        scene = GraphicsScene()
        self.F_ImageView.setScene(scene)
    #setMouseTracing
        scene = GraphicsScene()
        scene.Box_end.connect(self.Read_symbol)
        self.S1_ImageView.setScene(scene)
        self.page_2_output.clicked.connect(self.btn_extract)

        # self.model = QtWidgets.QFileSystemModel()
        # self.model.setRootPath(self.Config['dir_working'])
        # self.F_treeview.setModel(self.model)
        # self.F_treeview.setRootIndex(self.model.index(self.Config['dir_working']))
        #
        # #Table Set
        # item = QtWidgets.QTableWidgetItem()
        # item.setTextAlignment(QtCore.Qt.AlignCenter)
        # font = QtGui.QFont()
        # font.setBold(True)
        # font.setWeight(75)
        # item.setFont(font)
        # item.setBackground(QtGui.QColor(140, 140, 140))
        # self.S2_tableWidget.setHorizontalHeaderItem(3, item)
        #
        # #
        # self.current_listview = self.F_listwidget
        # self.current_imageview = self.F_ImageView
        # self.current_name = self.F_filename
        # self.current_size = self.F_filesize
        # self.current_path = self.F_filetype
        #
        # self.F_treeview.clicked.connect(self.select_file)
        # self.F_listwidget.clicked.connect(self.select_list_file_index)
        # self.pushButton.clicked.connect(self.btn_recog_clicked)
        # self.S_listwidget.clicked.connect(self.select_list_file_index)
        # self.S1_checkbox.stateChanged.connect(self.checkboxState)
        # self.page_2_change.clicked.connect(self.btn_change_clicked)
    def btn_extract(self):
        import openpyxl as xl
        Workbook = xl.Workbook()
        file_name = "Result_Quantity.xlsx"
        sheet1 = Workbook.active
        sheet1.title = "Result"
        Workbook.save(file_name)


    def Read_symbol(self):
        import copy
        start, end = self.current_imageview.scene().getData()
        Symbol = self.Symbol_list[self.selected_index]
        lenS = len(Symbol) -1
        temp = copy.deepcopy(Symbol[lenS])
        temp['type']= self.dclass
        temp['detail']=self.dspec

        coord = [start.x()/self.ratio, start.y()/self.ratio, end.x()/self.ratio, end.y()/self.ratio]
        temp['coord']=copy.deepcopy(coord)
        self.Symbol_list[self.selected_index].append(temp)
        self.set_image_view(self.selected_index)
    def Add_symbol(self):
        if self.current_page == 1 and self.current_sub_page == 0:
            dlg = insert_diagram(classes=self.classes)
            dlg.setWindowModality(Qt.ApplicationModal)
            if dlg.exec_():
                self.dclass, self.dspec = dlg.getData()
                scene = self.current_imageview.scene().setDragable()



class RectItem(QGraphicsRectItem):
    def paint(self, painter, option, widget=None):
        super(RectItem, self).paint(painter, option, widget)
        painter.save()
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(Qt.red)
        painter.drawEllipse(option.rect)
        painter.restore()

class GraphicsScene(QGraphicsScene):
    Box_end = pyqtSignal()
    def __init__(self, parent=None):
        QGraphicsScene.__init__(self, parent)
        self._start = QPointF()
        self._current_rect_item = None
        self.TF = False
        self._start = None
        self._end = None

    def getData(self):
        return self._start, self._end

    def setDragable(self):
        self.TF = True

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton and self.TF:
            self._start = event.scenePos()
            self._current_rect_item = QGraphicsRectItem()
            self._current_rect_item.setPen(Qt.red)
            self.addItem(self._current_rect_item)
            self._start = event.scenePos()
            r = QRectF(self._start, self._start)
            self._current_rect_item.setRect(r)
        super(GraphicsScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._current_rect_item is not None and self.TF:
            r = QRectF(self._start, event.scenePos()).normalized()
            self._current_rect_item.setRect(r)
        super(GraphicsScene, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self._current_rect_item is not None and self.TF:
            self._end = event.scenePos()
            self.removeItem(self._current_rect_item)
            self._current_rect_item = None
            self.TF = False
            self.Box_end.emit()
        super(GraphicsScene, self).mouseReleaseEvent(event)


    # def mousePressEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         print(event.scenePos())
    # def mouseReleaseEvent(self, event):
    #     if event.button() == Qt.LeftButton:
    #         print(event.scenePos())

class insert_diagram(QDialog):
    def __init__(self, parent=None, classes=None):
        super(insert_diagram, self).__init__(parent)
        self.UI = Ui_Dialog()
        self.UI.setupUi(self)
        self.D_class = None
        self.D_spec = None
        self.UI.buttonBox.rejected.connect(self.reject)
        self.UI.buttonBox.accepted.connect(self.accept)
        for key,value in classes.items():
            self.UI.combo_class.addItem(value.rstrip())
        self.UI.combo_class.addItem("None")
        self._setComboItem(0)
        self.UI.combo_class.currentIndexChanged.connect(self._setComboItem)

    def getData(self):
        if self.D_class == 5:
            return self.UI.TextEdit_Class.toPlainText(), self.UI.TextEdit_Specific.toPlainText()
        return self.D_class, str(self.UI.combo_speicifc.currentText())

    def _setComboItem(self, index):
        self.D_class = index
        combo = self.UI.combo_speicifc
        if index == 5: #None
            self.UI.stackedWidget.setCurrentIndex(1)
            return
        ###HARD CODING
        if index == 0: #Valve
            combo.clear()
            combo.addItems(["GATE", "BALL","GLOBE", "NEEDLE", "PLUG", "NORMAL", "CHECK", "None"])
        elif index == 1: #Instument
            combo.clear()
            combo.addItems(["Instrument"])
        else:
            combo.clear()
            combo.addItems(["None"])


