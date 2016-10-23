import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtSql
from mainwindow import Ui_MainWindow

class IdeasXUI(Ui_MainWindow):
    def __init__(self, MainWindow):
        Ui_MainWindow.__init__(self)
        self.setupUi(MainWindow)
        MainWindow.setWindowIcon(QtGui.QIcon("./icon/IDEAS.png"))
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('IdeasX.db')
        self.encoderModel = QtSql.QSqlTableModel()
        delrow = -1 
        self.encoderModel.setTable('encoder')
        self.encoderModel.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
        self.encoderModel.select()
        self.encoderModel.setHeaderData(0, QtCore.Qt.Horizontal, "Module ID")
        self.encoderModel.setHeaderData(1, QtCore.Qt.Horizontal, "Battery Capacity")
        self.encoderModel.setHeaderData(2, QtCore.Qt.Horizontal, "Battery Voltage")
        self.tableEncoder.setModel(self.encoderModel)
        
        self.tableEncoder.resizeColumnsToContents()
        self.statusbar.showMessage("Connected to IdeasX")

if __name__ == '__main__': 
    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = IdeasXUI(main_window)
    main_window.show()
    
    def updateTable():
        print("tick")
        ui.encoderModel.select()
        ui.tableEncoder.resizeColumnsToContents()
    
    displayTimer = QtCore.QTimer()
    displayTimer.timeout.connect(updateTable)
    displayTimer.start(1000)
        
    sys.exit(app.exec_())