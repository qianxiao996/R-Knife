# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(874, 644)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(200, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.label_3 = QtWidgets.QLabel(self.tab_3)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_3)
        self.lineEdit_3.setMaximumSize(QtCore.QSize(70, 25))
        self.lineEdit_3.setMaxLength(5)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.tab_3)
        self.tabWidget.setObjectName("tabWidget")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.checkBox_line = QtWidgets.QCheckBox(self.tab_5)
        self.checkBox_line.setMaximumSize(QtCore.QSize(100, 16777215))
        self.checkBox_line.setObjectName("checkBox_line")
        self.horizontalLayout_8.addWidget(self.checkBox_line)
        self.encode_type = QtWidgets.QComboBox(self.tab_5)
        self.encode_type.setMaximumSize(QtCore.QSize(100, 16777215))
        self.encode_type.setObjectName("encode_type")
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.encode_type.addItem("")
        self.horizontalLayout_8.addWidget(self.encode_type)
        self.label_12 = QtWidgets.QLabel(self.tab_5)
        self.label_12.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.comboBox_encode = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_encode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_encode.setObjectName("comboBox_encode")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.comboBox_encode.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_encode)
        self.label_11 = QtWidgets.QLabel(self.tab_5)
        self.label_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_8.addWidget(self.label_11)
        self.comboBox_decode = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_decode.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_decode.setObjectName("comboBox_decode")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.comboBox_decode.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox_decode)
        self.label_13 = QtWidgets.QLabel(self.tab_5)
        self.label_13.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_8.addWidget(self.label_13)
        self.comboBox_jinzhi = QtWidgets.QComboBox(self.tab_5)
        self.comboBox_jinzhi.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.comboBox_jinzhi.setObjectName("comboBox_jinzhi")
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
        self.horizontalLayout_8.addWidget(self.comboBox_jinzhi)
        self.gridLayout_6.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.zhuanyuan = QtWidgets.QPushButton(self.tab_5)
        self.zhuanyuan.setMinimumSize(QtCore.QSize(100, 0))
        self.zhuanyuan.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.zhuanyuan.setStyleSheet("")
        self.zhuanyuan.setObjectName("zhuanyuan")
        self.horizontalLayout_9.addWidget(self.zhuanyuan)
        self.Result_Copy_Button = QtWidgets.QPushButton(self.tab_5)
        self.Result_Copy_Button.setMinimumSize(QtCore.QSize(100, 0))
        self.Result_Copy_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Result_Copy_Button.setStyleSheet("")
        self.Result_Copy_Button.setObjectName("Result_Copy_Button")
        self.horizontalLayout_9.addWidget(self.Result_Copy_Button)
        self.tab_add = QtWidgets.QPushButton(self.tab_5)
        self.tab_add.setMinimumSize(QtCore.QSize(100, 0))
        self.tab_add.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab_add.setStyleSheet("")
        self.tab_add.setObjectName("tab_add")
        self.horizontalLayout_9.addWidget(self.tab_add)
        self.Source_clear_Button = QtWidgets.QPushButton(self.tab_5)
        self.Source_clear_Button.setMinimumSize(QtCore.QSize(100, 0))
        self.Source_clear_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Source_clear_Button.setStyleSheet("")
        self.Source_clear_Button.setObjectName("Source_clear_Button")
        self.horizontalLayout_9.addWidget(self.Source_clear_Button)
        self.Source_Paste_Button = QtWidgets.QPushButton(self.tab_5)
        self.Source_Paste_Button.setMinimumSize(QtCore.QSize(100, 0))
        self.Source_Paste_Button.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.Source_Paste_Button.setStyleSheet("")
        self.Source_Paste_Button.setObjectName("Source_Paste_Button")
        self.horizontalLayout_9.addWidget(self.Source_Paste_Button)
        self.gridLayout_6.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)
        self.tabWidget_4 = QtWidgets.QTabWidget(self.tab_5)
        self.tabWidget_4.setDocumentMode(False)
        self.tabWidget_4.setTabsClosable(True)
        self.tabWidget_4.setObjectName("tabWidget_4")
        self.tab_10 = QtWidgets.QWidget()
        self.tab_10.setObjectName("tab_10")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.tab_10)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.Result_text = QtWidgets.QPlainTextEdit(self.tab_10)
        self.Result_text.setObjectName("Result_text")
        self.gridLayout_11.addWidget(self.Result_text, 1, 0, 1, 1)
        self.Source_text = QtWidgets.QPlainTextEdit(self.tab_10)
        self.Source_text.setObjectName("Source_text")
        self.gridLayout_11.addWidget(self.Source_text, 0, 0, 1, 1)
        self.tabWidget_4.addTab(self.tab_10, "")
        self.gridLayout_6.addWidget(self.tabWidget_4, 2, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_54 = QtWidgets.QLabel(self.tab_4)
        self.label_54.setMinimumSize(QtCore.QSize(0, 28))
        self.label_54.setMaximumSize(QtCore.QSize(400, 16777215))
        self.label_54.setObjectName("label_54")
        self.horizontalLayout_6.addWidget(self.label_54)
        self.pushButton_morenpasswd_daochu = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_morenpasswd_daochu.setMaximumSize(QtCore.QSize(100, 16777215))
        self.pushButton_morenpasswd_daochu.setObjectName("pushButton_morenpasswd_daochu")
        self.horizontalLayout_6.addWidget(self.pushButton_morenpasswd_daochu)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_41 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_41.setObjectName("horizontalLayout_41")
        self.label_47 = QtWidgets.QLabel(self.tab_4)
        self.label_47.setObjectName("label_47")
        self.horizontalLayout_41.addWidget(self.label_47)
        self.lineEdit_select_data = QtWidgets.QLineEdit(self.tab_4)
        self.lineEdit_select_data.setObjectName("lineEdit_select_data")
        self.horizontalLayout_41.addWidget(self.lineEdit_select_data)
        self.pushButton_morenpasswd_start = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_morenpasswd_start.setObjectName("pushButton_morenpasswd_start")
        self.horizontalLayout_41.addWidget(self.pushButton_morenpasswd_start)
        self.gridLayout.addLayout(self.horizontalLayout_41, 0, 1, 1, 1)
        self.listWidget_morenpasswd_list = QtWidgets.QListWidget(self.tab_4)
        self.listWidget_morenpasswd_list.setMinimumSize(QtCore.QSize(250, 0))
        self.listWidget_morenpasswd_list.setMaximumSize(QtCore.QSize(500, 16777215))
        self.listWidget_morenpasswd_list.setObjectName("listWidget_morenpasswd_list")
        self.gridLayout.addWidget(self.listWidget_morenpasswd_list, 1, 0, 1, 1)
        self.tableWidget_morenpasswd_result = QtWidgets.QTableWidget(self.tab_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget_morenpasswd_result.sizePolicy().hasHeightForWidth())
        self.tableWidget_morenpasswd_result.setSizePolicy(sizePolicy)
        self.tableWidget_morenpasswd_result.setMinimumSize(QtCore.QSize(500, 0))
        self.tableWidget_morenpasswd_result.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tableWidget_morenpasswd_result.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_morenpasswd_result.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_morenpasswd_result.setObjectName("tableWidget_morenpasswd_result")
        self.tableWidget_morenpasswd_result.setColumnCount(4)
        self.tableWidget_morenpasswd_result.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_morenpasswd_result.setHorizontalHeaderItem(3, item)
        self.tableWidget_morenpasswd_result.horizontalHeader().setVisible(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_morenpasswd_result.horizontalHeader().setDefaultSectionSize(60)
        self.tableWidget_morenpasswd_result.horizontalHeader().setHighlightSections(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setMinimumSectionSize(25)
        self.tableWidget_morenpasswd_result.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget_morenpasswd_result.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_morenpasswd_result.verticalHeader().setVisible(False)
        self.tableWidget_morenpasswd_result.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_morenpasswd_result.verticalHeader().setDefaultSectionSize(30)
        self.tableWidget_morenpasswd_result.verticalHeader().setHighlightSections(True)
        self.tableWidget_morenpasswd_result.verticalHeader().setMinimumSectionSize(23)
        self.tableWidget_morenpasswd_result.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_morenpasswd_result.verticalHeader().setStretchLastSection(False)
        self.gridLayout.addWidget(self.tableWidget_morenpasswd_result, 1, 1, 1, 1)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_6 = QtWidgets.QWidget()
        self.tab_6.setObjectName("tab_6")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_6)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_57 = QtWidgets.QGridLayout()
        self.gridLayout_57.setObjectName("gridLayout_57")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_24 = QtWidgets.QLabel(self.tab_6)
        self.label_24.setObjectName("label_24")
        self.horizontalLayout_7.addWidget(self.label_24)
        self.lineEdit_cmd_ip = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_cmd_ip.setObjectName("lineEdit_cmd_ip")
        self.horizontalLayout_7.addWidget(self.lineEdit_cmd_ip)
        self.label_30 = QtWidgets.QLabel(self.tab_6)
        self.label_30.setObjectName("label_30")
        self.horizontalLayout_7.addWidget(self.label_30)
        self.lineEdit_cmd_port = QtWidgets.QLineEdit(self.tab_6)
        self.lineEdit_cmd_port.setObjectName("lineEdit_cmd_port")
        self.horizontalLayout_7.addWidget(self.lineEdit_cmd_port)
        self.pushButton_re_go = QtWidgets.QPushButton(self.tab_6)
        self.pushButton_re_go.setObjectName("pushButton_re_go")
        self.horizontalLayout_7.addWidget(self.pushButton_re_go)
        self.gridLayout_57.addLayout(self.horizontalLayout_7, 0, 0, 1, 1)
        self.textEdit_cmd_result = QtWidgets.QTextEdit(self.tab_6)
        self.textEdit_cmd_result.setObjectName("textEdit_cmd_result")
        self.gridLayout_57.addWidget(self.textEdit_cmd_result, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_57, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_6, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_10.addWidget(self.label_25)
        self.lineEdit_file_url = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_file_url.setObjectName("lineEdit_file_url")
        self.horizontalLayout_10.addWidget(self.lineEdit_file_url)
        self.label_31 = QtWidgets.QLabel(self.tab_2)
        self.label_31.setObjectName("label_31")
        self.horizontalLayout_10.addWidget(self.label_31)
        self.lineEdit_file_dest_name = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_file_dest_name.setObjectName("lineEdit_file_dest_name")
        self.horizontalLayout_10.addWidget(self.lineEdit_file_dest_name)
        self.pushButton_file_start = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_file_start.setObjectName("pushButton_file_start")
        self.horizontalLayout_10.addWidget(self.pushButton_file_start)
        self.gridLayout_8.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.textEdit_file_result = QtWidgets.QTextEdit(self.tab_2)
        self.textEdit_file_result.setObjectName("textEdit_file_result")
        self.gridLayout_8.addWidget(self.textEdit_file_result, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_2, "")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.tab_8)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_51 = QtWidgets.QLabel(self.tab_8)
        self.label_51.setMinimumSize(QtCore.QSize(0, 0))
        self.label_51.setObjectName("label_51")
        self.horizontalLayout_2.addWidget(self.label_51)
        self.pushButton_sharuanchaxun_start = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_sharuanchaxun_start.setMaximumSize(QtCore.QSize(150, 16777215))
        self.pushButton_sharuanchaxun_start.setObjectName("pushButton_sharuanchaxun_start")
        self.horizontalLayout_2.addWidget(self.pushButton_sharuanchaxun_start)
        self.gridLayout_7.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.textEdit_sharuanchaxun_result = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit_sharuanchaxun_result.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_sharuanchaxun_result.setObjectName("textEdit_sharuanchaxun_result")
        self.gridLayout_7.addWidget(self.textEdit_sharuanchaxun_result, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_8, "")
        self.tab_13 = QtWidgets.QWidget()
        self.tab_13.setObjectName("tab_13")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.tab_13)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.tab_13)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.pushButton_tiquanchaxun_start = QtWidgets.QPushButton(self.tab_13)
        self.pushButton_tiquanchaxun_start.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton_tiquanchaxun_start.setObjectName("pushButton_tiquanchaxun_start")
        self.horizontalLayout_4.addWidget(self.pushButton_tiquanchaxun_start)
        self.gridLayout_10.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.textEdit_tiquanchaxun_result = QtWidgets.QTextEdit(self.tab_13)
        self.textEdit_tiquanchaxun_result.setMinimumSize(QtCore.QSize(0, 0))
        self.textEdit_tiquanchaxun_result.setObjectName("textEdit_tiquanchaxun_result")
        self.gridLayout_10.addWidget(self.textEdit_tiquanchaxun_result, 1, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_13, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.radioButton_bash = QtWidgets.QRadioButton(self.tab)
        self.radioButton_bash.setChecked(True)
        self.radioButton_bash.setObjectName("radioButton_bash")
        self.horizontalLayout_5.addWidget(self.radioButton_bash)
        self.radioButton_powershell = QtWidgets.QRadioButton(self.tab)
        self.radioButton_powershell.setObjectName("radioButton_powershell")
        self.horizontalLayout_5.addWidget(self.radioButton_powershell)
        self.radioButton_python = QtWidgets.QRadioButton(self.tab)
        self.radioButton_python.setObjectName("radioButton_python")
        self.horizontalLayout_5.addWidget(self.radioButton_python)
        self.radioButton_perl = QtWidgets.QRadioButton(self.tab)
        self.radioButton_perl.setObjectName("radioButton_perl")
        self.horizontalLayout_5.addWidget(self.radioButton_perl)
        self.pushButton_copy = QtWidgets.QPushButton(self.tab)
        self.pushButton_copy.setObjectName("pushButton_copy")
        self.horizontalLayout_5.addWidget(self.pushButton_copy)
        self.pushButton_encode = QtWidgets.QPushButton(self.tab)
        self.pushButton_encode.setObjectName("pushButton_encode")
        self.horizontalLayout_5.addWidget(self.pushButton_encode)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.textEdit_java_result = QtWidgets.QTextEdit(self.tab)
        self.textEdit_java_result.setObjectName("textEdit_java_result")
        self.verticalLayout_2.addWidget(self.textEdit_java_result)
        self.gridLayout_5.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab, "")
        self.tab_12 = QtWidgets.QWidget()
        self.tab_12.setObjectName("tab_12")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_12)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tools_source = QtWidgets.QPlainTextEdit(self.tab_12)
        self.tools_source.setObjectName("tools_source")
        self.horizontalLayout_3.addWidget(self.tools_source)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tools_daoxu = QtWidgets.QPushButton(self.tab_12)
        self.tools_daoxu.setObjectName("tools_daoxu")
        self.verticalLayout_3.addWidget(self.tools_daoxu)
        self.tools_xiaoxie = QtWidgets.QPushButton(self.tab_12)
        self.tools_xiaoxie.setObjectName("tools_xiaoxie")
        self.verticalLayout_3.addWidget(self.tools_xiaoxie)
        self.tool_daxie = QtWidgets.QPushButton(self.tab_12)
        self.tool_daxie.setObjectName("tool_daxie")
        self.verticalLayout_3.addWidget(self.tool_daxie)
        self.tools_remove_duplicate = QtWidgets.QPushButton(self.tab_12)
        self.tools_remove_duplicate.setObjectName("tools_remove_duplicate")
        self.verticalLayout_3.addWidget(self.tools_remove_duplicate)
        self.tools_zhongwen_pinyin = QtWidgets.QPushButton(self.tab_12)
        self.tools_zhongwen_pinyin.setObjectName("tools_zhongwen_pinyin")
        self.verticalLayout_3.addWidget(self.tools_zhongwen_pinyin)
        self.tools_tiqushouzimu = QtWidgets.QPushButton(self.tab_12)
        self.tools_tiqushouzimu.setObjectName("tools_tiqushouzimu")
        self.verticalLayout_3.addWidget(self.tools_tiqushouzimu)
        self.tools_get_ip = QtWidgets.QPushButton(self.tab_12)
        self.tools_get_ip.setObjectName("tools_get_ip")
        self.verticalLayout_3.addWidget(self.tools_get_ip)
        self.tools_ip = QtWidgets.QPushButton(self.tab_12)
        self.tools_ip.setObjectName("tools_ip")
        self.verticalLayout_3.addWidget(self.tools_ip)
        self.tools_get_china_ip = QtWidgets.QPushButton(self.tab_12)
        self.tools_get_china_ip.setObjectName("tools_get_china_ip")
        self.verticalLayout_3.addWidget(self.tools_get_china_ip)
        self.tools_remove_china_ip = QtWidgets.QPushButton(self.tab_12)
        self.tools_remove_china_ip.setObjectName("tools_remove_china_ip")
        self.verticalLayout_3.addWidget(self.tools_remove_china_ip)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout_9.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.tabWidget_2.addTab(self.tab_12, "")
        self.gridLayout_2.addWidget(self.tabWidget_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget_4.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI Tools"))
        self.label.setText(_translate("MainWindow", "URL"))
        self.label_2.setText(_translate("MainWindow", "IP地址"))
        self.label_3.setText(_translate("MainWindow", "端口"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "快速启动"))
        self.checkBox_line.setText(_translate("MainWindow", "按行处理"))
        self.encode_type.setItemText(0, _translate("MainWindow", "UTF-8"))
        self.encode_type.setItemText(1, _translate("MainWindow", "GBK"))
        self.encode_type.setItemText(2, _translate("MainWindow", "GB2312"))
        self.encode_type.setItemText(3, _translate("MainWindow", "GB18030"))
        self.label_12.setText(_translate("MainWindow", "编码"))
        self.comboBox_encode.setItemText(0, _translate("MainWindow", "URL"))
        self.comboBox_encode.setItemText(1, _translate("MainWindow", "Unicode"))
        self.comboBox_encode.setItemText(2, _translate("MainWindow", "Escape_u"))
        self.comboBox_encode.setItemText(3, _translate("MainWindow", "HTMLEncode"))
        self.comboBox_encode.setItemText(4, _translate("MainWindow", "Base32"))
        self.comboBox_encode.setItemText(5, _translate("MainWindow", "Base64"))
        self.label_11.setText(_translate("MainWindow", "解码"))
        self.comboBox_decode.setItemText(0, _translate("MainWindow", "URL"))
        self.comboBox_decode.setItemText(1, _translate("MainWindow", "Unicode"))
        self.comboBox_decode.setItemText(2, _translate("MainWindow", "Escape_u"))
        self.comboBox_decode.setItemText(3, _translate("MainWindow", "HTMLDecode"))
        self.comboBox_decode.setItemText(4, _translate("MainWindow", "Base32"))
        self.comboBox_decode.setItemText(5, _translate("MainWindow", "Base64"))
        self.label_13.setText(_translate("MainWindow", "进制"))
        self.comboBox_jinzhi.setItemText(0, _translate("MainWindow", "2->8"))
        self.comboBox_jinzhi.setItemText(1, _translate("MainWindow", "2->10"))
        self.comboBox_jinzhi.setItemText(2, _translate("MainWindow", "2->16"))
        self.comboBox_jinzhi.setItemText(3, _translate("MainWindow", "8->2"))
        self.comboBox_jinzhi.setItemText(4, _translate("MainWindow", "8->10"))
        self.comboBox_jinzhi.setItemText(5, _translate("MainWindow", "8->16"))
        self.comboBox_jinzhi.setItemText(6, _translate("MainWindow", "10->2"))
        self.comboBox_jinzhi.setItemText(7, _translate("MainWindow", "10->8"))
        self.comboBox_jinzhi.setItemText(8, _translate("MainWindow", "10->16"))
        self.comboBox_jinzhi.setItemText(9, _translate("MainWindow", "16->2"))
        self.comboBox_jinzhi.setItemText(10, _translate("MainWindow", "16->8"))
        self.comboBox_jinzhi.setItemText(11, _translate("MainWindow", "16->10"))
        self.zhuanyuan.setText(_translate("MainWindow", "转源文本"))
        self.Result_Copy_Button.setText(_translate("MainWindow", "复制结果"))
        self.tab_add.setText(_translate("MainWindow", "增加tab"))
        self.Source_clear_Button.setText(_translate("MainWindow", "清空文本"))
        self.Source_Paste_Button.setText(_translate("MainWindow", "粘贴密文"))
        self.Result_text.setPlaceholderText(_translate("MainWindow", "结果会显示在此处"))
        self.Source_text.setPlaceholderText(_translate("MainWindow", "请在此处输入"))
        self.tabWidget_4.setTabText(self.tabWidget_4.indexOf(self.tab_10), _translate("MainWindow", "996"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "编码解码"))
        self.label_54.setText(_translate("MainWindow", "已收集设备类型"))
        self.pushButton_morenpasswd_daochu.setText(_translate("MainWindow", "导出数据"))
        self.label_47.setText(_translate("MainWindow", "设备关键字："))
        self.pushButton_morenpasswd_start.setText(_translate("MainWindow", "查询"))
        self.tableWidget_morenpasswd_result.setSortingEnabled(True)
        item = self.tableWidget_morenpasswd_result.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget_morenpasswd_result.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "设备名称"))
        item = self.tableWidget_morenpasswd_result.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "用户名"))
        item = self.tableWidget_morenpasswd_result.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "密码"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "默认密码"))
        self.label_24.setText(_translate("MainWindow", "IP地址："))
        self.label_30.setText(_translate("MainWindow", "端口："))
        self.pushButton_re_go.setText(_translate("MainWindow", "生成"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_6), _translate("MainWindow", "反向Shell生成"))
        self.label_25.setText(_translate("MainWindow", "URL:"))
        self.label_31.setText(_translate("MainWindow", "目标文件名："))
        self.pushButton_file_start.setText(_translate("MainWindow", "生成"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), _translate("MainWindow", "下载命令生成"))
        self.label_51.setText(_translate("MainWindow", "tasklist /svc"))
        self.pushButton_sharuanchaxun_start.setText(_translate("MainWindow", "查询杀软"))
        self.textEdit_sharuanchaxun_result.setPlaceholderText(_translate("MainWindow", "请复制命令执行结果在这里"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_8), _translate("MainWindow", "杀软查询"))
        self.label_4.setText(_translate("MainWindow", "Windows提权查询"))
        self.pushButton_tiquanchaxun_start.setText(_translate("MainWindow", "查询"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_13), _translate("MainWindow", "提权查询"))
        self.label_5.setText(_translate("MainWindow", "命令"))
        self.radioButton_bash.setText(_translate("MainWindow", "Bash"))
        self.radioButton_powershell.setText(_translate("MainWindow", "PowerShell"))
        self.radioButton_python.setText(_translate("MainWindow", "Python"))
        self.radioButton_perl.setText(_translate("MainWindow", "Perl"))
        self.pushButton_copy.setText(_translate("MainWindow", "复制"))
        self.pushButton_encode.setText(_translate("MainWindow", "编码"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab), _translate("MainWindow", "Java命令编码"))
        self.tools_source.setPlaceholderText(_translate("MainWindow", "请输入文本"))
        self.tools_daoxu.setText(_translate("MainWindow", "倒序输出"))
        self.tools_xiaoxie.setText(_translate("MainWindow", "全小写"))
        self.tool_daxie.setText(_translate("MainWindow", "全大写"))
        self.tools_remove_duplicate.setText(_translate("MainWindow", "去除重复项"))
        self.tools_zhongwen_pinyin.setText(_translate("MainWindow", "中文转拼音"))
        self.tools_tiqushouzimu.setText(_translate("MainWindow", "提取首字母"))
        self.tools_get_ip.setText(_translate("MainWindow", "正则提取IP"))
        self.tools_ip.setText(_translate("MainWindow", "IP归属查询"))
        self.tools_get_china_ip.setText(_translate("MainWindow", "提取国内IP"))
        self.tools_remove_china_ip.setText(_translate("MainWindow", "提取国外IP"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_12), _translate("MainWindow", "小工具"))
