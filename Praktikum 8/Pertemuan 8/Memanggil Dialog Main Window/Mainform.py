

from PyQt5 import QtCore, QtGui, QtWidgets
from Dialog import Ui_Dialog

class Ui_MainWindow(object):
    def setupUi(self, form):
        MainWindow.setObjectName("form")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(form)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 401, 291))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(30, 260, 351, 17))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 371, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label.setText("")
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(form)

        self.pushButton.clicked.connect(self.button_clicked)

    def button_clicked(self):
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        Dialog.show()
        rsp = Dialog.exec_()

        if rsp == QtWidgets.QDialog.Accepted:
            self.label.setText("Ok Button was Clicked")
        else:
            self.label.setText("Cancel Button was Clicked")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Dialog"))
        self.pushButton.setText(_translate("MainWindow", "Call Dialog"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
