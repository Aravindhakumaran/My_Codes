# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Mon Nov 27 10:06:11 2017
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1309, 501)
        MainWindow.setStyleSheet(_fromUtf8("background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(_fromUtf8("#predictButton{    \n"
"    \n"
"background-color: qlineargradient(spread:pad, x1:0.489263, y1:1, x2:0.494, y2:0.00590909, stop:0 rgba(93, 173, 1, 255), stop:0.489474 rgba(96, 152, 0, 255), stop:1 rgba(100, 185, 1, 255));\n"
"\n"
"    \n"
"    color: rgb(203, 255, 204);\n"
"    border-radius:8px;\n"
"border:0.5px solid rgba(106, 167, 0, 255);\n"
"font: 75 15pt \"Segoe UI\";\n"
"\n"
"}\n"
"\n"
"#predictButton:hover{    \n"
"\n"
"    background-color: qlineargradient(spread:pad, x1:0.489263, y1:1, x2:0.494, y2:0.00590909, stop:0 rgba(101, 188, 1, 255), stop:0.489474 rgba(106, 167, 0, 255), stop:1 rgba(107, 198, 1, 255));\n"
"    \n"
"border:0.5px solid  rgba(93, 173, 1, 255);\n"
"\n"
"}\n"
"\n"
"#predictButton:pressed{    \n"
"    background-color: qlineargradient(spread:pad, x1:0.489263, y1:1, x2:0.494, y2:0.00590909, stop:0 rgba(93, 172, 1, 255), stop:0.489474 rgba(93, 147, 0, 255), stop:1 rgba(95, 177, 1, 255));\n"
"}\n"
"\n"
"QListWidget{\n"
"    background-color: qlineargradient(spread:pad, x1:0.542, y1:1, x2:0.542, y2:0.722, stop:0 rgba(213, 213, 213, 255), stop:0.273684 rgba(226, 226, 226, 255), stop:0.563158 rgba(255, 255, 255, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);\n"
"font: 12pt \"Segoe UI\";\n"
"border-bottom-left-radius:8px;\n"
"border-bottom-right-radius:8px;\n"
"}\n"
"\n"
"#label_3,#label_4{\n"
"border-top-left-radius:8px;\n"
"border-top-right-radius:8px;\n"
"font: 10pt \"Segoe UI\";    \n"
"color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0.526, y1:0.267, x2:0.526053, y2:1, stop:0 rgba(77, 77, 77, 255), stop:0.536842 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QSrollBar:horizontal{\n"
"border: 1px solid #999999;\n"
"width:8px;\n"
"background:white;\n"
"margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
"QSrollBar:vertical{\n"
"border: 1px solid #999999;\n"
"width:8px;\n"
"background:white;\n"
"margin: 0px 0px 0px 0px;\n"
"}\n"
"\n"
" QScrollBar::handle:horizontal{\n"
"width:8px;\n"
"background:black;\n"
"border-radius:4px;\n"
"min-height:0px;\n"
"\n"
"}\n"
"\n"
" QScrollBar::handle:vertical{\n"
"width:8px;\n"
"background:black;\n"
"border-radius:4px;\n"
"min-height:0px;\n"
"\n"
"}\n"
"\n"
"#deselct_btn , #selct_btn{\n"
" border-radius:5px;\n"
"border:0.6px solid black;\n"
"background-color: rgb(0, 0, 235);\n"
"color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"#deselct_btn:hover,#selct_btn:hover{\n"
" border-radius:5px;\n"
"border:0.6px solid black;\n"
"background-color: rgb(0, 0, 255);\n"
"color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"#deselct_btn:pressed,#selct_btn:pressed{\n"
" border-radius:5px;\n"
"border:0.6px solid black;\n"
"background-color: rgb(0, 0, 205);\n"
"color: rgb(255, 255, 255);\n"
"} \n"
"\n"
"#kg{\n"
"border-radius:5px;\n"
"border:0.5px solid gray;\n"
"}\n"
""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 721, 51))
        self.label.setStyleSheet(_fromUtf8("font: 75 22pt \"Segoe UI\";\n"
"background-color: qradialgradient(spread:pad, cx:0.542, cy:0, radius:0.729, fx:0.568, fy:0, stop:0 rgba(172, 172, 172, 255), stop:1 rgba(117, 117, 117, 255));"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.symp_List = QtGui.QListWidget(self.centralwidget)
        self.symp_List.setGeometry(QtCore.QRect(20, 90, 256, 192))
        self.symp_List.setStyleSheet(_fromUtf8(""))
        self.symp_List.setFrameShape(QtGui.QFrame.StyledPanel)
        self.symp_List.setFrameShadow(QtGui.QFrame.Sunken)
        self.symp_List.setObjectName(_fromUtf8("symp_List"))
        self.sel_Symp_List = QtGui.QListWidget(self.centralwidget)
        self.sel_Symp_List.setGeometry(QtCore.QRect(445, 90, 256, 192))
        self.sel_Symp_List.setStyleSheet(_fromUtf8(""))
        self.sel_Symp_List.setObjectName(_fromUtf8("sel_Symp_List"))
        self.deselct_btn = QtGui.QToolButton(self.centralwidget)
        self.deselct_btn.setGeometry(QtCore.QRect(290, 170, 61, 22))
        self.deselct_btn.setStyleSheet(_fromUtf8(""))
        self.deselct_btn.setObjectName(_fromUtf8("deselct_btn"))
        self.selct_btn = QtGui.QToolButton(self.centralwidget)
        self.selct_btn.setGeometry(QtCore.QRect(370, 170, 61, 22))
        self.selct_btn.setStyleSheet(_fromUtf8(""))
        self.selct_btn.setObjectName(_fromUtf8("selct_btn"))
        self.kg = QtGui.QLineEdit(self.centralwidget)
        self.kg.setGeometry(QtCore.QRect(226, 293, 51, 31))
        self.kg.setStyleSheet(_fromUtf8("font: 11pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);"))
        self.kg.setText(_fromUtf8(""))
        self.kg.setAlignment(QtCore.Qt.AlignCenter)
        self.kg.setObjectName(_fromUtf8("kg"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(76, 293, 131, 31))
        self.label_2.setStyleSheet(_fromUtf8("font: 11pt \"Segoe UI\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.predictButton = QtGui.QPushButton(self.centralwidget)
        self.predictButton.setGeometry(QtCore.QRect(320, 260, 81, 71))
        self.predictButton.setStyleSheet(_fromUtf8(""))
        self.predictButton.setAutoDefault(False)
        self.predictButton.setDefault(False)
        self.predictButton.setFlat(False)
        self.predictButton.setObjectName(_fromUtf8("predictButton"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 69, 256, 21))
        self.label_3.setStyleSheet(_fromUtf8(""))
        self.label_3.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(445, 70, 256, 21))
        self.label_4.setStyleSheet(_fromUtf8(""))
        self.label_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 340, 722, 161))
        self.scrollArea.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.522, y1:0, x2:0.528, y2:1, stop:1 rgba(175, 175, 175, 255), stop:0.5 rgba(117, 117, 117, 255));\n"
"\n"
"selection-background-color:qlineargradient(spread:pad, x1:0.526, y1:0.6875, x2:0.536579, y2:1, stop:0 rgba(117, 117, 117, 255), stop:0.989474 rgba(160, 160, 160, 255));"))
        self.scrollArea.setFrameShape(QtGui.QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(False)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 161))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(720, 0, 5, 501))
        self.line.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(117, 117, 117, 255), stop:0.485149 rgba(255, 255, 255, 255), stop:1 rgba(117, 117, 117, 255));"))
        self.line.setLineWidth(-1)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(1290, 4, 16, 493))
        self.pushButton.setStyleSheet(_fromUtf8("font: 75 16pt \"Segoe UI\";\n"
"selection-background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(227, 227, 227);"))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.webView = QtWebKit.QWebView(self.centralwidget)
        self.webView.setGeometry(QtCore.QRect(730, 5, 557, 351))
        self.webView.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.image = QtGui.QFrame(self.centralwidget)
        self.image.setGeometry(QtCore.QRect(940, 365, 130, 130))
        self.image.setStyleSheet(_fromUtf8(""))
        self.image.setFrameShape(QtGui.QFrame.StyledPanel)
        self.image.setFrameShadow(QtGui.QFrame.Raised)
        self.image.setObjectName(_fromUtf8("image"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Disease Prediction System", None))
        self.deselct_btn.setText(_translate("MainWindow", "<", None))
        self.selct_btn.setText(_translate("MainWindow", ">", None))
        self.label_2.setText(_translate("MainWindow", "Your Weight(in Kgs)", None))
        self.predictButton.setText(_translate("MainWindow", "Predict", None))
        self.label_3.setText(_translate("MainWindow", "Symptoms", None))
        self.label_4.setText(_translate("MainWindow", "Selected Symptoms", None))
        self.pushButton.setText(_translate("MainWindow", "<", None))
        self.actionQuit.setText(_translate("MainWindow", "&Quit", None))

from PyQt4 import QtWebKit
