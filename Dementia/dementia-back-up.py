# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dementia.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os,sip
import pandas as pd
import matplotlib as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import  FigureCanvasQTAgg , NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
from matplotlib.figure import Figure 
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
import time
import seaborn as sns
import matplotlib, random
matplotlib.use('Qt5Agg')





class MatplotlibCanvas(FigureCanvasQTAgg):
    def __init__(self,parent=None, dpi = 120):
        fig = Figure(dpi = dpi)
        self.axes = fig.add_subplot(111)
        super(MatplotlibCanvas,self).__init__(fig)
        fig.tight_layout()

class PandasModel(QtCore.QAbstractTableModel): 
    def __init__(self, df = pd.DataFrame(), parent=None): 
        QtCore.QAbstractTableModel.__init__(self, parent=parent)
        self._df = df.copy()

    def toDataFrame(self):
        return self._df.copy()

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if orientation == QtCore.Qt.Horizontal:
            try:
                return self._df.columns.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()
        elif orientation == QtCore.Qt.Vertical:
            try:
                # return self.df.index.tolist()
                return self._df.index.tolist()[section]
            except (IndexError, ):
                return QtCore.QVariant()

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role != QtCore.Qt.DisplayRole:
            return QtCore.QVariant()

        if not index.isValid():
            return QtCore.QVariant()

        return QtCore.QVariant(str(self._df.iloc[index.row(), index.column()]))

    def setData(self, index, value, role):
        row = self._df.index[index.row()]
        col = self._df.columns[index.column()]
        if hasattr(value, 'toPyObject'):
            # PyQt4 gets a QVariant
            value = value.toPyObject()
        else:
            # PySide gets an unicode
            dtype = self._df[col].dtype
            if dtype != object:
                value = None if value == '' else dtype.type(value)
        self._df.set_value(row, col, value)
        return True

    def rowCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.index)

    def columnCount(self, parent=QtCore.QModelIndex()): 
        return len(self._df.columns)

    def sort(self, column, order):
        colname = self._df.columns.tolist()[column]
        self.layoutAboutToBeChanged.emit()
        self._df.sort_values(colname, ascending= order == QtCore.Qt.AscendingOrder, inplace=True)
        self._df.reset_index(inplace=True, drop=True)
        self.layoutChanged.emit()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1856, 970)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("emojiIcons/gene.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Greenframebehind = QtWidgets.QFrame(self.centralwidget)
        self.Greenframebehind.setGeometry(QtCore.QRect(10, 4, 1841, 941))
        self.Greenframebehind.setStyleSheet("background-color: rgb(16, 79, 127);")
        self.Greenframebehind.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Greenframebehind.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Greenframebehind.setObjectName("Greenframebehind")
        self.frameBehindplotWidget = QtWidgets.QFrame(self.Greenframebehind)
        self.frameBehindplotWidget.setGeometry(QtCore.QRect(9, 3, 1822, 911))
        self.frameBehindplotWidget.setStyleSheet("\n"
"background-color: rgb(199, 240, 248);")
        self.frameBehindplotWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBehindplotWidget.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBehindplotWidget.setObjectName("frameBehindplotWidget")

        self.frameBehindplotWidget2 = QtWidgets.QFrame(self.frameBehindplotWidget)
        self.frameBehindplotWidget2.setGeometry(QtCore.QRect(200, 180, 1611, 521))
        self.frameBehindplotWidget2.setStyleSheet("QFrame#frameBehindplotWidget2{border-radius: 6px;\n"
"    background-color: rgb(16, 79, 127);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QFrame:hover#frameBehindplotWidget2\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.frameBehindplotWidget2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameBehindplotWidget2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameBehindplotWidget2.setObjectName("frameBehindplotWidget2")

        self.TitleLabel = QtWidgets.QLabel(self.frameBehindplotWidget)
        self.TitleLabel.setGeometry(QtCore.QRect(850, 20, 391, 41))
        self.TitleLabel.setStyleSheet("\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 115, 173);\n"
"border radius: 12px;")
        self.TitleLabel.setObjectName("TitleLabel")

        self.plotWidget = QtWidgets.QWidget(self.frameBehindplotWidget2)
        self.plotWidget.setGeometry(QtCore.QRect(10, 10, 1591, 501))
        self.plotWidget.setStyleSheet("\n"
"\n"
"QWidget#plotWidget{border-radius: 6px;\n"
"    background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QWidget:hover#plotWidget\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.plotWidget.setObjectName("plotWidget")
        self.tableView = QtWidgets.QTableView(self.frameBehindplotWidget2)
        self.tableView.setGeometry(QtCore.QRect(10, 10, 1591, 501))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setObjectName("tableView")
     
        self.behindTitleLabel1_2 = QtWidgets.QLabel(self.frameBehindplotWidget)
        self.behindTitleLabel1_2.setGeometry(QtCore.QRect(830, 10, 421, 61))
        self.behindTitleLabel1_2.setStyleSheet("\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(16, 79, 127);\n"
"border radius: 12px;")
        self.behindTitleLabel1_2.setText("")
        self.behindTitleLabel1_2.setObjectName("behindTitleLabel1_2")
        self.uploadcsvButton = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.uploadcsvButton.setGeometry(QtCore.QRect(10, 40, 171, 41))
        self.uploadcsvButton.setStyleSheet("\n"
"\n"
"QPushButton#uploadcsvButton{border-radius: 12px;\n"
"    background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#uploadcsvButton\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagesicons/addIcon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uploadcsvButton.setIcon(icon)
        self.uploadcsvButton.setObjectName("uploadcsvButton")
      
        self.NumberofPatients = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.NumberofPatients.setGeometry(QtCore.QRect(200, 80, 181, 31))
        self.NumberofPatients.setStyleSheet("\n"
"\n"
"QPushButton#NumberofPatients{border-radius: 12px;\n"
"    background-color: rgb(155, 232, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#NumberofPatients\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.NumberofPatients.setObjectName("NumberofPatients")
        self.correlationMatrixbutton = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.correlationMatrixbutton.setGeometry(QtCore.QRect(390, 80, 181, 31))
        self.correlationMatrixbutton.setStyleSheet("\n"
"\n"
"QPushButton#correlationMatrixbutton{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#correlationMatrixbutton\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.correlationMatrixbutton.setObjectName("correlationMatrixbutton")

        self.tableviewButton = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.tableviewButton.setGeometry(QtCore.QRect(400, 120, 181, 31))
        self.tableviewButton.setStyleSheet("\n"
"\n"
"QPushButton#tableviewButton{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#tableviewButton\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.tableviewButton.setObjectName("tableviewButton")
        self.viewAgeplot = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.viewAgeplot.setGeometry(QtCore.QRect(580, 80, 191, 31))
        self.viewAgeplot.setStyleSheet("\n"
"\n"
"QPushButton#viewAgeplot{border-radius: 12px;\n"
"    background-color: rgb(62, 197, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#viewAgeplot\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.viewAgeplot.setObjectName("viewAgeplot")
        self.plotMMSE = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.plotMMSE.setGeometry(QtCore.QRect(990, 80, 171, 31))
        self.plotMMSE.setStyleSheet("\n"
"\n"
"QPushButton#plotMMSE{border-radius: 12px;\n"
"    font: 700 9pt \"Segoe UI\";\n"
"    background-color: rgb(0, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#plotMMSE\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.plotMMSE.setObjectName("plotMMSE")
       
        self.viewGroupPlot = QtWidgets.QComboBox(self.frameBehindplotWidget)
        self.viewGroupPlot.setGeometry(QtCore.QRect(780, 80, 191, 31))
        self.viewGroupPlot.setStyleSheet("\n"
"\n"
"QComboBox#viewGroupPlot{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"    background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#viewGroupPlot\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.viewGroupPlot.setObjectName("viewGroupPlot")
        self.viewGroupPlot.addItem("")

        self.comboBox2 = QtWidgets.QComboBox(self.frameBehindplotWidget)
        self.comboBox2.setGeometry(QtCore.QRect(200, 120, 191, 31))
        self.comboBox2.setStyleSheet("\n"
"\n"
"QComboBox#comboBox2{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"    background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#comboBox2\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.addItem("")

        
        self.behindlabelBottom = QtWidgets.QLabel(self.frameBehindplotWidget)
        self.behindlabelBottom.setGeometry(QtCore.QRect(200, 710, 1611, 191))
        self.behindlabelBottom.setStyleSheet("background-color: rgb(0, 59, 177);\n"
"")
        self.behindlabelBottom.setObjectName("behindlabelBottom")

        self.label = QtWidgets.QLabel(self.frameBehindplotWidget)
        self.label.setGeometry(QtCore.QRect(210, 716, 1591, 180))
        self.label.setStyleSheet("background-color: rgb(222, 241, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.machineLearningcomboBox = QtWidgets.QComboBox(self.frameBehindplotWidget)
        self.machineLearningcomboBox.setGeometry(QtCore.QRect(1180, 80, 311, 31))
        self.machineLearningcomboBox.setStyleSheet("\n"
"\n"
"QComboBox#machineLearningcomboBox{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"    background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"        font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#machineLearningcomboBox\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.machineLearningcomboBox.setObjectName("machineLearningcomboBox")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.comparisonresultButton = QtWidgets.QPushButton(self.frameBehindplotWidget)
        self.comparisonresultButton.setGeometry(QtCore.QRect(830, 140, 431, 31))
        self.comparisonresultButton.setStyleSheet("\n"
"\n"
"QPushButton#comparisonresultButton{border-radius: 12px;\n"
"    \n"
"    border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"    font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#comparisonresultButton\n"
"{\n"
"border-width:2px;\n"
"    border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.comparisonresultButton.setObjectName("comparisonresultButton")
        self.frameBehindplotWidget2.raise_()
        self.behindTitleLabel1_2.raise_()
        self.TitleLabel.raise_()
        self.tableView.raise_()
        self.plotWidget.raise_()
        self.uploadcsvButton.raise_()
        self.NumberofPatients.raise_()
        self.correlationMatrixbutton.raise_()
        self.tableviewButton.raise_()
        self.viewAgeplot.raise_()
        self.plotMMSE.raise_()
        self.viewGroupPlot.raise_()
        self.comboBox2.raise_()
        self.behindlabelBottom.raise_()
        self.label.raise_()
        self.machineLearningcomboBox.raise_()
        self.comparisonresultButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1856, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)  


        self.gridLayout = QtWidgets.QGridLayout(self.plotWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.plotWidget)
        self.label.setObjectName("label")
        
        self.horizontalLayout.addWidget(self.label)
     
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(self.spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.filename = ''
        self.dftoplot = []
        # self.df = []
        self.themes = ['bmh', 'classic', 'dark_background', 'fast', 
        'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-bright',
                'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
                'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook',
                'seaborn-paper', 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk',
                'seaborn-ticks', 'seaborn-white', 'seaborn-whitegrid', 'seaborn',
                'Solarize_Light2', 'tableau-colorblind10']
       
        self.comboBox2.addItems(self.themes)
        self.base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(self.base_name)[0]
#====================================================================================
    def uploadCSV(self):
        self.filename = QtWidgets.QFileDialog.getOpenFileName(filter = "csv (*.csv)")[0]
        print("File :", self.filename)  

        self.tableView.setVisible(True)
        self.tableView.setVisible(False)
        self.file = []
        self.file.append(self.filename)
        self.f = str(self.file[0])
        path =  self.filename
        self.df = pd.read_csv(path)
        self.df=self.df.drop(['Subject ID','MRI ID','Hand'],axis=1)
        self.df['SES'].fillna((self.df['SES'].median()), inplace=True)
        self.df['MMSE'].fillna((self.df['MMSE'].median()), inplace=True)
        self.df['CDR'] = self.df['CDR'].apply(lambda x: self.cat_CDR(x))
        self.df2= self.df
        model = PandasModel(self.df2)
        self.tableView.setModel(model)

        self.viewDataframe()

    def cat_CDR(self,n):
      if n == 0:
        return 'Normal' 
      else:                 # As we have no cases of sever dementia CDR score=3
        return 'Dementia'
#================================================================
    def viewDataframe(self):
        self.tableView.setVisible(True)
        self.plotWidget.setVisible(False)

        path =  self.f
        self.df = pd.read_csv(path)
        self.df=self.df.drop(['Subject ID','MRI ID','Hand'],axis=1)
        self.df['SES'].fillna((self.df['SES'].median()), inplace=True)
        self.df['MMSE'].fillna((self.df['MMSE'].median()), inplace=True)
        self.df['CDR'] = self.df['CDR'].apply(lambda x: self.cat_CDR(x))
        self.df2= self.df
        model = PandasModel(self.df2)
        self.tableView.setModel(model)

      
#=============================================================
    def numOfpatient(self):
        self.readData()
     
        self.tableView.setVisible(False)
        self.plotWidget.setVisible(True)
        
      

       # count plot on single categorical variable
     
        # print(sns.countplot(x ='Group', data = self.df2))
 
        self.canv.axes.cla()  #clear the current axes
        self.ax = self.canv.axes

        # fig, self.ax = plt.subplots(figsize=(5,4), dpi=200)
        # self.ax.plot(self.paTientNum)

        self.df.plot(ax = self.canv.axes)
        
        
        self.ax.set(xlabel= "Group",ylabel ='Number of patients',title='Group')

        # self.base_name = os.path.basename(self.filename)
        # self.Title = os.path.splitext(self.base_name)[0]
        # ax.set_title(self.Title)

        # ax =  self.figure.add_subplot(111) 
        # self.df.plot(x='col1',y='col2', ax=ax)
 
        self.canv.draw()

    
   
#========================================================================

    def readData(self):
        """ This function will read the data using pandas and call the update
                function to plot
        """
        base_name = os.path.basename(self.filename)
        self.Title = os.path.splitext(base_name)[0]
        print('FILE',self.Title )
        self.df = pd.read_csv(self.filename,encoding = 'utf-8').fillna(0)
        self.Update(self.themes[0]) # lets 0th theme be the default : bmh

    def Update(self,value):
        plt.clf()
        plt.style.use(value)
        try:
                self.horizontalLayout.removeWidget(self.toolbar)
                self.verticalLayout.removeWidget(self.canv)
                
                sip.delete(self.toolbar)
                sip.delete(self.canv)
                self.toolbar = None
                self.canv = None
                self.verticalLayout.removeItem(self.spacerItem1)
        except Exception as e:
                print(e)
                pass
        self.canv = MatplotlibCanvas(self)
        self.toolbar = NavigationToolbar(self.canv,self.plotWidget)
        
        self.horizontalLayout.addWidget(self.toolbar)
        self.verticalLayout.addWidget(self.canv)
        
#===================================================================


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dementia EDA"))
        self.TitleLabel.setText(_translate("MainWindow", "       Dementia Exploratory Data Analysis"))
        self.uploadcsvButton.setText(_translate("MainWindow", "Upload csv"))
        self.tableviewButton.setText(_translate("MainWindow", "View Dataframe"))
        self.NumberofPatients.setText(_translate("MainWindow", "Number of patients"))
        self.correlationMatrixbutton.setText(_translate("MainWindow", "Correlation matrix"))
        self.viewAgeplot.setText(_translate("MainWindow", "View Age plot"))
        self.plotMMSE.setText(_translate("MainWindow", "Plot MMSE"))
        self.viewGroupPlot.setCurrentText(_translate("MainWindow", "   View Group plot"))
        self.viewGroupPlot.setItemText(0, _translate("MainWindow", "   View Group plot"))
        self.comboBox2.setCurrentText(_translate("MainWindow", "   View Group plot"))
        self.comboBox2.setItemText(0, _translate("MainWindow", "   Theme"))
        self.machineLearningcomboBox.setCurrentText(_translate("MainWindow", "  Select Machine Learning"))
        self.machineLearningcomboBox.setItemText(0, _translate("MainWindow", "  Select Machine Learning"))
        self.machineLearningcomboBox.setItemText(1, _translate("MainWindow", "SVC- Support Vector Machine"))
        self.machineLearningcomboBox.setItemText(2, _translate("MainWindow", "Decision Tree Model"))
        self.machineLearningcomboBox.setItemText(3, _translate("MainWindow", "AdaBoost Model"))
        self.machineLearningcomboBox.setItemText(4, _translate("MainWindow", "Random Forest"))
        self.machineLearningcomboBox.setItemText(5, _translate("MainWindow", "XGBClassifier"))
        self.comparisonresultButton.setText(_translate("MainWindow", "Comparison Result (Machine Learning used)"))


   ##==========Attaching the functions to the buttons when clicked===========================================
        self.uploadcsvButton.clicked.connect(self.uploadCSV)
        self.NumberofPatients.clicked.connect(self.numOfpatient)
        self.tableviewButton.clicked.connect(self.viewDataframe)
        self.comboBox2.currentIndexChanged['QString'].connect(self.Update)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
