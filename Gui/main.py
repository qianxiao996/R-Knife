# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QCheckBox, QComboBox,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QPlainTextEdit, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QTabWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(874, 644)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget_2 = QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_3 = QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.label = QLabel(self.tab_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(self.tab_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 0))
        self.lineEdit.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.label_2 = QLabel(self.tab_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.tab_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(200, 25))

        self.horizontalLayout.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.tab_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.tab_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMaximumSize(QSize(70, 25))
        self.lineEdit_3.setMaxLength(5)

        self.horizontalLayout.addWidget(self.lineEdit_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.tab_3)
        self.tabWidget.setObjectName(u"tabWidget")

        self.verticalLayout.addWidget(self.tabWidget)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_6 = QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget_4 = QTabWidget(self.tab_5)
        self.tabWidget_4.setObjectName(u"tabWidget_4")
        self.tabWidget_4.setDocumentMode(False)
        self.tabWidget_4.setTabsClosable(True)
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.gridLayout_11 = QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.Result_text = QPlainTextEdit(self.tab_10)
        self.Result_text.setObjectName(u"Result_text")

        self.gridLayout_11.addWidget(self.Result_text, 1, 0, 1, 1)

        self.Source_text = QPlainTextEdit(self.tab_10)
        self.Source_text.setObjectName(u"Source_text")

        self.gridLayout_11.addWidget(self.Source_text, 0, 0, 1, 1)

        self.tabWidget_4.addTab(self.tab_10, "")

        self.gridLayout_6.addWidget(self.tabWidget_4, 1, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.checkBox_line = QCheckBox(self.tab_5)
        self.checkBox_line.setObjectName(u"checkBox_line")
        self.checkBox_line.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.checkBox_line)

        self.encode_type = QComboBox(self.tab_5)
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.encode_type.setObjectName(u"encode_type")
        self.encode_type.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_8.addWidget(self.encode_type)

        self.label_12 = QLabel(self.tab_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_12)

        self.comboBox_encode = QComboBox(self.tab_5)
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.setObjectName(u"comboBox_encode")
        self.comboBox_encode.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_encode)

        self.label_11 = QLabel(self.tab_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_11)

        self.comboBox_decode = QComboBox(self.tab_5)
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.setObjectName(u"comboBox_decode")
        self.comboBox_decode.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_decode)

        self.label_13 = QLabel(self.tab_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_13)

        self.comboBox_jinzhi = QComboBox(self.tab_5)
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.addItem("")
        self.comboBox_jinzhi.setObjectName(u"comboBox_jinzhi")
        self.comboBox_jinzhi.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_8.addWidget(self.comboBox_jinzhi)


        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayout = QGridLayout(self.tab_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_54 = QLabel(self.tab_4)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMinimumSize(QSize(0, 28))
        self.label_54.setMaximumSize(QSize(400, 16777215))

        self.horizontalLayout_6.addWidget(self.label_54)

        self.pushButton_morenpasswd_daochu = QPushButton(self.tab_4)
        self.pushButton_morenpasswd_daochu.setObjectName(u"pushButton_morenpasswd_daochu")
        self.pushButton_morenpasswd_daochu.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_morenpasswd_daochu)


        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_47 = QLabel(self.tab_4)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_41.addWidget(self.label_47)

        self.lineEdit_select_data = QLineEdit(self.tab_4)
        self.lineEdit_select_data.setObjectName(u"lineEdit_select_data")

        self.horizontalLayout_41.addWidget(self.lineEdit_select_data)

        self.pushButton_morenpasswd_start = QPushButton(self.tab_4)
        self.pushButton_morenpasswd_start.setObjectName(u"pushButton_morenpasswd_start")

        self.horizontalLayout_41.addWidget(self.pushButton_morenpasswd_start)


        self.gridLayout.addLayout(self.horizontalLayout_41, 0, 1, 1, 1)

        self.listWidget_morenpasswd_list = QListWidget(self.tab_4)
        self.listWidget_morenpasswd_list.setObjectName(u"listWidget_morenpasswd_list")
        self.listWidget_morenpasswd_list.setMinimumSize(QSize(250, 0))
        self.listWidget_morenpasswd_list.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.listWidget_morenpasswd_list, 1, 0, 1, 1)

        self.tableWidget_morenpasswd_result = QTableWidget(self.tab_4)
        if (self.tableWidget_morenpasswd_result.columnCount() < 4):
            self.tableWidget_morenpasswd_result.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tableWidget_morenpasswd_result.setObjectName(u"tableWidget_morenpasswd_result")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_morenpasswd_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_morenpasswd_result.setSizePolicy(sizePolicy)
        self.tableWidget_morenpasswd_result.setMinimumSize(QSize(500, 0))
        self.tableWidget_morenpasswd_result.setFocusPolicy(Qt.NoFocus)
        self.tableWidget_morenpasswd_result.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableWidget_morenpasswd_result.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_morenpasswd_result.setSortingEnabled(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setVisible(False)
        self.tableWidget_morenpasswd_result.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_morenpasswd_result.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_morenpasswd_result.horizontalHeader().setHighlightSections(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_morenpasswd_result.verticalHeader().setVisible(False)
        self.tableWidget_morenpasswd_result.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_morenpasswd_result.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_morenpasswd_result.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_morenpasswd_result.verticalHeader().setHighlightSections(True)
        self.tableWidget_morenpasswd_result.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget_morenpasswd_result.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tableWidget_morenpasswd_result, 1, 1, 1, 1)

        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_4 = QGridLayout(self.tab_6)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_57 = QGridLayout()
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_24 = QLabel(self.tab_6)
        self.label_24.setObjectName(u"label_24")

        self.horizontalLayout_7.addWidget(self.label_24)

        self.lineEdit_cmd_ip = QLineEdit(self.tab_6)
        self.lineEdit_cmd_ip.setObjectName(u"lineEdit_cmd_ip")

        self.horizontalLayout_7.addWidget(self.lineEdit_cmd_ip)

        self.label_30 = QLabel(self.tab_6)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_7.addWidget(self.label_30)

        self.lineEdit_cmd_port = QLineEdit(self.tab_6)
        self.lineEdit_cmd_port.setObjectName(u"lineEdit_cmd_port")

        self.horizontalLayout_7.addWidget(self.lineEdit_cmd_port)

        self.pushButton_re_go = QPushButton(self.tab_6)
        self.pushButton_re_go.setObjectName(u"pushButton_re_go")

        self.horizontalLayout_7.addWidget(self.pushButton_re_go)


        self.gridLayout_57.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)

        self.textEdit_cmd_result = QTextEdit(self.tab_6)
        self.textEdit_cmd_result.setObjectName(u"textEdit_cmd_result")

        self.gridLayout_57.addWidget(self.textEdit_cmd_result, 1, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_57, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_8 = QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_25 = QLabel(self.tab_2)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_10.addWidget(self.label_25)

        self.lineEdit_file_url = QLineEdit(self.tab_2)
        self.lineEdit_file_url.setObjectName(u"lineEdit_file_url")

        self.horizontalLayout_10.addWidget(self.lineEdit_file_url)

        self.label_31 = QLabel(self.tab_2)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_10.addWidget(self.label_31)

        self.lineEdit_file_dest_name = QLineEdit(self.tab_2)
        self.lineEdit_file_dest_name.setObjectName(u"lineEdit_file_dest_name")

        self.horizontalLayout_10.addWidget(self.lineEdit_file_dest_name)

        self.pushButton_file_start = QPushButton(self.tab_2)
        self.pushButton_file_start.setObjectName(u"pushButton_file_start")

        self.horizontalLayout_10.addWidget(self.pushButton_file_start)


        self.gridLayout_8.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)

        self.textEdit_file_result = QTextEdit(self.tab_2)
        self.textEdit_file_result.setObjectName(u"textEdit_file_result")

        self.gridLayout_8.addWidget(self.textEdit_file_result, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.gridLayout_7 = QGridLayout(self.tab_8)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_51 = QLabel(self.tab_8)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.label_51)

        self.pushButton_sharuanchaxun_start = QPushButton(self.tab_8)
        self.pushButton_sharuanchaxun_start.setObjectName(u"pushButton_sharuanchaxun_start")
        self.pushButton_sharuanchaxun_start.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_2.addWidget(self.pushButton_sharuanchaxun_start)


        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.textEdit_sharuanchaxun_result = QTextEdit(self.tab_8)
        self.textEdit_sharuanchaxun_result.setObjectName(u"textEdit_sharuanchaxun_result")
        self.textEdit_sharuanchaxun_result.setMinimumSize(QSize(0, 0))

        self.gridLayout_7.addWidget(self.textEdit_sharuanchaxun_result, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_13 = QWidget()
        self.tab_13.setObjectName(u"tab_13")
        self.gridLayout_10 = QGridLayout(self.tab_13)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.tab_13)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.pushButton_tiquanchaxun_start = QPushButton(self.tab_13)
        self.pushButton_tiquanchaxun_start.setObjectName(u"pushButton_tiquanchaxun_start")
        self.pushButton_tiquanchaxun_start.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_4.addWidget(self.pushButton_tiquanchaxun_start)


        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.textEdit_tiquanchaxun_result = QTextEdit(self.tab_13)
        self.textEdit_tiquanchaxun_result.setObjectName(u"textEdit_tiquanchaxun_result")
        self.textEdit_tiquanchaxun_result.setMinimumSize(QSize(0, 0))

        self.gridLayout_10.addWidget(self.textEdit_tiquanchaxun_result, 1, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_5 = QGridLayout(self.tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_5 = QLabel(self.tab)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_5.addWidget(self.label_5)

        self.radioButton_bash = QRadioButton(self.tab)
        self.radioButton_bash.setObjectName(u"radioButton_bash")
        self.radioButton_bash.setChecked(True)

        self.horizontalLayout_5.addWidget(self.radioButton_bash)

        self.radioButton_powershell = QRadioButton(self.tab)
        self.radioButton_powershell.setObjectName(u"radioButton_powershell")

        self.horizontalLayout_5.addWidget(self.radioButton_powershell)

        self.radioButton_python = QRadioButton(self.tab)
        self.radioButton_python.setObjectName(u"radioButton_python")

        self.horizontalLayout_5.addWidget(self.radioButton_python)

        self.radioButton_perl = QRadioButton(self.tab)
        self.radioButton_perl.setObjectName(u"radioButton_perl")

        self.horizontalLayout_5.addWidget(self.radioButton_perl)

        self.pushButton_copy = QPushButton(self.tab)
        self.pushButton_copy.setObjectName(u"pushButton_copy")

        self.horizontalLayout_5.addWidget(self.pushButton_copy)

        self.pushButton_encode = QPushButton(self.tab)
        self.pushButton_encode.setObjectName(u"pushButton_encode")

        self.horizontalLayout_5.addWidget(self.pushButton_encode)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.textEdit_java_result = QTextEdit(self.tab)
        self.textEdit_java_result.setObjectName(u"textEdit_java_result")

        self.verticalLayout_2.addWidget(self.textEdit_java_result)


        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.gridLayout_12 = QGridLayout(self.tab_7)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.tabWidget_3 = QTabWidget(self.tab_7)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.gridLayout_13 = QGridLayout(self.tab_9)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.comboBox_sfzh_province = QComboBox(self.tab_9)
        self.comboBox_sfzh_province.addItem("")
        self.comboBox_sfzh_province.setObjectName(u"comboBox_sfzh_province")

        self.horizontalLayout_9.addWidget(self.comboBox_sfzh_province)

        self.label_7 = QLabel(self.tab_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(30, 16777215))
        self.label_7.setLayoutDirection(Qt.LeftToRight)
        self.label_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.comboBox_sfzh_city = QComboBox(self.tab_9)
        self.comboBox_sfzh_city.addItem("")
        self.comboBox_sfzh_city.setObjectName(u"comboBox_sfzh_city")

        self.horizontalLayout_9.addWidget(self.comboBox_sfzh_city)

        self.label_9 = QLabel(self.tab_9)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_9.addWidget(self.label_9)

        self.comboBox_sfzh_area = QComboBox(self.tab_9)
        self.comboBox_sfzh_area.addItem("")
        self.comboBox_sfzh_area.setObjectName(u"comboBox_sfzh_area")

        self.horizontalLayout_9.addWidget(self.comboBox_sfzh_area)

        self.label_10 = QLabel(self.tab_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(70, 16777215))

        self.horizontalLayout_9.addWidget(self.label_10)


        self.gridLayout_13.addLayout(self.horizontalLayout_9, 0, 0, 1, 3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_14 = QLabel(self.tab_9)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_12.addWidget(self.label_14)

        self.comboBox_sfzh_sex = QComboBox(self.tab_9)
        self.comboBox_sfzh_sex.addItem("")
        self.comboBox_sfzh_sex.addItem("")
        self.comboBox_sfzh_sex.addItem("")
        self.comboBox_sfzh_sex.setObjectName(u"comboBox_sfzh_sex")

        self.horizontalLayout_12.addWidget(self.comboBox_sfzh_sex)

        self.label_8 = QLabel(self.tab_9)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_12.addWidget(self.label_8)

        self.spinBox_sfzh_num = QSpinBox(self.tab_9)
        self.spinBox_sfzh_num.setObjectName(u"spinBox_sfzh_num")
        self.spinBox_sfzh_num.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_sfzh_num.setMinimum(0)
        self.spinBox_sfzh_num.setMaximum(65535)
        self.spinBox_sfzh_num.setValue(500)

        self.horizontalLayout_12.addWidget(self.spinBox_sfzh_num)

        self.checkBox_sfzh = QCheckBox(self.tab_9)
        self.checkBox_sfzh.setObjectName(u"checkBox_sfzh")

        self.horizontalLayout_12.addWidget(self.checkBox_sfzh)


        self.gridLayout_13.addLayout(self.horizontalLayout_12, 0, 3, 1, 2)

        self.label_6 = QLabel(self.tab_9)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_13.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_sfzh = QLineEdit(self.tab_9)
        self.lineEdit_sfzh.setObjectName(u"lineEdit_sfzh")

        self.gridLayout_13.addWidget(self.lineEdit_sfzh, 1, 1, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_15 = QLabel(self.tab_9)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_11.addWidget(self.label_15)

        self.comboBox_sfzh_year = QComboBox(self.tab_9)
        self.comboBox_sfzh_year.addItem("")
        self.comboBox_sfzh_year.addItem("")
        self.comboBox_sfzh_year.addItem("")
        self.comboBox_sfzh_year.setObjectName(u"comboBox_sfzh_year")

        self.horizontalLayout_11.addWidget(self.comboBox_sfzh_year)

        self.comboBox_sfzh_year_2 = QComboBox(self.tab_9)
        self.comboBox_sfzh_year_2.addItem("")
        self.comboBox_sfzh_year_2.setObjectName(u"comboBox_sfzh_year_2")

        self.horizontalLayout_11.addWidget(self.comboBox_sfzh_year_2)

        self.label_16 = QLabel(self.tab_9)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_11.addWidget(self.label_16)

        self.comboBox_sfzh_month = QComboBox(self.tab_9)
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.addItem("")
        self.comboBox_sfzh_month.setObjectName(u"comboBox_sfzh_month")

        self.horizontalLayout_11.addWidget(self.comboBox_sfzh_month)

        self.label_17 = QLabel(self.tab_9)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_11.addWidget(self.label_17)

        self.comboBox_sfzh_day = QComboBox(self.tab_9)
        self.comboBox_sfzh_day.addItem("")
        self.comboBox_sfzh_day.setObjectName(u"comboBox_sfzh_day")

        self.horizontalLayout_11.addWidget(self.comboBox_sfzh_day)

        self.label_18 = QLabel(self.tab_9)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_11.addWidget(self.label_18)


        self.gridLayout_13.addLayout(self.horizontalLayout_11, 1, 2, 1, 2)

        self.pushButton_sfzh_go = QPushButton(self.tab_9)
        self.pushButton_sfzh_go.setObjectName(u"pushButton_sfzh_go")
        self.pushButton_sfzh_go.setMaximumSize(QSize(100, 16777215))

        self.gridLayout_13.addWidget(self.pushButton_sfzh_go, 1, 4, 1, 1)

        self.textEdit_sfzh_result = QTextEdit(self.tab_9)
        self.textEdit_sfzh_result.setObjectName(u"textEdit_sfzh_result")

        self.gridLayout_13.addWidget(self.textEdit_sfzh_result, 2, 0, 1, 5)

        self.tabWidget_3.addTab(self.tab_9, "")
        self.tab_11 = QWidget()
        self.tab_11.setObjectName(u"tab_11")
        self.gridLayout_15 = QGridLayout(self.tab_11)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.comboBox_phone_province = QComboBox(self.tab_11)
        self.comboBox_phone_province.addItem("")
        self.comboBox_phone_province.setObjectName(u"comboBox_phone_province")

        self.horizontalLayout_14.addWidget(self.comboBox_phone_province)

        self.label_19 = QLabel(self.tab_11)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.label_19)

        self.comboBox_phone_city = QComboBox(self.tab_11)
        self.comboBox_phone_city.addItem("")
        self.comboBox_phone_city.setObjectName(u"comboBox_phone_city")

        self.horizontalLayout_14.addWidget(self.comboBox_phone_city)

        self.label_20 = QLabel(self.tab_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout_14.addWidget(self.label_20)


        self.gridLayout_15.addLayout(self.horizontalLayout_14, 0, 0, 1, 1)

        self.label_21 = QLabel(self.tab_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_15.addWidget(self.label_21, 0, 1, 1, 1)

        self.comboBox_phone_operator = QComboBox(self.tab_11)
        self.comboBox_phone_operator.addItem("")
        self.comboBox_phone_operator.setObjectName(u"comboBox_phone_operator")

        self.gridLayout_15.addWidget(self.comboBox_phone_operator, 0, 2, 1, 1)

        self.label_22 = QLabel(self.tab_11)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_15.addWidget(self.label_22, 0, 3, 1, 1)

        self.comboBox_phone_number = QComboBox(self.tab_11)
        self.comboBox_phone_number.addItem("")
        self.comboBox_phone_number.setObjectName(u"comboBox_phone_number")

        self.gridLayout_15.addWidget(self.comboBox_phone_number, 0, 4, 1, 1)

        self.label_23 = QLabel(self.tab_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(40, 16777215))

        self.gridLayout_15.addWidget(self.label_23, 0, 5, 1, 1)

        self.spinBox_phone_num = QSpinBox(self.tab_11)
        self.spinBox_phone_num.setObjectName(u"spinBox_phone_num")
        self.spinBox_phone_num.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_phone_num.setMinimum(0)
        self.spinBox_phone_num.setMaximum(65535)
        self.spinBox_phone_num.setValue(500)

        self.gridLayout_15.addWidget(self.spinBox_phone_num, 0, 6, 1, 1)

        self.checkBox_phone_num = QCheckBox(self.tab_11)
        self.checkBox_phone_num.setObjectName(u"checkBox_phone_num")

        self.gridLayout_15.addWidget(self.checkBox_phone_num, 0, 7, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_phone_go = QPushButton(self.tab_11)
        self.pushButton_phone_go.setObjectName(u"pushButton_phone_go")

        self.verticalLayout_4.addWidget(self.pushButton_phone_go)

        self.pushButton_phone_number = QPushButton(self.tab_11)
        self.pushButton_phone_number.setObjectName(u"pushButton_phone_number")

        self.verticalLayout_4.addWidget(self.pushButton_phone_number)


        self.gridLayout_15.addLayout(self.verticalLayout_4, 0, 8, 2, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_26 = QLabel(self.tab_11)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_20.addWidget(self.label_26)

        self.spinBox_phone_start_num = QSpinBox(self.tab_11)
        self.spinBox_phone_start_num.setObjectName(u"spinBox_phone_start_num")
        self.spinBox_phone_start_num.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_phone_start_num.setMinimum(0)
        self.spinBox_phone_start_num.setMaximum(9999)
        self.spinBox_phone_start_num.setSingleStep(1)
        self.spinBox_phone_start_num.setValue(0)

        self.horizontalLayout_20.addWidget(self.spinBox_phone_start_num)

        self.label_27 = QLabel(self.tab_11)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_20.addWidget(self.label_27)

        self.spinBox_phone_end_num = QSpinBox(self.tab_11)
        self.spinBox_phone_end_num.setObjectName(u"spinBox_phone_end_num")
        self.spinBox_phone_end_num.setInputMethodHints(Qt.ImhDigitsOnly)
        self.spinBox_phone_end_num.setMinimum(0)
        self.spinBox_phone_end_num.setMaximum(9999)
        self.spinBox_phone_end_num.setSingleStep(1)
        self.spinBox_phone_end_num.setValue(9999)

        self.horizontalLayout_20.addWidget(self.spinBox_phone_end_num)

        self.label_28 = QLabel(self.tab_11)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_20.addWidget(self.label_28)

        self.lineEdit_phone = QLineEdit(self.tab_11)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")

        self.horizontalLayout_20.addWidget(self.lineEdit_phone)


        self.gridLayout_15.addLayout(self.horizontalLayout_20, 1, 0, 1, 8)

        self.textEdit_phone_result = QTextEdit(self.tab_11)
        self.textEdit_phone_result.setObjectName(u"textEdit_phone_result")

        self.gridLayout_15.addWidget(self.textEdit_phone_result, 2, 0, 1, 9)

        self.tabWidget_3.addTab(self.tab_11, "")

        self.gridLayout_12.addWidget(self.tabWidget_3, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_7, "")
        self.tab_12 = QWidget()
        self.tab_12.setObjectName(u"tab_12")
        self.gridLayout_9 = QGridLayout(self.tab_12)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tools_source = QPlainTextEdit(self.tab_12)
        self.tools_source.setObjectName(u"tools_source")

        self.horizontalLayout_3.addWidget(self.tools_source)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tools_daoxu = QPushButton(self.tab_12)
        self.tools_daoxu.setObjectName(u"tools_daoxu")

        self.verticalLayout_3.addWidget(self.tools_daoxu)

        self.tools_xiaoxie = QPushButton(self.tab_12)
        self.tools_xiaoxie.setObjectName(u"tools_xiaoxie")

        self.verticalLayout_3.addWidget(self.tools_xiaoxie)

        self.tool_daxie = QPushButton(self.tab_12)
        self.tool_daxie.setObjectName(u"tool_daxie")

        self.verticalLayout_3.addWidget(self.tool_daxie)

        self.tools_remove_duplicate = QPushButton(self.tab_12)
        self.tools_remove_duplicate.setObjectName(u"tools_remove_duplicate")

        self.verticalLayout_3.addWidget(self.tools_remove_duplicate)

        self.tools_zhongwen_pinyin = QPushButton(self.tab_12)
        self.tools_zhongwen_pinyin.setObjectName(u"tools_zhongwen_pinyin")

        self.verticalLayout_3.addWidget(self.tools_zhongwen_pinyin)

        self.tools_tiqushouzimu = QPushButton(self.tab_12)
        self.tools_tiqushouzimu.setObjectName(u"tools_tiqushouzimu")

        self.verticalLayout_3.addWidget(self.tools_tiqushouzimu)

        self.tools_get_ip = QPushButton(self.tab_12)
        self.tools_get_ip.setObjectName(u"tools_get_ip")

        self.verticalLayout_3.addWidget(self.tools_get_ip)

        self.tools_ip = QPushButton(self.tab_12)
        self.tools_ip.setObjectName(u"tools_ip")

        self.verticalLayout_3.addWidget(self.tools_ip)

        self.tools_get_china_ip = QPushButton(self.tab_12)
        self.tools_get_china_ip.setObjectName(u"tools_get_china_ip")

        self.verticalLayout_3.addWidget(self.tools_get_china_ip)

        self.tools_remove_china_ip = QPushButton(self.tab_12)
        self.tools_remove_china_ip.setObjectName(u"tools_remove_china_ip")

        self.verticalLayout_3.addWidget(self.tools_remove_china_ip)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.tabWidget_2.addTab(self.tab_12, "")

        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget_4.setCurrentIndex(0)
        self.tabWidget_3.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"R-Knife", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"URL", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u5feb\u901f\u542f\u52a8", None))
        self.Result_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u7ed3\u679c\u4f1a\u663e\u793a\u5728\u6b64\u5904", None))
        self.Source_text.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u5728\u6b64\u5904\u8f93\u5165", None))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), QCoreApplication.translate("MainWindow", u"996", None))
        self.checkBox_line.setText(QCoreApplication.translate("MainWindow", u"\u6309\u884c\u5904\u7406", None))
        self.encode_type.setItemText(0, QCoreApplication.translate("MainWindow", u"UTF-8", None))
        self.encode_type.setItemText(1, QCoreApplication.translate("MainWindow", u"GBK", None))
        self.encode_type.setItemText(2, QCoreApplication.translate("MainWindow", u"GB2312", None))
        self.encode_type.setItemText(3, QCoreApplication.translate("MainWindow", u"GB18030", None))

        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.comboBox_encode.setItemText(0, QCoreApplication.translate("MainWindow", u"URL", None))
        self.comboBox_encode.setItemText(1, QCoreApplication.translate("MainWindow", u"Unicode", None))
        self.comboBox_encode.setItemText(2, QCoreApplication.translate("MainWindow", u"Escape_u", None))
        self.comboBox_encode.setItemText(3, QCoreApplication.translate("MainWindow", u"HTMLEncode", None))
        self.comboBox_encode.setItemText(4, QCoreApplication.translate("MainWindow", u"Base32", None))
        self.comboBox_encode.setItemText(5, QCoreApplication.translate("MainWindow", u"Base64", None))

        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.comboBox_decode.setItemText(0, QCoreApplication.translate("MainWindow", u"URL", None))
        self.comboBox_decode.setItemText(1, QCoreApplication.translate("MainWindow", u"Unicode", None))
        self.comboBox_decode.setItemText(2, QCoreApplication.translate("MainWindow", u"Escape_u", None))
        self.comboBox_decode.setItemText(3, QCoreApplication.translate("MainWindow", u"HTMLDecode", None))
        self.comboBox_decode.setItemText(4, QCoreApplication.translate("MainWindow", u"Base32", None))
        self.comboBox_decode.setItemText(5, QCoreApplication.translate("MainWindow", u"Base64", None))

        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5236", None))
        self.comboBox_jinzhi.setItemText(0, QCoreApplication.translate("MainWindow", u"2->8", None))
        self.comboBox_jinzhi.setItemText(1, QCoreApplication.translate("MainWindow", u"2->10", None))
        self.comboBox_jinzhi.setItemText(2, QCoreApplication.translate("MainWindow", u"2->16", None))
        self.comboBox_jinzhi.setItemText(3, QCoreApplication.translate("MainWindow", u"8->2", None))
        self.comboBox_jinzhi.setItemText(4, QCoreApplication.translate("MainWindow", u"8->10", None))
        self.comboBox_jinzhi.setItemText(5, QCoreApplication.translate("MainWindow", u"8->16", None))
        self.comboBox_jinzhi.setItemText(6, QCoreApplication.translate("MainWindow", u"10->2", None))
        self.comboBox_jinzhi.setItemText(7, QCoreApplication.translate("MainWindow", u"10->8", None))
        self.comboBox_jinzhi.setItemText(8, QCoreApplication.translate("MainWindow", u"10->16", None))
        self.comboBox_jinzhi.setItemText(9, QCoreApplication.translate("MainWindow", u"16->2", None))
        self.comboBox_jinzhi.setItemText(10, QCoreApplication.translate("MainWindow", u"16->8", None))
        self.comboBox_jinzhi.setItemText(11, QCoreApplication.translate("MainWindow", u"16->10", None))

        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u89e3\u7801", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u6536\u96c6\u8bbe\u5907\u7c7b\u578b", None))
        self.pushButton_morenpasswd_daochu.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa\u6570\u636e", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u5173\u952e\u5b57\uff1a", None))
        self.pushButton_morenpasswd_start.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        ___qtablewidgetitem = self.tableWidget_morenpasswd_result.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_morenpasswd_result.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u540d\u79f0", None));
        ___qtablewidgetitem2 = self.tableWidget_morenpasswd_result.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u540d", None));
        ___qtablewidgetitem3 = self.tableWidget_morenpasswd_result.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u9ed8\u8ba4\u5bc6\u7801", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"IP\u5730\u5740\uff1a", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u7aef\u53e3\uff1a", None))
        self.pushButton_re_go.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"\u53cd\u5411Shell\u751f\u6210", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"URL:", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u76ee\u6807\u6587\u4ef6\u540d\uff1a", None))
        self.pushButton_file_start.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u547d\u4ee4\u751f\u6210", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"tasklist /svc", None))
        self.pushButton_sharuanchaxun_start.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u6740\u8f6f", None))
        self.textEdit_sharuanchaxun_result.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u590d\u5236\u547d\u4ee4\u6267\u884c\u7ed3\u679c\u5728\u8fd9\u91cc", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"\u6740\u8f6f\u67e5\u8be2", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Windows\u63d0\u6743\u67e5\u8be2", None))
        self.pushButton_tiquanchaxun_start.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), QCoreApplication.translate("MainWindow", u"\u63d0\u6743\u67e5\u8be2", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u547d\u4ee4", None))
        self.radioButton_bash.setText(QCoreApplication.translate("MainWindow", u"Bash", None))
        self.radioButton_powershell.setText(QCoreApplication.translate("MainWindow", u"PowerShell", None))
        self.radioButton_python.setText(QCoreApplication.translate("MainWindow", u"Python", None))
        self.radioButton_perl.setText(QCoreApplication.translate("MainWindow", u"Perl", None))
        self.pushButton_copy.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236", None))
        self.pushButton_encode.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Java\u547d\u4ee4\u7f16\u7801", None))
        self.comboBox_sfzh_province.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u7701", None))
        self.comboBox_sfzh_city.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u5e02", None))
        self.comboBox_sfzh_area.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u53bf\uff08\u533a\uff09", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u6027\u522b", None))
        self.comboBox_sfzh_sex.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.comboBox_sfzh_sex.setItemText(1, QCoreApplication.translate("MainWindow", u"\u7537", None))
        self.comboBox_sfzh_sex.setItemText(2, QCoreApplication.translate("MainWindow", u"\u5973", None))

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u6761\u6570", None))
        self.checkBox_sfzh.setText(QCoreApplication.translate("MainWindow", u"\u53ea\u6253\u5370\u8eab\u4efd\u8bc1\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8eab\u4efd\u8bc1\u53f7", None))
        self.lineEdit_sfzh.setText(QCoreApplication.translate("MainWindow", u"******************", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u751f\u65e5", None))
        self.comboBox_sfzh_year.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.comboBox_sfzh_year.setItemText(1, QCoreApplication.translate("MainWindow", u"19", None))
        self.comboBox_sfzh_year.setItemText(2, QCoreApplication.translate("MainWindow", u"20", None))

        self.comboBox_sfzh_year_2.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u5e74", None))
        self.comboBox_sfzh_month.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))
        self.comboBox_sfzh_month.setItemText(1, QCoreApplication.translate("MainWindow", u"01", None))
        self.comboBox_sfzh_month.setItemText(2, QCoreApplication.translate("MainWindow", u"02", None))
        self.comboBox_sfzh_month.setItemText(3, QCoreApplication.translate("MainWindow", u"03", None))
        self.comboBox_sfzh_month.setItemText(4, QCoreApplication.translate("MainWindow", u"04", None))
        self.comboBox_sfzh_month.setItemText(5, QCoreApplication.translate("MainWindow", u"05", None))
        self.comboBox_sfzh_month.setItemText(6, QCoreApplication.translate("MainWindow", u"06", None))
        self.comboBox_sfzh_month.setItemText(7, QCoreApplication.translate("MainWindow", u"07", None))
        self.comboBox_sfzh_month.setItemText(8, QCoreApplication.translate("MainWindow", u"08", None))
        self.comboBox_sfzh_month.setItemText(9, QCoreApplication.translate("MainWindow", u"09", None))
        self.comboBox_sfzh_month.setItemText(10, QCoreApplication.translate("MainWindow", u"10", None))
        self.comboBox_sfzh_month.setItemText(11, QCoreApplication.translate("MainWindow", u"11", None))
        self.comboBox_sfzh_month.setItemText(12, QCoreApplication.translate("MainWindow", u"12", None))

        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u6708", None))
        self.comboBox_sfzh_day.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u65e5", None))
        self.pushButton_sfzh_go.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_9), QCoreApplication.translate("MainWindow", u"SFZH\u751f\u6210", None))
        self.comboBox_phone_province.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u7701", None))
        self.comboBox_phone_city.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u5e02", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u8fd0\u8425\u5546", None))
        self.comboBox_phone_operator.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u53f7\u6bb5", None))
        self.comboBox_phone_number.setItemText(0, QCoreApplication.translate("MainWindow", u"\u968f\u673a", None))

        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u6761\u6570", None))
        self.checkBox_phone_num.setText(QCoreApplication.translate("MainWindow", u"\u53ea\u6253\u5370\u624b\u673a\u53f7", None))
        self.pushButton_phone_go.setText(QCoreApplication.translate("MainWindow", u"\u751f\u6210", None))
        self.pushButton_phone_number.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u6570\u5b57", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u7ed3\u675f\u6570\u5b57", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7\u7801\u5f52\u5c5e\u5730\u67e5\u8be2", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_11), QCoreApplication.translate("MainWindow", u"\u624b\u673a\u53f7\u751f\u6210", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"\u8d26\u53f7\u751f\u6210", None))
        self.tools_source.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u6587\u672c", None))
        self.tools_daoxu.setText(QCoreApplication.translate("MainWindow", u"\u5012\u5e8f\u8f93\u51fa", None))
        self.tools_xiaoxie.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5c0f\u5199", None))
        self.tool_daxie.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5927\u5199", None))
        self.tools_remove_duplicate.setText(QCoreApplication.translate("MainWindow", u"\u53bb\u9664\u91cd\u590d\u9879", None))
        self.tools_zhongwen_pinyin.setText(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u8f6c\u62fc\u97f3", None))
        self.tools_tiqushouzimu.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u9996\u5b57\u6bcd", None))
        self.tools_get_ip.setText(QCoreApplication.translate("MainWindow", u"\u6b63\u5219\u63d0\u53d6IP", None))
        self.tools_ip.setText(QCoreApplication.translate("MainWindow", u"IP\u5f52\u5c5e\u67e5\u8be2", None))
        self.tools_get_china_ip.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u56fd\u5185IP", None))
        self.tools_remove_china_ip.setText(QCoreApplication.translate("MainWindow", u"\u63d0\u53d6\u56fd\u5916IP", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), QCoreApplication.translate("MainWindow", u"\u5c0f\u5de5\u5177", None))
    # retranslateUi

