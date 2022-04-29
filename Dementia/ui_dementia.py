# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dementiapGFyeR.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import images icons_rc
import images icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1856, 970)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.Greenframebehind = QFrame(self.centralwidget)
        self.Greenframebehind.setObjectName(u"Greenframebehind")
        self.Greenframebehind.setGeometry(QRect(10, 4, 1841, 941))
        self.Greenframebehind.setStyleSheet(u"background-color: rgb(16, 79, 127);")
        self.Greenframebehind.setFrameShape(QFrame.StyledPanel)
        self.Greenframebehind.setFrameShadow(QFrame.Raised)
        self.frameBehindplotWidget = QFrame(self.Greenframebehind)
        self.frameBehindplotWidget.setObjectName(u"frameBehindplotWidget")
        self.frameBehindplotWidget.setGeometry(QRect(9, 3, 1822, 911))
        self.frameBehindplotWidget.setStyleSheet(u"\n"
"background-color: rgb(199, 240, 248);")
        self.frameBehindplotWidget.setFrameShape(QFrame.StyledPanel)
        self.frameBehindplotWidget.setFrameShadow(QFrame.Raised)
        self.TitleLabel = QLabel(self.frameBehindplotWidget)
        self.TitleLabel.setObjectName(u"TitleLabel")
        self.TitleLabel.setGeometry(QRect(816, 20, 391, 41))
        self.TitleLabel.setStyleSheet(u"\n"
"font: 700 11pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(58, 115, 173);\n"
"border radius: 12px;")
        self.plotWidget = QWidget(self.frameBehindplotWidget)
        self.plotWidget.setObjectName(u"plotWidget")
        self.plotWidget.setGeometry(QRect(210, 191, 1591, 501))
        self.plotWidget.setStyleSheet(u"\n"
"\n"
"QWidget#plotWidget{border-radius: 6px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QWidget:hover#plotWidget\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.tableWidget = QTableWidget(self.plotWidget)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 1591, 611))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.behindTitleLabel1_2 = QLabel(self.frameBehindplotWidget)
        self.behindTitleLabel1_2.setObjectName(u"behindTitleLabel1_2")
        self.behindTitleLabel1_2.setGeometry(QRect(800, 10, 421, 61))
        self.behindTitleLabel1_2.setStyleSheet(u"\n"
"font: 700 11pt \"Segoe UI\";\n"
"background-color: rgb(16, 79, 127);\n"
"border radius: 12px;")
        self.uploadcsvButton = QPushButton(self.frameBehindplotWidget)
        self.uploadcsvButton.setObjectName(u"uploadcsvButton")
        self.uploadcsvButton.setGeometry(QRect(10, 40, 171, 41))
        self.uploadcsvButton.setStyleSheet(u"\n"
"\n"
"QPushButton#uploadcsvButton{border-radius: 12px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#uploadcsvButton\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/imagesicons/addIcon.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.uploadcsvButton.setIcon(icon)
        self.frameBehindplotWidget2 = QFrame(self.frameBehindplotWidget)
        self.frameBehindplotWidget2.setObjectName(u"frameBehindplotWidget2")
        self.frameBehindplotWidget2.setGeometry(QRect(200, 180, 1611, 621))
        self.frameBehindplotWidget2.setStyleSheet(u"QFrame#frameBehindplotWidget2{border-radius: 6px;\n"
"	background-color: rgb(16, 79, 127);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QFrame:hover#frameBehindplotWidget2\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.frameBehindplotWidget2.setFrameShape(QFrame.StyledPanel)
        self.frameBehindplotWidget2.setFrameShadow(QFrame.Raised)
        self.NumberofPatients = QPushButton(self.frameBehindplotWidget)
        self.NumberofPatients.setObjectName(u"NumberofPatients")
        self.NumberofPatients.setGeometry(QRect(220, 90, 181, 31))
        self.NumberofPatients.setStyleSheet(u"\n"
"\n"
"QPushButton#NumberofPatients{border-radius: 12px;\n"
"	background-color: rgb(155, 232, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#NumberofPatients\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.correlationMatrixbutton = QPushButton(self.frameBehindplotWidget)
        self.correlationMatrixbutton.setObjectName(u"correlationMatrixbutton")
        self.correlationMatrixbutton.setGeometry(QRect(410, 90, 181, 31))
        self.correlationMatrixbutton.setStyleSheet(u"\n"
"\n"
"QPushButton#correlationMatrixbutton{border-radius: 12px;\n"
"	\n"
"	border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#correlationMatrixbutton\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.viewAgeplot = QPushButton(self.frameBehindplotWidget)
        self.viewAgeplot.setObjectName(u"viewAgeplot")
        self.viewAgeplot.setGeometry(QRect(600, 90, 191, 31))
        self.viewAgeplot.setStyleSheet(u"\n"
"\n"
"QPushButton#viewAgeplot{border-radius: 12px;\n"
"	background-color: rgb(62, 197, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#viewAgeplot\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.plotMMSE = QPushButton(self.frameBehindplotWidget)
        self.plotMMSE.setObjectName(u"plotMMSE")
        self.plotMMSE.setGeometry(QRect(410, 130, 171, 31))
        self.plotMMSE.setStyleSheet(u"\n"
"\n"
"QPushButton#plotMMSE{border-radius: 12px;\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	background-color: rgb(0, 170, 255);\n"
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
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.viewGroupPlot = QComboBox(self.frameBehindplotWidget)
        self.viewGroupPlot.addItem("")
        self.viewGroupPlot.setObjectName(u"viewGroupPlot")
        self.viewGroupPlot.setGeometry(QRect(600, 130, 191, 31))
        self.viewGroupPlot.setStyleSheet(u"\n"
"\n"
"QComboBox#viewGroupPlot{border-radius: 12px;\n"
"	\n"
"	border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"	background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#viewGroupPlot\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.textEdit = QTextEdit(self.frameBehindplotWidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(200, 820, 1611, 81))
        self.textEdit.setStyleSheet(u"background-color: rgb(0, 59, 177);\n"
"")
        self.label = QLabel(self.frameBehindplotWidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 825, 1591, 71))
        self.label.setStyleSheet(u"background-color: rgb(222, 241, 255);")
        self.comparisonresultButton = QPushButton(self.frameBehindplotWidget)
        self.comparisonresultButton.setObjectName(u"comparisonresultButton")
        self.comparisonresultButton.setGeometry(QRect(1240, 130, 371, 31))
        self.comparisonresultButton.setStyleSheet(u"\n"
"\n"
"QPushButton#comparisonresultButton{border-radius: 12px;\n"
"	\n"
"	border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QPushButton:hover#comparisonresultButton\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.preprocessingFrame = QLabel(self.frameBehindplotWidget)
        self.preprocessingFrame.setObjectName(u"preprocessingFrame")
        self.preprocessingFrame.setGeometry(QRect(210, 80, 601, 91))
        self.preprocessingFrame.setStyleSheet(u"\n"
"\n"
"QLabel#preprocessingLabel{border-radius: 12px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"\n"
"	font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLabel:hover#preprocessingLabel\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.preprocessingFrame.setMidLineWidth(-1)
        self.dataprocessingLabel = QLabel(self.frameBehindplotWidget)
        self.dataprocessingLabel.setObjectName(u"dataprocessingLabel")
        self.dataprocessingLabel.setGeometry(QRect(430, 56, 181, 21))
        self.dataprocessingLabel.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border radius: 12px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.viewGroupPlot_2 = QComboBox(self.frameBehindplotWidget)
        self.viewGroupPlot_2.addItem("")
        self.viewGroupPlot_2.setObjectName(u"viewGroupPlot_2")
        self.viewGroupPlot_2.setGeometry(QRect(220, 130, 181, 31))
        self.viewGroupPlot_2.setStyleSheet(u"\n"
"\n"
"QComboBox#viewGroupPlot_2{border-radius: 12px;\n"
"	\n"
"	border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"	background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"	font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#viewGroupPlot_2\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.machineLearningcomboBox = QComboBox(self.frameBehindplotWidget)
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.addItem("")
        self.machineLearningcomboBox.setObjectName(u"machineLearningcomboBox")
        self.machineLearningcomboBox.setGeometry(QRect(1240, 90, 371, 31))
        self.machineLearningcomboBox.setStyleSheet(u"\n"
"\n"
"QComboBox#machineLearningcomboBox{border-radius: 12px;\n"
"	\n"
"	border-color: rgb(85, 170, 255);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"	background-color: rgb(158, 213, 255);\n"
"border-color:rgb(16, 79, 127);\n"
"		font: 700 9pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QComboBox:hover#machineLearningcomboBox\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.machineLearningFrame = QLabel(self.frameBehindplotWidget)
        self.machineLearningFrame.setObjectName(u"machineLearningFrame")
        self.machineLearningFrame.setGeometry(QRect(1210, 80, 601, 91))
        self.machineLearningFrame.setStyleSheet(u"\n"
"\n"
"QLabel#machineLearningLabel{border-radius: 12px;\n"
"	background-color: rgb(247, 255, 251);\n"
"border-style:outset;\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"\n"
"	font: 10pt \"Segoe UI\";\n"
";}\n"
"\n"
"\n"
"QLabel:hover#machineLearningLabel\n"
"{\n"
"border-width:2px;\n"
"	border-color: rgb(84, 204, 255);\n"
"}\n"
"")
        self.machineLearningFrame.setMidLineWidth(-1)
        self.machinelearningLabel = QLabel(self.frameBehindplotWidget)
        self.machinelearningLabel.setObjectName(u"machinelearningLabel")
        self.machinelearningLabel.setGeometry(QRect(1430, 56, 191, 21))
        self.machinelearningLabel.setStyleSheet(u"font: 9pt \"Segoe UI\";\n"
"text-decoration: underline;\n"
"font: 700 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border radius: 12px;\n"
"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 127);")
        self.machineLearningFrame.raise_()
        self.preprocessingFrame.raise_()
        self.frameBehindplotWidget2.raise_()
        self.behindTitleLabel1_2.raise_()
        self.TitleLabel.raise_()
        self.plotWidget.raise_()
        self.uploadcsvButton.raise_()
        self.NumberofPatients.raise_()
        self.correlationMatrixbutton.raise_()
        self.viewAgeplot.raise_()
        self.plotMMSE.raise_()
        self.viewGroupPlot.raise_()
        self.textEdit.raise_()
        self.label.raise_()
        self.comparisonresultButton.raise_()
        self.dataprocessingLabel.raise_()
        self.viewGroupPlot_2.raise_()
        self.machineLearningcomboBox.raise_()
        self.machinelearningLabel.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1856, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.TitleLabel.setText(QCoreApplication.translate("MainWindow", u"       Dementia Exploratory Data Analysis", None))
        self.behindTitleLabel1_2.setText("")
        self.uploadcsvButton.setText(QCoreApplication.translate("MainWindow", u"Upload csv", None))
        self.NumberofPatients.setText(QCoreApplication.translate("MainWindow", u"Number of patients", None))
        self.correlationMatrixbutton.setText(QCoreApplication.translate("MainWindow", u"Correlation matrix", None))
        self.viewAgeplot.setText(QCoreApplication.translate("MainWindow", u"View Age plot", None))
        self.plotMMSE.setText(QCoreApplication.translate("MainWindow", u"Plot MMSE", None))
        self.viewGroupPlot.setItemText(0, QCoreApplication.translate("MainWindow", u"   View Group plot", None))

        self.viewGroupPlot.setCurrentText(QCoreApplication.translate("MainWindow", u"   View Group plot", None))
        self.label.setText("")
        self.comparisonresultButton.setText(QCoreApplication.translate("MainWindow", u"Comparison Result (Machine Learning used)", None))
        self.preprocessingFrame.setText("")
        self.dataprocessingLabel.setText(QCoreApplication.translate("MainWindow", u"       DATA PREPROCESSING           ", None))
        self.viewGroupPlot_2.setItemText(0, QCoreApplication.translate("MainWindow", u"   View Group plot", None))

        self.viewGroupPlot_2.setCurrentText(QCoreApplication.translate("MainWindow", u"   View Group plot", None))
        self.machineLearningcomboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"  Select Machine Learning", None))
        self.machineLearningcomboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"SVC- Support Vector Machine", None))
        self.machineLearningcomboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Decision Tree Model", None))
        self.machineLearningcomboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"AdaBoost Model", None))
        self.machineLearningcomboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Random Forest", None))
        self.machineLearningcomboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"XGBClassifier", None))

        self.machineLearningcomboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"  Select Machine Learning", None))
        self.machineLearningFrame.setText("")
        self.machinelearningLabel.setText(QCoreApplication.translate("MainWindow", u"          MACHINE LEARNING        ", None))
    # retranslateUi

