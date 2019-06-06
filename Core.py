import PyQt5 as qt
from GUI import Model
import os
os.environ['DISPLAY'] = 'localhost:10.0'

def main():
    import sys
    app = qt.QtWidgets.QApplication(sys.argv)
    MainWindow = Model.MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
    # MainWindow = qt.QtWidgets.QMainWindow()
    # ui = UI.Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())
if __name__ == "__main__":
    main()