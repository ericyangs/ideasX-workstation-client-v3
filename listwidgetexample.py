import sys
from PyQt5 import QtGui, QtWidgets, QtCore
from ideasxdevice import Ui_IdeasXDevice
from mainwindow import Ui_MainWindow


class IdeasXUI(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("./icon/IDEAS.png"))

        self.statusbar.showMessage("Connected to IdeasX")
        IdeasXDevice = QtWidgets.QWidget()
        #ui = Ui_IdeasXDevice()
        #ui.setupUi(IdeasXDevice)
        IdeasXDevice = Ui_IdeasXDevice()
        myCustomWidgetItem = QtWidgets.QListWidgetItem()
        myCustomWidgetItem.setSizeHint(QtCore.QSize(100,40))
        self.listEncoder.addItem(myCustomWidgetItem)
        self.listEncoder.setItemWidget(myCustomWidgetItem, IdeasXDevice)

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