import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow


class MainWindow_EXEC():

    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.update_calendar()
        self.update_progressbar()

        MainWindow.show()
        sys.exit(app.exec_())


# ------------------------------------------------------
    def update_calendar(self):
        self.ui.calendarWidget.selectionChanged.connect(self.update_date)

    def update_date(self):
        self.ui.dateEdit.setDate(self.ui.calendarWidget.selectedDate())


# ------------------------------------------------------
    def update_progressbar(self):
        radio_3 = self.ui.radioButton_3.text()
        self.ui.radioButton_3.setText('Set Progressbar')
        radio_3_upd = self.ui.radioButton_3.text()
        print(radio_3, radio_3_upd)

        self.ui.radioButton_3.clicked.connect(self.set_progressbar)


    def set_progressbar(self):
        progress_value = self.ui.progressBar.value()
        print('progressBar: ', progress_value)

        new_value = self.ui.lcdNumber.value()
        self.ui.progressBar.setValue(new_value)
        print('progressBar: ', self.ui.progressBar.value())

if __name__ == "__main__":
    MainWindow_EXEC()
