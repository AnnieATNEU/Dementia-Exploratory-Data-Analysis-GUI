from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
# in case of pyside: just replace PyQt5->PySide2

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

class MplWidget(qtw.QWidget):
  
    def __init__(self, parent=None):
        
        super().__init__(parent)

        fig = Figure(figsize=(5, 5))
        self.can = FigureCanvasQTAgg(fig)
        self.toolbar = NavigationToolbar2QT(self.can, self)
        layout = qtw.QVBoxLayout(self)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.can)

        # here you can set up your figure/axis
        self.ax = self.can.figure.add_subplot(111)

    def plot_basic_line(self, X, Y, label):
        # plot a basic line plot from x and y values.
        self.ax.cla() # clears the axis
        self.ax.plot(X, Y, label=label)
        self.ax.grid(True)
        self.ax.legend()
        self.can.figure.tight_layout()
        self.can.draw()

class MyQtApp(qtw.QWidget):
    def __init__(self):
        super(MyQtApp, self).__init__()

        # layout
        self.mpl_can = MplWidget(self)
        self.btn_plot1 = qtw.QPushButton('plot1', self)
        self.btn_plot2 = qtw.QPushButton('plot2', self)
        self.btn_plot3 = qtw.QPushButton('scatter', self)
        self.layout = qtw.QVBoxLayout(self)
        self.layout.addWidget(self.mpl_can)
        self.layout.addWidget(self.btn_plot1)
        self.layout.addWidget(self.btn_plot2)
        self.layout.addWidget(self.btn_plot3)
        self.setLayout(self.layout)

        # connects
        self.btn_plot1.clicked.connect(self.plot1)
        self.btn_plot2.clicked.connect(self.plot2)
        self.btn_plot3.clicked.connect(self.plot_scatter)

    def keyPressEvent(self, event):
        if event.key() == qtc.Qt.Key_1: self.plot1()
        elif event.key() == qtc.Qt.Key_2: self.plot2()
        elif event.key() == qtc.Qt.Key_3: self.plot_scatter()

    def plot1(self):
        X, Y = (1, 2), (1, 2)
        self.mpl_can.plot_basic_line(X, Y, label='plot1')

    def plot2(self):
        X, Y = (10, 20), (10, 20)
        self.mpl_can.plot_basic_line(X, Y, label='plot2')
    
    def plot_scatter(self):
        X, Y = (1, 7, 9, 3, 2), (3, 6, 8, 2, 11)
        self.mpl_can.ax.scatter(X, Y, label='scatter')
        self.mpl_can.ax.legend()
        self.mpl_can.can.draw()


if __name__ == '__main__':
    app = qtw.QApplication([])
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()