from PySide6 import QtCore, QtGui, QtWidgets


class CalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent,
                                             verticalHeaderFormat=QtWidgets.QCalendarWidget.NoVerticalHeader,
                                             gridVisible=False)

        for d in (QtCore.Qt.Saturday, QtCore.Qt.Sunday,):
            fmt = self.weekdayTextFormat(d)
            fmt.setForeground(QtCore.Qt.darkGray)
            self.setWeekdayTextFormat(d, fmt)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = CalendarWidget()
    w.show()
    sys.exit(app.exec_())
