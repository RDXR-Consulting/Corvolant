# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Corvolant(object):
    def setupUi(self, Corvolant):
        Corvolant.setObjectName("Corvolant")
        Corvolant.setWindowModality(QtCore.Qt.NonModal)
        Corvolant.resize(1000, 600)
        Corvolant.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Corvolant.setStyleSheet("background-color: rgb(16, 35, 48);")
        self.centralwidget = QtWidgets.QWidget(Corvolant)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 600))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.name_widget = QtWidgets.QWidget(self.centralwidget)
        self.name_widget.setMinimumSize(QtCore.QSize(120, 0))
        self.name_widget.setStyleSheet("background-color: rgb(20, 45, 62);\n"
"\n"
"QPushButton{\n"
"background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;\n"
"}")
        self.name_widget.setObjectName("name_widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.name_widget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.name_menu_button = QtWidgets.QPushButton(self.name_widget)
        self.name_menu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.name_menu_button.setMaximumSize(QtCore.QSize(50, 50))
        self.name_menu_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        self.name_menu_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_menu_button.setIcon(icon)
        self.name_menu_button.setIconSize(QtCore.QSize(20, 20))
        self.name_menu_button.setCheckable(True)
        self.name_menu_button.setAutoExclusive(False)
        self.name_menu_button.setObjectName("name_menu_button")
        self.verticalLayout_5.addWidget(self.name_menu_button)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.name_miners_button = QtWidgets.QPushButton(self.name_widget)
        self.name_miners_button.setMinimumSize(QtCore.QSize(50, 50))
        self.name_miners_button.setMaximumSize(QtCore.QSize(999999, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_miners_button.setFont(font)
        self.name_miners_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_miners_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/miners_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_miners_button.setIcon(icon1)
        self.name_miners_button.setIconSize(QtCore.QSize(20, 20))
        self.name_miners_button.setCheckable(True)
        self.name_miners_button.setAutoExclusive(True)
        self.name_miners_button.setObjectName("name_miners_button")
        self.verticalLayout_4.addWidget(self.name_miners_button)
        self.name_spies_button = QtWidgets.QPushButton(self.name_widget)
        self.name_spies_button.setMinimumSize(QtCore.QSize(50, 50))
        self.name_spies_button.setMaximumSize(QtCore.QSize(999999, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_spies_button.setFont(font)
        self.name_spies_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/spies_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_spies_button.setIcon(icon2)
        self.name_spies_button.setIconSize(QtCore.QSize(20, 20))
        self.name_spies_button.setCheckable(True)
        self.name_spies_button.setAutoExclusive(True)
        self.name_spies_button.setObjectName("name_spies_button")
        self.verticalLayout_4.addWidget(self.name_spies_button)
        self.name_useful_button = QtWidgets.QPushButton(self.name_widget)
        self.name_useful_button.setMinimumSize(QtCore.QSize(50, 50))
        self.name_useful_button.setMaximumSize(QtCore.QSize(999999, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.name_useful_button.setFont(font)
        self.name_useful_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/userful_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.name_useful_button.setIcon(icon3)
        self.name_useful_button.setIconSize(QtCore.QSize(20, 20))
        self.name_useful_button.setCheckable(True)
        self.name_useful_button.setAutoExclusive(True)
        self.name_useful_button.setObjectName("name_useful_button")
        self.verticalLayout_4.addWidget(self.name_useful_button)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.pushButton_6 = QtWidgets.QPushButton(self.name_widget)
        self.pushButton_6.setStyleSheet("color:white;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.verticalLayout_4.addWidget(self.pushButton_6)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout.addWidget(self.name_widget, 0, 1, 1, 1)
        self.main_widget = QtWidgets.QWidget(self.centralwidget)
        self.main_widget.setObjectName("main_widget")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.main_widget)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.stackedWidget = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget.setMaximumSize(QtCore.QSize(9999, 90))
        self.stackedWidget.setStyleSheet("background-color: rgb(20, 45, 62);\n"
"color: white;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.miners_page_button = QtWidgets.QWidget()
        self.miners_page_button.setObjectName("miners_page_button")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.miners_page_button)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.miners_page_button)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_9 = QtWidgets.QPushButton(self.miners_page_button)
        self.pushButton_9.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout.addWidget(self.pushButton_9)
        self.pushButton_10 = QtWidgets.QPushButton(self.miners_page_button)
        self.pushButton_10.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout.addWidget(self.pushButton_10)
        self.pushButton_11 = QtWidgets.QPushButton(self.miners_page_button)
        self.pushButton_11.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout.addWidget(self.pushButton_11)
        self.pushButton_12 = QtWidgets.QPushButton(self.miners_page_button)
        self.pushButton_12.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout.addWidget(self.pushButton_12)
        self.gridLayout_3.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.miners_page_button)
        self.spies_page_button = QtWidgets.QWidget()
        self.spies_page_button.setObjectName("spies_page_button")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.spies_page_button)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.spies_header_label = QtWidgets.QLabel(self.spies_page_button)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.spies_header_label.setFont(font)
        self.spies_header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.spies_header_label.setObjectName("spies_header_label")
        self.gridLayout_2.addWidget(self.spies_header_label, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_13 = QtWidgets.QPushButton(self.spies_page_button)
        self.pushButton_13.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_2.addWidget(self.pushButton_13)
        self.pushButton_14 = QtWidgets.QPushButton(self.spies_page_button)
        self.pushButton_14.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_2.addWidget(self.pushButton_14)
        self.pushButton_15 = QtWidgets.QPushButton(self.spies_page_button)
        self.pushButton_15.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_15.setObjectName("pushButton_15")
        self.horizontalLayout_2.addWidget(self.pushButton_15)
        self.pushButton_16 = QtWidgets.QPushButton(self.spies_page_button)
        self.pushButton_16.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_2.addWidget(self.pushButton_16)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_6.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.spies_page_button)
        self.useful_page_button = QtWidgets.QWidget()
        self.useful_page_button.setObjectName("useful_page_button")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.useful_page_button)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.useful_header_label = QtWidgets.QLabel(self.useful_page_button)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.useful_header_label.setFont(font)
        self.useful_header_label.setAlignment(QtCore.Qt.AlignCenter)
        self.useful_header_label.setObjectName("useful_header_label")
        self.gridLayout_4.addWidget(self.useful_header_label, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_17 = QtWidgets.QPushButton(self.useful_page_button)
        self.pushButton_17.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_17.setObjectName("pushButton_17")
        self.horizontalLayout_3.addWidget(self.pushButton_17)
        self.pushButton_18 = QtWidgets.QPushButton(self.useful_page_button)
        self.pushButton_18.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_3.addWidget(self.pushButton_18)
        self.pushButton_19 = QtWidgets.QPushButton(self.useful_page_button)
        self.pushButton_19.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_3.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.useful_page_button)
        self.pushButton_20.setMinimumSize(QtCore.QSize(0, 25))
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_3.addWidget(self.pushButton_20)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.gridLayout_7.addLayout(self.gridLayout_4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.useful_page_button)
        self.verticalLayout_7.addWidget(self.stackedWidget)
        self.stackedWidget_2 = QtWidgets.QStackedWidget(self.main_widget)
        self.stackedWidget_2.setObjectName("stackedWidget_2")
        self.home_page = QtWidgets.QWidget()
        self.home_page.setObjectName("home_page")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.home_page)
        self.gridLayout_16.setObjectName("gridLayout_16")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem1, 0, 0, 1, 1)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout()
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_7 = QtWidgets.QLabel(self.home_page)
        self.label_7.setMaximumSize(QtCore.QSize(250, 250))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/icon/crvl_logo.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_13.addWidget(self.label_7)
        self.label_6 = QtWidgets.QLabel(self.home_page)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;\n"
"background-color: none;")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_13.addWidget(self.label_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_13.addItem(spacerItem2)
        self.gridLayout_16.addLayout(self.verticalLayout_13, 0, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_16.addItem(spacerItem3, 0, 2, 1, 1)
        self.stackedWidget_2.addWidget(self.home_page)
        self.keygen_page = QtWidgets.QWidget()
        self.keygen_page.setObjectName("keygen_page")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.keygen_page)
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.widget = QtWidgets.QWidget(self.keygen_page)
        self.widget.setStyleSheet("background-color: rgb(20, 45, 62);\n"
"color: white;")
        self.widget.setObjectName("widget")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(-1, -1, -1, 60)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setReadOnly(True)
        self.textEdit.setPlaceholderText("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_9.addWidget(self.textEdit)
        self.gridLayout_10.addLayout(self.verticalLayout_9, 0, 0, 1, 1)
        self.gridLayout_11.addWidget(self.widget_2, 0, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_9.setContentsMargins(-1, 50, -1, -1)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_8.addWidget(self.checkBox)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setIconSize(QtCore.QSize(16, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_8.addWidget(self.checkBox_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.checkBox_3 = QtWidgets.QCheckBox(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_8.addWidget(self.checkBox_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem6)
        self.checkBox_4 = QtWidgets.QCheckBox(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_8.addWidget(self.checkBox_4)
        self.gridLayout_8.addLayout(self.verticalLayout_8, 0, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(250, 0, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setMaximumSize(QtCore.QSize(250, 25))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.gridLayout_8.addLayout(self.verticalLayout_10, 0, 1, 1, 1)
        self.gridLayout_9.addLayout(self.gridLayout_8, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout_9.addWidget(self.label_4, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_9.addWidget(self.pushButton, 3, 0, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem8, 4, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem9, 2, 0, 1, 1)
        self.gridLayout_11.addWidget(self.widget_3, 1, 0, 1, 1)
        self.gridLayout_12.addWidget(self.widget, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.keygen_page)
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget_2.addWidget(self.page)
        self.keylogger_page = QtWidgets.QWidget()
        self.keylogger_page.setObjectName("keylogger_page")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.keylogger_page)
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.widget_4 = QtWidgets.QWidget(self.keylogger_page)
        self.widget_4.setStyleSheet("background-color: rgb(20, 45, 62);\n"
"color: white;")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_5)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_12.addWidget(self.textEdit_2)
        self.gridLayout_14.addWidget(self.widget_5, 0, 0, 1, 1)
        self.widget_6 = QtWidgets.QWidget(self.widget_4)
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_5.setCheckable(True)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_5.addWidget(self.pushButton_5)
        self.verticalLayout_11.addLayout(self.horizontalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem11)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_11.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_11.addWidget(self.pushButton_4)
        self.gridLayout_13.addLayout(self.verticalLayout_11, 0, 0, 1, 1)
        self.gridLayout_14.addWidget(self.widget_6, 0, 1, 1, 1)
        self.gridLayout_15.addWidget(self.widget_4, 0, 0, 1, 1)
        self.stackedWidget_2.addWidget(self.keylogger_page)
        self.verticalLayout_7.addWidget(self.stackedWidget_2)
        self.gridLayout.addWidget(self.main_widget, 0, 2, 1, 1)
        self.icon_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_widget.setMinimumSize(QtCore.QSize(75, 0))
        self.icon_widget.setStyleSheet("background-color: rgb(20, 45, 62);\n"
"QPushButton{\n"
"background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;}")
        self.icon_widget.setObjectName("icon_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.icon_menu_button = QtWidgets.QPushButton(self.icon_widget)
        self.icon_menu_button.setMinimumSize(QtCore.QSize(50, 50))
        self.icon_menu_button.setMaximumSize(QtCore.QSize(50, 50))
        self.icon_menu_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        self.icon_menu_button.setText("")
        self.icon_menu_button.setIcon(icon)
        self.icon_menu_button.setIconSize(QtCore.QSize(20, 20))
        self.icon_menu_button.setCheckable(True)
        self.icon_menu_button.setChecked(False)
        self.icon_menu_button.setAutoRepeat(False)
        self.icon_menu_button.setAutoExclusive(False)
        self.icon_menu_button.setObjectName("icon_menu_button")
        self.verticalLayout_2.addWidget(self.icon_menu_button)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.icon_miners_button = QtWidgets.QPushButton(self.icon_widget)
        self.icon_miners_button.setMinimumSize(QtCore.QSize(50, 50))
        self.icon_miners_button.setMaximumSize(QtCore.QSize(50, 50))
        self.icon_miners_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        self.icon_miners_button.setText("")
        self.icon_miners_button.setIcon(icon1)
        self.icon_miners_button.setIconSize(QtCore.QSize(20, 20))
        self.icon_miners_button.setCheckable(True)
        self.icon_miners_button.setAutoExclusive(True)
        self.icon_miners_button.setObjectName("icon_miners_button")
        self.verticalLayout.addWidget(self.icon_miners_button)
        self.icon_spies_button = QtWidgets.QPushButton(self.icon_widget)
        self.icon_spies_button.setMinimumSize(QtCore.QSize(50, 50))
        self.icon_spies_button.setMaximumSize(QtCore.QSize(50, 50))
        self.icon_spies_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        self.icon_spies_button.setText("")
        self.icon_spies_button.setIcon(icon2)
        self.icon_spies_button.setIconSize(QtCore.QSize(20, 20))
        self.icon_spies_button.setCheckable(True)
        self.icon_spies_button.setAutoExclusive(True)
        self.icon_spies_button.setObjectName("icon_spies_button")
        self.verticalLayout.addWidget(self.icon_spies_button)
        self.icon_useful_button = QtWidgets.QPushButton(self.icon_widget)
        self.icon_useful_button.setMinimumSize(QtCore.QSize(50, 50))
        self.icon_useful_button.setMaximumSize(QtCore.QSize(50, 50))
        self.icon_useful_button.setStyleSheet("background-color: rgb(29, 84, 87);\n"
"border: none;\n"
"color: white;")
        self.icon_useful_button.setText("")
        self.icon_useful_button.setIcon(icon3)
        self.icon_useful_button.setIconSize(QtCore.QSize(20, 20))
        self.icon_useful_button.setCheckable(True)
        self.icon_useful_button.setAutoExclusive(True)
        self.icon_useful_button.setObjectName("icon_useful_button")
        self.verticalLayout.addWidget(self.icon_useful_button)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem12)
        self.pushButton_7 = QtWidgets.QPushButton(self.icon_widget)
        self.pushButton_7.setStyleSheet("color:white;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.gridLayout.addWidget(self.icon_widget, 0, 0, 1, 1)
        Corvolant.setCentralWidget(self.centralwidget)

        self.retranslateUi(Corvolant)
        self.stackedWidget.setCurrentIndex(2)
        self.stackedWidget_2.setCurrentIndex(0)
        self.icon_menu_button.toggled['bool'].connect(self.icon_widget.setHidden) # type: ignore
        self.icon_menu_button.toggled['bool'].connect(self.name_widget.setVisible) # type: ignore
        self.name_menu_button.toggled['bool'].connect(self.name_widget.setHidden) # type: ignore
        self.name_menu_button.toggled['bool'].connect(self.icon_widget.setVisible) # type: ignore
        self.pushButton_2.toggled['bool'].connect(self.pushButton_5.setVisible) # type: ignore
        self.pushButton_2.toggled['bool'].connect(self.pushButton_2.setHidden) # type: ignore
        self.pushButton_5.toggled['bool'].connect(self.pushButton_5.setHidden) # type: ignore
        self.pushButton_5.toggled['bool'].connect(self.pushButton_2.setVisible) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Corvolant)

    def retranslateUi(self, Corvolant):
        _translate = QtCore.QCoreApplication.translate
        Corvolant.setWindowTitle(_translate("Corvolant", "MainWindow"))
        self.name_miners_button.setText(_translate("Corvolant", "Miners"))
        self.name_spies_button.setText(_translate("Corvolant", "Spies"))
        self.name_useful_button.setText(_translate("Corvolant", "Useful"))
        self.pushButton_6.setText(_translate("Corvolant", "Home"))
        self.label_2.setText(_translate("Corvolant", "Miners"))
        self.pushButton_9.setText(_translate("Corvolant", "Keylogger"))
        self.pushButton_10.setText(_translate("Corvolant", "Miners_кнопка"))
        self.pushButton_11.setText(_translate("Corvolant", "Miners_кнопка"))
        self.pushButton_12.setText(_translate("Corvolant", "Miners_кнопка"))
        self.spies_header_label.setText(_translate("Corvolant", "Spies"))
        self.pushButton_13.setText(_translate("Corvolant", "Spies_кнопка"))
        self.pushButton_14.setText(_translate("Corvolant", "Spies_кнопка"))
        self.pushButton_15.setText(_translate("Corvolant", "Spies_кнопка"))
        self.pushButton_16.setText(_translate("Corvolant", "Spies_кнопка"))
        self.useful_header_label.setText(_translate("Corvolant", "Useful"))
        self.pushButton_17.setText(_translate("Corvolant", "Генератор паролей"))
        self.pushButton_18.setText(_translate("Corvolant", "Useful_кнопка"))
        self.pushButton_19.setText(_translate("Corvolant", "Useful_кнопка"))
        self.pushButton_20.setText(_translate("Corvolant", "Useful_кнопка"))
        self.label_6.setText(_translate("Corvolant", "CORVOLANT"))
        self.label_3.setText(_translate("Corvolant", "Generate password"))
        self.textEdit.setHtml(_translate("Corvolant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt;\">your password</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:10pt;\"><br /></p></body></html>"))
        self.checkBox.setText(_translate("Corvolant", "Uppercase"))
        self.checkBox_2.setText(_translate("Corvolant", "Lowercase"))
        self.checkBox_3.setText(_translate("Corvolant", "Num"))
        self.checkBox_4.setText(_translate("Corvolant", "Symbols"))
        self.label_5.setText(_translate("Corvolant", "Password Lenght:"))
        self.label_4.setText(_translate("Corvolant", "Settings"))
        self.pushButton.setText(_translate("Corvolant", "Generate"))
        self.label.setText(_translate("Corvolant", "Pressed buttons log"))
        self.textEdit_2.setHtml(_translate("Corvolant", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:43 - G</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:43 - i</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:43 - t</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:44 - enter</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:44 - esc</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:44 - backspace</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:49 - v</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">11:49 - k</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Corvolant", "Начать запись"))
        self.pushButton_5.setText(_translate("Corvolant", "Остановить запись"))
        self.pushButton_3.setText(_translate("Corvolant", "Очисть лог"))
        self.pushButton_4.setText(_translate("Corvolant", "Сохранить в файл"))
        self.pushButton_7.setText(_translate("Corvolant", "H"))
import resources_rc
