from PySide6.QtCore import QThread, Signal
import frozen_dir
import random
SETUP_DIR = frozen_dir.app_path()


class Phone(QThread):
    """该线程用于计算耗时的累加操作"""
    _data = Signal(str)  # 信号类型 str

    def __init__(self,all_haoduan,count,start_num,end_num,is_phone,parent=None):
        super(Phone, self).__init__(parent)
        self.all_haoduan =  all_haoduan
        self.start_num = start_num
        self.end_num = end_num
        self.is_phone =is_phone
        self.count =count
    def run(self):
        while self.count:
            a = random.choice(self.all_haoduan)
            for i in range(self.start_num,self.end_num):
                if self.count==0:
                    break
                else:
                    self.count -= 1
                aaa = a[0]+str(i).rjust(4,'0')
                if self.is_phone:
                    text =aaa
                else:
                    text =aaa+" "+a[1]+a[2]+" "+a[3]
                self._data.emit(text)
        self._data.emit("end")

    def is_id_card(self,id):
        sum = 0
        for index, item in enumerate(id[:-1]):
            sum += 2 ** (17 - index) % 11 * int(item)
        num = (12 - sum % 11) % 11
        if num < 10:
            return  id[:17]+str(num)
        else:
            return  id[:17]+"X"

            # return '校验通过' if id[-1] == str(num) else f'校验失败，正确尾号应为：{num}'
        # else:
        #     return '校验通过' if id[-1] == 'X' else f'校验失败，正确尾号应为：{num}'

