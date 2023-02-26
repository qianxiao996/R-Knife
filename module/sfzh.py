from PyQt5.QtCore import QThread, pyqtSignal
import frozen_dir
import random
SETUP_DIR = frozen_dir.app_path()


class SFZH(QThread):
    """该线程用于计算耗时的累加操作"""
    _data = pyqtSignal(str)  # 信号类型 str

    def __init__(self,province_city_area_list,sexstring,year_list,month_day_list,is_sfzh,count,parent=None):
        super(SFZH, self).__init__(parent)
        self.province_city_area_list =  province_city_area_list
        self.sexstring = sexstring
        self.year_list = year_list
        self.month_day_list = month_day_list
        self.is_sfzh =is_sfzh
        self.count =count
    def run(self):
        paichusuo_daima = []
        for i in range(100):
            paichusuo_daima.append(str(i).rjust(2,'0'))
        while self.count:
            self.count -=1
            a = random.choice(self.province_city_area_list)
            b = random.choice(self.year_list)
            c = random.choice(self.month_day_list)

            d = random.choice(paichusuo_daima)
            e =  random.choice(list(self.sexstring))
            if int(e)%2==0:
                sex_c = "女"
            else:
                sex_c="男"
            sfzh = str(a[0])+str(b)+str(c)+str(d)+str(e)+'1'
            sfzh = self.is_id_card(sfzh)
            if self.is_sfzh:
                text =sfzh
            else:
                text =sfzh+" "+a[1]+" "+b+"年"+c[:2]+"月"+c[2:]+"日 性别:"+sex_c
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

