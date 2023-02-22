#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser
import json,base64
import os,re
import subprocess
import sys,csv
import random,time
from PyQt5.QtGui import QMouseEvent
from  PyQt5.Qt import QCursor
from urllib.parse import urlparse
import pyperclip
import qdarkstyle
from qdarkstyle import LightPalette
from qt_material import apply_stylesheet

from PyQt5.QtGui import QPixmap,QMovie
from module.Tools_Start import Tools_Start

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import requests,sqlite3
from Gui.main import Ui_MainWindow
import frozen_dir
from module.func_binary import Class_Binary
from module.func_decode import Class_Decode
from module.func_encode import Class_Encode


SETUP_DIR = frozen_dir.app_path()
sys.path.append(SETUP_DIR)
version = '1.0'
config_file_dir = './Conf/config.ini'
update_time = '20230222'
DB_NAME = './Conf/DB.db'
requests.packages.urllib3.disable_warnings()

class MainWindows(QtWidgets.QMainWindow):  # 主窗口
    def __init__(self, parent=None):
        super(MainWindows, self).__init__(parent)
        self.Ui = Ui_MainWindow()
        self.Ui.setupUi(self)
        self.setWindowTitle('R-Knife v' + version + ' ' + update_time)
        self.setWindowIcon(QtGui.QIcon('Conf/logo.ico'))
        self.Ui.lineEdit.editingFinished.connect(self.split_url)
        self.load_config()
        self.load_button()
        self.generate_shell()
        self.generate_file_shell()
        self.Ui.tab_add.clicked.connect(self.add_Tab)  # 添加tab
        desktop = QApplication.desktop()
        # print(desktop.width(),desktop.height())
        self.x=desktop.width()-200
        # self.y=desktop.height()-(desktop.height()-100)
        self.y=desktop.height()-300

        #编码解码
        self.Ui.tabWidget_4.tabCloseRequested.connect(self.closeTab)
        self.Ui.tabWidget_4.currentChanged.connect(self.onCurrentChanged)
        self.Ui.tabWidget_4.tabBar().installEventFilter(self)
        self.Ui.tabWidget_4.tabBar().previousMiddleIndex = -1
        self.Ui.Source_Paste_Button.clicked.connect(lambda: self.paste('Source'))  # paste_Source
        self.Ui.Source_clear_Button.clicked.connect(lambda: self.Ui.Source_text.clear())  # clear_source
        self.Ui.Result_Copy_Button.clicked.connect(lambda: self.Copy_text( self.Ui.Result_text.toPlainText()))  # copy_result
        self.Ui.zhuanyuan.clicked.connect(self.zhuan_yuanwenben)  # paste_result

        self.Ui.comboBox_encode.activated[str].connect(lambda:self.gogogo(self.Ui.comboBox_encode.currentText()))
        self.Ui.comboBox_decode.activated[str].connect(lambda:self.gogogo(self.Ui.comboBox_decode.currentText(),"Decode"))
        self.Ui.comboBox_jinzhi.activated[str].connect(lambda:self.Binary_gogogo(self.Ui.comboBox_jinzhi.currentText()))

        #默认设备密码
        self.load_morepasswd()
        # self.Ui.tableWidget_morenpasswd_result.setVisible(False)
        self.Ui.tableWidget_morenpasswd_result.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(0)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(1)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(2)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(3)
        # self.Ui.tableWidget_morenpasswd_result.setVisible(True)
        self.Ui.listWidget_morenpasswd_list.clicked.connect(self.change_morenpasswd_click_value)
        # self.Ui.pushButton_morenpasswd_username_copy.clicked.connect(lambda :self.Copy_text(self.Ui.textEdit_morenpasswd_username.toPlainText()))
        # self.Ui.pushButton_pushButton_morenpasswd_passwd_copy.clicked.connect(lambda :self.Copy_text(self.Ui.textEdit_morenpasswd_passwd.toPlainText()))
        self.Ui.pushButton_morenpasswd_daochu.clicked.connect(lambda: self.export_file(self.Ui.tableWidget_morenpasswd_result, ''))
        self.Ui.pushButton_morenpasswd_start.clicked.connect(self.morenpasswd_start)
        # self.Ui.portscan_result.setColumnWidth(-1, 30)


        #命令生成

        self.Ui.pushButton_re_go.clicked.connect(self.generate_shell)
        self.Ui.pushButton_file_start.clicked.connect(self.generate_file_shell)

        #杀软查询
        self.Ui.pushButton_sharuanchaxun_start.clicked.connect(self.sharuanchaxun_start)


        #提权查询
        self.Ui.pushButton_tiquanchaxun_start.clicked.connect(self.tiquanchaxun_start)

        #java编码
        self.Ui.pushButton_copy.clicked.connect(lambda: self.Copy_text(self.Ui.textEdit_java_result.toPlainText()))  # copy_source
        self.Ui.pushButton_encode.clicked.connect(self.java_encode)


        #小工具
        self.Ui.tools_ip.clicked.connect(lambda :self.tools("ipsearch"))
        self.Ui.tool_daxie.clicked.connect(lambda :self.tools("alldaxie"))
        self.Ui.tools_xiaoxie.clicked.connect(lambda :self.tools("allxiaoxie"))
        self.Ui.tools_daoxu.clicked.connect(lambda :self.tools("daoxu"))
        self.Ui.tools_zhongwen_pinyin.clicked.connect(lambda :self.tools("zhongwen_pinyin"))
        self.Ui.tools_tiqushouzimu.clicked.connect(lambda :self.tools("tiqushouzimu"))

        self.Ui.tools_remove_duplicate.clicked.connect(lambda :self.tools("remove_duplicate"))
        self.Ui.tools_get_ip.clicked.connect(lambda :self.tools("get_ip"))
        self.Ui.tools_get_china_ip.clicked.connect(lambda :self.tools("get_china_ip"))
        self.Ui.tools_remove_china_ip.clicked.connect(lambda :self.tools("remove_china_ip"))

    def java_encode(self):
        _text =self.Ui.textEdit_java_result.toPlainText().encode()
        box = QtWidgets.QMessageBox()
        base64_str = base64.b64encode(_text).decode()
        if not _text:
            box.warning(self, "提示",'请输入命令!')
            return
        if self.Ui.radioButton_bash.isChecked():
            _text = 'bash -c {echo,' + base64_str + '}|{base64,-d}|{bash,-i}';
        elif self.Ui.radioButton_powershell.isChecked():
            _text = 'powershell.exe -NonI -W Hidden -NoP -Exec Bypass -Enc ' + base64_str
        elif self.Ui.radioButton_python.isChecked():
            _text = "python -c exec('" + base64_str + "'.decode('base64'))";
        elif self.Ui.radioButton_perl.isChecked():
            _text = "perl -MMIME::Base64 -e eval(decode_base64('" + base64_str + "'))";
        else:
            box.warning(self, "提示",'请选择编码方式!')
        self.Ui.textEdit_java_result.setPlainText(_text)
    def tools(self,type):
        tools_source = self.Ui.tools_source.toPlainText()
        if tools_source:
            self.tools_obj = Tools_Start(tools_source,type )  # 创建一个线程
            self.tools_obj._data.connect(self.update_data_tools)  # 线程发过来的信号挂接到槽函数update_sum
            self.Ui.tools_source.clear()
            self.tools_obj.start()  # 线程启动
    def update_data_tools(self,data):
        self.Ui.tools_source.appendPlainText(data)

    def sharuanchaxun_start(self):
        res_text =self.Ui.textEdit_sharuanchaxun_result.toPlainText()
        if res_text=='':
            self.Ui.textEdit_sharuanchaxun_result.append("请输入数据！")
            return
        re_data_list = re.findall(r'(\w+)\.exe',res_text)
        sql_poc = "SELECT distinct * from av where av_name !=''"
        av_data_dict = self.sql_search(sql_poc,'dict')
        result=[]
        self.Ui.textEdit_sharuanchaxun_result.clear()
        for exe in re_data_list:
            for av_exe in av_data_dict:
                if exe+'.exe' == av_exe['av_exe']:
                    result.append(av_exe['av_name'])
                    self.Ui.textEdit_sharuanchaxun_result.append(av_exe['av_exe']+"----"+av_exe['av_name'])
        if len(result)==0:
            self.Ui.textEdit_sharuanchaxun_result.append("未查询到杀软信息！")
    def tiquanchaxun_start(self):
        res_text =self.Ui.textEdit_tiquanchaxun_result.toPlainText()
        if res_text=='':
            self.Ui.textEdit_tiquanchaxun_result.append("请输入数据！")
            return
        # system_os_version = re.findall(r'OS 名称:.*',res_text).replace("OS 名称:","")
        # re_data_list = re.findall(r'/KB[0-9]{7}/',res_text)
        re_data_list = re.findall(r'\[\d+]\:\W(KB.*)',res_text)
        sql_poc = "SELECT distinct * from Privilege_Exploit where kb !=''"
        _data_dict = self.sql_search(sql_poc,'dict')
        result=[]
        self.Ui.textEdit_tiquanchaxun_result.clear()
        result_str ='可能利用的EXP如下：<br><br>'
        for i in _data_dict:
            if i['kb'] not in re_data_list:
                result.append(i)
                result_str += '''<a style="color:green">Title:</a>%s<br><a style="color:green">Bulletin Id:</a>%s<a style="color:green"><br>Operating System:</a>%s<a style="color:green"><br>CVEs:</a>%s<hr style="background-color:pink;height:1px; border:none;"/>'''%(i.get('Title'),i.get('Bulletin_Id'),i.get('system'),i.get('CVES'))
        self.Ui.textEdit_tiquanchaxun_result.setHtml(result_str)
        if len(result)==0:
            self.Ui.textEdit_tiquanchaxun_result.setHtml("未查询到EXP信息！")
        # self.set_morenpasswd_table_value(passwd_list)
    def load_morepasswd(self):
        sql_poc = "SELECT distinct type from passwd where type !=''"
        passwd_type_list = self.sql_search(sql_poc)
        passwd_type_list = self.sql_search(sql_poc)
        # print(passwd_type_list)
        for type in passwd_type_list:
            self.Ui.listWidget_morenpasswd_list.addItem(str(type[0].strip()))
    def generate_shell(self):
        ip = self.Ui.lineEdit_cmd_ip.text()
        port = self.Ui.lineEdit_cmd_port.text()
        sql ="select * from cmd where type ='shell'"
        sql_result = self.sql_search(sql,'dict')
        data=''
        if sql_result:
            for i in sql_result:
                if ip and port:
                    data +="<p style=\"color:green\">"+i['name']+"</p>"+i['value'].replace('127.0.0.1',ip).replace('8888',port)+'<br><hr style="background-color:pink;height:1px; border:none;"/>'
                else:
                    data +="<p style=\"color:green\">"+i['name']+"</p>"+i['value']+'<br><hr style="background-color:pink;height:1px; border:none;"/>'

        self.Ui.textEdit_cmd_result.setHtml(data)

    def generate_file_shell(self):
        url = self.Ui.lineEdit_file_url.text()
        dest_name = self.Ui.lineEdit_file_dest_name.text()
        sql = "select * from cmd where type ='file'"
        sql_result = self.sql_search(sql, 'dict')
        data = ''
        if sql_result:
            for i in sql_result:
                if url:
                    data += "<p style=\"color:green\">" + i['name'] + "</p>" + i['value'].replace('http://127.0.0.1/exp.exe',
                                                                                                  url).replace('exploit.exe',
                                                                                                              dest_name) + '<br><hr style="background-color:pink;height:1px; border:none;"/>'
                else:
                    data += "<p style=\"color:green\">" + i['name'] + "</p>" + i[
                        'value'] + '<br><hr style="background-color:pink;height:1px; border:none;"/>'

        self.Ui.textEdit_file_result.setHtml(data)
    def change_morenpasswd_click_value(self):
        itemname =self.Ui.listWidget_morenpasswd_list.selectedItems()[0].text()
        sql_poc = "SELECT distinct * from passwd where type ='"+itemname+"'"
        passwd_list = self.sql_search(sql_poc, 'dict')
        self.set_morenpasswd_table_value(passwd_list)
        # self.morenpasswd_get_name_passwd()
    def morenpasswd_start(self):
        type =self.Ui.lineEdit_select_data.text()
        sql_poc = "SELECT distinct * from passwd where type like '%" + type+ "%'"
        passwd_list = self.sql_search(sql_poc, 'dict')
        self.set_morenpasswd_table_value(passwd_list)
        # self.morenpasswd_get_name_passwd()
    def Clear_tableWidget(self, table_obj):
        for i in range(0, table_obj.rowCount()):  # 循环行
            table_obj.removeRow(0)
    def set_morenpasswd_table_value(self,passwd_list):
        self.Clear_tableWidget(self.Ui.tableWidget_morenpasswd_result)
        #排序先关闭再打开 防止为空
        # self.Ui.tableWidget_morenpasswd_result.setSortingEnabled(False)
        # self.Ui.tableWidget_morenpasswd_result.setVisible(False)

        for value in passwd_list:
            row = self.Ui.tableWidget_morenpasswd_result.rowCount()  # 获取行数
            self.Ui.tableWidget_morenpasswd_result.setRowCount(row + 1)
            passwd_id = QTableWidgetItem(value.get('id'))
            passwd_type = QTableWidgetItem(value.get("type"))
            passwd_name = QTableWidgetItem(value.get('name'))
            passwd_passwd = QTableWidgetItem(value.get('passwd'))
            self.Ui.tableWidget_morenpasswd_result.setItem(row, 0, passwd_id)
            self.Ui.tableWidget_morenpasswd_result.setItem(row, 1, passwd_type)
            self.Ui.tableWidget_morenpasswd_result.setItem(row, 2, passwd_name)
            self.Ui.tableWidget_morenpasswd_result.setItem(row, 3, passwd_passwd)
            # 自动调节列宽度
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(0)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(1)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(2)
        # self.Ui.tableWidget_morenpasswd_result.resizeColumnToContents(3)
        # self.Ui.tableWidget_morenpasswd_result.setVisible(True)
        # self.Ui.tableWidget_morenpasswd_result.setSortingEnabled(True)
    def sql_search(self, sql, type='list'):
        if type == 'dict':
            conn = sqlite3.connect(DB_NAME)
            conn.row_factory = self.dict_factory
        else:
            conn = sqlite3.connect(DB_NAME)
        # 创建一个游标 curson
        cursor = conn.cursor()
        # self.Ui.textEdit_log.append("[%s]Info:正在查询数据..."%(time.strftime('%H:%M:%S', time.localtime(time.time()))))
        # 列出所有数据
        cursor.execute(sql)
        if type in ["delete","update","insert"]:
            conn.commit()
            return True
        values = cursor.fetchall()
        return values
    # sql查询返回字典
    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    def Binary_gogogo(self, Binary_type):
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText()
            if len(text) <= 0:
                self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
                return 0
            else:
                text_list = self.get_text_list(text)
            for text in text_list:
                status,result_text,type__ = getattr(Class_Binary(), 'exec_Binary')(text, Binary_type.replace("->","_"))
                self.Ui.Result_text.appendPlainText(str(result_text))
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))
    def gogogo(self, func_name, class_name="Encode"):
        try:
            self.Ui.Result_text.clear()
            text = self.Ui.Source_text.toPlainText().strip()
            if len(text) <= 0:
                self.Ui.Result_text.appendPlainText('请输入一个源字符串！')
                return 0
            else:
                text_list = self.get_text_list(text)
            encode_type = self.Ui.encode_type.currentText()
            obj = eval('Class_' + class_name + '()')
            for text in text_list:
                status,result_text,type__ = getattr(obj, 'func_'+func_name)(encode_type, text)
                self.Ui.Result_text.appendPlainText(str(result_text))
        except Exception as e:
            self.Ui.Result_text.appendPlainText(str(e))

    def get_text_list(self, text):
        text_list = []
        if self.Ui.checkBox_line.isChecked():
            text_list = text.splitlines()
        else:
            text_list.append(text)
        return text_list

    def open_close_(self,flag):
        if  flag:
            self.hide()
            self.form2 = QtWidgets.QWidget()
            self.vuln_widget = Ui_Dialog()
            self.vuln_widget.setupUi(self.form2)
            # self.form2.setStyleSheet(qss_style)
            self.form2.move(self.x, self.y)  # 左上角点的坐标
            # self.form2.move(desktop.width()-200, desktop.height()-(desktop.height()-100))  # 左上角点的坐标
            self.form2.show()
            self.vuln_widget.label.clicked.connect(lambda: self.open_close_(0))
            self.vuln_widget.label.clicked_move.connect(self.label_clicked)

            # self.vuln_widget.pushButton.clicked.connect(lambda:self.open_close_(0))
        else:
            self.show()
            isMaximized = self.windowState() & QtCore.Qt.WindowMaximized
            if isMaximized:
                self.showMaximized()
            else:

                self.showNormal() #
            self.form2.close()
    def label_clicked(self,text):
        self.x=text[0]
        self.y=text[1]
        # print(text)
        self.form2.move(self.x,self.y)  # 左上角点的坐标

        # Dialog.show()
    def split_url(self):
        url = self.Ui.lineEdit.text()
        result = urlparse(url)
        self.Ui.lineEdit_2.setText(result.hostname)
        if result.port:
            self.Ui.lineEdit_3.setText(str(result.port))
        else:
            if result.scheme=="https":
                self.Ui.lineEdit_3.setText("443")
            else:
                self.Ui.lineEdit_3.setText("80")

    def load_settings(self):
        #得到所有标签
        # setting = config_setup.sections()
        #得到所有建
        setting_list = config_setup.options("Setting")


    def load_config(self):
        global config_setup
        # 实例化configParser对象
        config_setup = configparser.ConfigParser()
        # -read读取ini文件
        config_setup.read(config_file_dir, encoding='utf-8')
        app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5', palette=LightPalette()))
        # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def load_button(self):
        f=open("conf/data.json",encoding="utf-8")
        self.data = json.loads(f.read())
        f.close()
        column_num = config_setup.get("Setting","column_num")
        for tab_name in self.data.keys():
            tab = QtWidgets.QWidget()
            tab.setObjectName(tab_name)
            gridLayout_3 = QtWidgets.QGridLayout(tab)
            gridLayout_3.setObjectName("gridLayout_3")
            gridLayout = QtWidgets.QGridLayout()
            gridLayout.setObjectName("gridLayout_2")
            line_num=0
            col_num=0
            for i in self.data[tab_name].keys():
                if col_num >= int(column_num):
                    line_num+=1
                    col_num=0
                pushButton = QtWidgets.QPushButton(tab)
                pushButton.setObjectName(i)
                pushButton.setText(i)
                pushButton.clicked.connect(self.click_button)

                gridLayout.addWidget(pushButton, line_num, col_num, 1, 1)
                col_num+=1
            gridLayout_3.addLayout(gridLayout, 0, 0, 1, 1)
            spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
            gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
            self.Ui.tabWidget.addTab(tab, tab_name)

    def click_button(self):
        try:
            path = frozen_dir.app_path()
            url = self.Ui.lineEdit.text()
            ip = self.Ui.lineEdit_2.text()
            port = self.Ui.lineEdit_3.text()
            currentTab = self.Ui.tabWidget.currentWidget()
            # print(currentTab.objectName())
            button = self.sender()
            # print(button.text())
            # print(button.objectName)
            cmd = self.data[currentTab.objectName()][button.objectName()]
            if currentTab.objectName()=='命令速用':
                pyperclip.copy(cmd)
                # self.Ui.statusBar.showMessage("复制成功：" + cmd,5000)
            else:
                cmd = cmd.replace("{{url}}",url).replace("{{ip}}",ip).replace("{{port}}",port).replace("{{tools}}",path+'/tools/')
                # print(os.path.dirname(sys.executable))
                for i in  config_setup.options("Setting"):
                    cmd =cmd.replace("{{%s}}"%i,config_setup.get("Setting",i))
                cmd =cmd.replace('\\','\\\\')
                # print(cmd)
                # self.Ui.statusBar.showMessage("执行命令：" + cmd,5000)
                with open('log.log', 'a') as out:
                    out.write("\nshell:"+cmd+"  "+"log:")
                    subprocess.Popen(cmd,shell=True, stdout=out,stderr=out)
            # if 'start cmd' in cmd:
            #     subprocess.Popen(  cmd  , shell=True)
            # else:
            #     p = subprocess.Popen( cmd,shell=True,stderr=subprocess.PIPE)
            #     stdout, stderr = p.communicate(cmd)
            #
            #     if stderr :
            #         stdout = stderr
            #         box = QtWidgets.QMessageBox()
            #         box.warning(self, "提示","cmd:\n"+cmd+"\n\nError:\n"+stderr.decode())
            #     p.kill()
        except Exception as e:
            box = QtWidgets.QMessageBox()
            box.warning(self, "提示",str(e) + '----' + str(e.__traceback__.tb_lineno) + '行')
    ## 编码解码
    def add_Tab(self):
        self.Ui.tab = QWidget()
        self.Ui.tab.setObjectName(u"tab")
        self.Ui.gridLayout = QGridLayout(self.Ui.tab)
        self.Ui.gridLayout.setObjectName(u"gridLayout")
        self.Ui.verticalLayout = QVBoxLayout()
        self.Ui.verticalLayout.setObjectName(u"verticalLayout")
        # self.Ui.source_text = QLabel(self.Ui.tab)
        # self.Ui.source_text.setObjectName(u"source_text")
        # self.source_text.setMinimumSize(QSize(0, 30))
        # self.Ui.source_text.setStyleSheet(u"")

        # self.Ui.verticalLayout.addWidget(self.Ui.source_text)
        self.Ui.Source_text = QPlainTextEdit(self.Ui.tab)
        self.Ui.Source_text.setObjectName(u"Source_text")
        self.Ui.Source_text.setPlaceholderText('请在此处输入')

        self.Ui.verticalLayout.addWidget(self.Ui.Source_text)

        # self.Ui.result_text = QLabel(self.Ui.tab)
        # self.Ui.result_text.setObjectName(u"result_text")
        # self.result_text.setMinimumSize(QSize(0, 30))
        # self.Ui.result_text.setStyleSheet(u"")

        # self.Ui.verticalLayout.addWidget(self.Ui.result_text)

        self.Ui.Result_text = QPlainTextEdit(self.Ui.tab)
        self.Ui.Result_text.setObjectName(u"Result_text")
        self.Ui.Result_text.setPlaceholderText('结果会显示在此处')

        self.Ui.verticalLayout.addWidget(self.Ui.Result_text)
        # self.Ui.source_text.setText(QCoreApplication.translate("MainWindow", u"Source", None))
        # self.Ui.result_text.setText(QCoreApplication.translate("MainWindow", u"Result", None))
        self.Ui.gridLayout.addLayout(self.Ui.verticalLayout, 0, 0, 1, 1)
        lisra = ["梦媛", "涵钰", "妲可", "含钰", "连倩", "辰泽", "涵博", "海萍", "祖儿", "佳琪", "诗晗", "之言", "清妍", "淑媛", "智妍", "晴然",
                 "树静",
                 "娜娜", "瑞楠", "晓满", "婉雅", "雨婷", "筱满", "雅文", "玉琪", "敖雯", "文殊", "喻喧", "海英", "舒欣", "云亿", "莨静", "雅芝",
                 "蕴兵",
                 "乐乐", "之恋", "小满", "悦心", "可人", "忆初", "衬心", "诠释", "尘封", "奔赴", "心鸢", "晴栀", "堇年", "青柠", "埋葬", "夏墨",
                 "随风",
                 "屿暖", "深邃", "途往", "迷离", "槿城", "零落", "余笙", "梦呓", "墨凉", "晨曦", "纪年", "未央", "失语", "柠栀", "梦巷", "九离",
                 "暮雨",
                 "木兮", "浅歌", "沐北", "惜颜", "素笺", "锁心", "柠萌", "卿歌", "归期", "予别", "情笙", "缥缈", "轩辕", "浮光", "缠绵", "碧影",
                 "星愿",
                 "星月", "星雨", "沧澜", "醉月", "春媱", "夏露", "秋颜", "冬耀", "缱绻", "涟漪", "若溪", "微凉", "暖阳", "半夏", "崖悔", "洛尘",
                 "矜柔",
                 "绚烂", "矫情", "真淳", "明媚", "迷离", "隐忍", "灼热", "幻灭", "落拓", "锦瑟", "妖娆", "邪殇", "离殇", "恋夏", "梦琪", "忆柳",
                 "之桃",
                 "慕青", "问兰", "尔岚", "元香", "初夏", "沛菡", "傲珊", "曼文", "乐菱", "痴珊", "恨玉", "惜文", "香寒", "新柔", "语蓉", "海安",
                 "夜蓉",
                 "涵柏", "水桃", "醉蓝", "春儿", "语琴", "从彤", "傲晴", "语兰", "又菱", "碧彤", "元霜", "怜梦", "紫寒", "妙彤", "曼易", "南莲",
                 "紫翠",
                 "雨寒", "易烟", "如萱", "若南", "寻真", "晓亦", "向珊", "慕灵", "以蕊", "寻雁", "映易", "雪柳", "孤岚", "笑霜", "海云", "凝天",
                 "沛珊",
                 "寒云", "冰旋", "宛儿", "绿真", "盼儿", "晓霜", "碧凡", "夏菡", "若烟", "半梦", "雅绿", "冰蓝", "灵槐", "平安", "书翠", "翠风",
                 "香巧",
                 "代云", "梦曼", "幼翠", "友巧", "听寒", "梦柏", "醉易", "访旋", "亦玉", "凌萱", "访卉", "怀亦", "笑蓝", "春翠", "靖柏", "夜蕾",
                 "冰夏",
                 "梦松", "书雪", "乐枫", "念薇", "靖雁", "寻春", "恨山", "从寒", "忆香", "觅波", "静曼", "凡旋", "以亦", "念露", "芷蕾", "千兰",
                 "新波",
                 "代真", "新蕾", "雁玉", "冷卉", "紫山", "千琴", "恨天", "傲芙", "盼山", "怀蝶", "冰兰", "山柏", "翠萱", "恨松", "问旋", "从南",
                 "白易",
                 "问筠", "如霜", "半芹", "丹珍", "冰彤", "亦寒", "寒雁", "怜云", "寻文", "乐丹", "翠柔", "谷山", "之瑶", "冰露", "尔珍", "谷雪",
                 "乐萱",
                 "涵菡", "海莲", "傲蕾", "青槐", "冬儿", "易梦", "惜雪", "宛海", "之柔", "夏青", "亦瑶", "妙菡", "春竹", "痴梦", "紫蓝", "晓巧",
                 "幻柏",
                 "元风", "冰枫", "访蕊", "南春", "芷蕊", "凡蕾", "凡柔", "安蕾", "天荷", "含玉", "书兰", "雅琴", "书瑶", "春雁", "从安", "夏槐",
                 "念芹",
                 "怀萍", "代曼", "幻珊", "谷丝", "秋翠", "白晴", "海露", "代荷", "含玉", "书蕾", "听白", "访琴", "灵雁", "秋春", "雪青", "乐瑶",
                 "含烟",
                 "涵双", "平蝶", "雅蕊", "傲之", "灵薇", "绿春", "含蕾", "从梦", "从蓉", "初丹", "听兰", "听蓉", "语芙", "夏彤", "凌瑶", "忆翠",
                 "幻灵",
                 "怜菡", "紫南", "依珊", "妙竹", "访烟", "怜蕾", "映寒", "友绿", "冰萍", "惜霜", "凌香", "芷蕾", "雁卉", "迎梦", "元柏", "代萱",
                 "紫真",
                 "千青", "凌寒", "紫安", "寒安", "怀蕊", "秋荷", "涵雁", "以山", "凡梅", "盼曼", "翠彤", "谷冬", "新巧", "冷安", "千萍", "冰烟",
                 "雅阳",
                 "友绿", "南松", "诗云", "飞风", "寄灵", "书芹", "幼蓉", "以蓝", "笑寒", "忆寒", "秋烟", "芷巧", "水香", "映之", "醉波", "幻莲",
                 "夜山",
                 "芷卉", "向彤", "小玉", "幼南", "凡梦", "尔曼", "念波", "迎松", "青寒", "笑天", "涵蕾", "YYDS", "栓Q", "辣鸡CTF,毁我青春"]
        self.Ui.tabWidget_4.addTab(self.Ui.tab, random.choice(lisra))
        self.Ui.tabWidget_4.setCurrentIndex(self.Ui.tabWidget_4.count() - 1)
    def closeEvent(self, event):
        """
        重写closeEvent方法，实现dialog窗体关闭时执行一些代码
        :param event: close()触发的事件
        :return: None
        """
        reply = QtWidgets.QMessageBox.question(self,
                                               '本程序',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            config_setup.write(open(config_file_dir, "r+", encoding="utf-8"))  # r+模式
            event.accept()
        else:
            event.ignore()

    def changeEvent(self, event):
        if event.type() == QtCore.QEvent.WindowStateChange:
            if self.windowState() & QtCore.Qt.WindowMinimized:
                self.open_close_(1)
                # print('changeEvent: Minimised')
            elif event.oldState() & QtCore.Qt.WindowMinimized:
                # self.open_close_(0)
                pass
                # print('changeEvent: Normal/Maximised/FullScreen')
        else:
            QtWidgets.QWidget.changeEvent(self, event)
    def eventFilter(self, object, event):
        if object == self.Ui.tabWidget_4.tabBar():
            # if  event.type() in [QEvent.MouseButtonPress,  QEvent.MouseButtonRelease] :
            if event.type() in [QEvent.MouseButtonPress]:
                mouseEvent = QMouseEvent(event)
                if mouseEvent.buttons() == QtCore.Qt.RightButton:
                    self.add_Tab()
            elif event.type() == QtCore.QEvent.MouseButtonDblClick:
                # If image is double clicked, remove bar.
                self.add_Tab()
        return False
    def onCurrentChanged(self, ix):
        w = self.Ui.tabWidget_4.widget(ix)
        te = w.findChild(QPlainTextEdit, 'Source_text')
        re = w.findChild(QPlainTextEdit, 'Result_text')
        if te is not None:
            self.Ui.Source_text = te
            self.Ui.Result_text = re
            # print(te.toPlainText())
    def closeTab(self, currentIndex):
        if self.Ui.tabWidget_4.count() == 1:
            QMessageBox.information(self, '嘤嘤嘤', '最后一个Tab了，无法关闭！')
        else:
            self.Ui.tabWidget_4.removeTab(currentIndex)
    def paste(self, text):
        try:
            data = pyperclip.paste()
            if text == 'Source':
                # print(text)
                source_text = self.Ui.Source_text.toPlainText().strip()  #
                data = source_text + data
                self.Ui.Source_text.appendPlainText(data)
            if text == 'result':
                result_text = self.Ui.Result_text.toPlainText()  #
                data = result_text + data
                self.Ui.Result_text.appendPlainText(data)
        except Exception as e:
            # print(str(e))
            pass
    def Copy_text(self, data):
        try:
            # 访问剪切板，存入值
            pyperclip.copy(data)
        except Exception as e:
            pass

    def zhuan_yuanwenben(self):
        text = self.Ui.Result_text.toPlainText()
        if text:
            self.Ui.Source_text.setPlainText(text)
    # 导出扫描结果
    def export_file(self, table_obj, log_obj):
        data = []
        comdata = []
        if table_obj.rowCount()>0:
            for lll in range(0, table_obj.columnCount()):  # 循环列
                data.append(table_obj.horizontalHeaderItem(lll).text())  # 空格分隔
            comdata.append(list(data))
            data = []
            for i in range(0, table_obj.rowCount()):  # 循环行
                for j in range(0, table_obj.columnCount()):  # 循环列
                    if table_obj.item(i, j) != None:  # 有数据
                        data.append(table_obj.item(i, j).text())  # 空格分隔
                comdata.append(list(data))
                data = []
            if len(comdata) > 0:
                path = (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '.csv').replace(' ', '-').replace('-',
                                                                                                                 '').replace(
                    ':', '')
                # print(path)
                file_name = self.file_save(path)
                if file_name != "":
                    with open(file_name, 'w',encoding='utf-8',newline="") as f:
                        writer = csv.writer(f)
                        for row in comdata:
                            writer.writerow(row)
                    f.close()
                    box = QtWidgets.QMessageBox()
                    box.information(self, "Success", "导出成功！\n文件位置：" + file_name)
                    # self.Ui.statusBar.showMessage("Success", "导出成功！\n文件位置：" + file_name, 5000)
                else:
                    # box2= QtWidgets.QMessageBox()
                    # box2.warning(self, "Error", "保存失败！文件名错误！" )
                    pass
            else:
                try:
                    box = QtWidgets.QMessageBox()
                    box.warning(self, "提示", "表格无结果！")
                    if log_obj !='':
                        log_obj.append(
                        "[%s]Faile:没有结果！" % (time.strftime('%H:%M:%S', time.localtime(time.time()))))
                except:
                    pass
    # 保存文件对话框
    def file_save(self, filename):
        fileName, filetype = QFileDialog.getSaveFileName(self, (r"保存文件"), (filename), r"All files(*.*)")
        return fileName

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(150, 150)
        # Dialog.setMaximumSize(QtCore.QSize(100, 30))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        # self.pushButton = QtWidgets.QPushButton(Dialog)
        # self.pushButton.setMaximumSize(QtCore.QSize(50, 50))
        # self.pushButton.setObjectName("pushButton")
        # self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        # self.pushButton.setText("显示")
        self.label = MyLabel(Dialog)
        # self.label.clicked_move.connect(self.label_clicked)  # 线程发过来的信号挂接到槽函数update_sum
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.resize(150, 150)
        self.label.setStyleSheet('background:transparent;border-radius: 10px;border-style: outset;')
        self.label.setObjectName("label")
        pixmap = QPixmap()  # 按指定路径找到图片
        # pixmap.load('conf/logo.gif', "GIF")
        # self.label.setPixmap(pixmap)  # 在label上显示图片
        # self.label.setScaledContents(True)  # 让图片自适应label大小
        movie =  QMovie('conf/logo.gif')
        self.label.setMovie(movie)  # 在label上显示图片
        self.label.setScaledContents(True)  # 在label上显示图片
        movie.start();
        Dialog.setWindowTitle("Form")
        Dialog.setWindowFlags(Qt.FramelessWindowHint|Qt.WindowStaysOnTopHint|QtCore.Qt.SplashScreen)
        Dialog.setAttribute(Qt.WA_TranslucentBackground)  # 窗口透明


class MyLabel(QLabel):
    clicked_move = pyqtSignal(list)
    clicked = pyqtSignal(str)
    def __init__(self,parent=None):
        super(MyLabel, self).__init__(parent)
        self.txt = ''
    # 鼠标键按下时调用;
    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.clicked.emit(self.txt)
        elif  event.buttons() == QtCore.Qt.RightButton:
            pass
    #松开调用
    # def mousePressEvent(self, event):
    #     pass

    def mouseMoveEvent(self, e):
        # x = e.x()
        # y = e.y()
        pos = QCursor.pos()
        # print(str(pos.x())+":"+str(pos.y()))
        # text = "x: {0},  y: {1}".format(x, y)
        self.clicked_move.emit([pos.x(),pos.y()])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindows()
    translator = QTranslator()
    translator.load('./conf/qm/qt_zh_CN.qm') #改变中文菜单
    app.installTranslator(translator)
    translator_2 = QTranslator()
    translator_2.load('./conf/qm/widgets_zh_cn.qm') #改变QTextEdit右键为中文
    app.installTranslator(translator_2)
    window.show()
    sys.exit(app.exec_())
