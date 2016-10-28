import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from mainwindow import Ui_MainWindow
from ideasxdevice import Ui_Form

class IdeasXUI(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("./icon/IDEAS.png"))

        self.statusbar.showMessage("Connected to IdeasX")
        for i in range(0, 100):
            wid = Ui_Form()
            
            wid2 = QtWidgets.QListWidgetItem()
            wid2.setSizeHint(QtCore.QSize(300, 60))
            self.listEncoder.addItem(wid2)
            self.listEncoder.setItemWidget(wid2, wid)


if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = IdeasXUI(main_window)
    main_window.show()
    
    '''
    def updateTable():
        print("tick")
        ui.encoderModel.select()
        ui.tableEncoder.resizeColumnsToContents()
    
    displayTimer = QtCore.QTimer()
    displayTimer.timeout.connect(updateTable)
    displayTimer.start(1000)
    '''    
    sys.exit(app.exec_())