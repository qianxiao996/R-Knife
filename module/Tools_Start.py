import re
import socket,pypinyin
import struct
from PySide6.QtCore import QThread, Signal


class Tools_Start(QThread):
    """该线程用于计算耗时的累加操作"""
    _data = Signal(str)  # 信号类型 str
    def __init__(self,tools_source,tools_type,parent=None):
        super(Tools_Start,self).__init__(parent)
        self.tools_source = tools_source
        self.tools_type = tools_type


    def run(self):
        try:
            obj = getattr(self, self.tools_type, 0)
            if obj:
                obj()
            else:
                self._data.emit((self.tools_source))
            #ip归属地查询
        except Exception as e:
            self._data.emit(str(e))
            return
    def ipsearch(self):
        ip_list = list(filter(None, self.tools_source.splitlines()))
        cz = CzIp()
        self._data.emit((cz.get_version()+"纪录总数:"+str(cz.index_count)+"条\n"))
        for ip in ip_list:
            if ip and re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
            ip):
                result= ip+" "+(cz.get_addr_by_ip(ip))
            else:
                result = ip + " 不是IP"
            self._data.emit((result))
        self._data.emit(("查询完成"))
        return
    def alldaxie(self):
        result = self.tools_source.upper()
        self._data.emit((result))
        return
    def allxiaoxie(self):
        result = self.tools_source.lower()
        self._data.emit((result))
        return
    def daoxu(self):
        self._data.emit(self.tools_source[::-1])
        return
    def zhongwen_pinyin(self):
        s=''
        for i in pypinyin.pinyin(self.tools_source, style=pypinyin.NORMAL):
            s += ''.join(i)
        self._data.emit(s)
        return
    def tiqushouzimu(self):
        aaaa=''.join(pypinyin.lazy_pinyin(self.tools_source, style=pypinyin.Style.FIRST_LETTER))
        self._data.emit(aaaa)
        return
    def remove_duplicate(self):
        data = self.tools_source.splitlines()
        data  ='\n'.join(set(data))
        self._data.emit(data)
        return
    def get_ip(self):
        ip_list = list(filter(None, self.tools_source.splitlines()))
        result=''
        for ip in ip_list:
            if ip and re.match(
                    r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                    ip):
                result += ip+'\n'
        self._data.emit((result))
        return
    def get_china_ip(self):
        country = ["河北省","山西省" ,"辽宁省" ,"吉林省","黑龙省","江苏省" ,"浙江省" ,"安徽省" ,"福建省","江西省", "山东省", "河南省" ,"湖北省","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏","新疆","北京","天津","上海","重庆","香港","澳门"]
        ip_list = list(filter(None, self.tools_source.splitlines()))
        cz = CzIp()
        self._data.emit((cz.get_version()+"纪录总数:"+str(cz.index_count)+"条\n"))
        for ip in ip_list:
            if ip and re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
                for d in country:
                    if d  in (cz.get_addr_by_ip(ip)):
                        result=ip+" "+(cz.get_addr_by_ip(ip))
                        self._data.emit((result))
                        break
        self._data.emit(("提取完成"))
        return
    def remove_china_ip(self):
        country = ["河北省","山西省" ,"辽宁省" ,"吉林省","黑龙省","江苏省" ,"浙江省" ,"安徽省" ,"福建省","江西省", "山东省", "河南省" ,"湖北省","湖北","湖南","广东","海南","四川","贵州","云南","陕西","甘肃","青海","台湾","内蒙古","广西","西藏","宁夏","新疆","北京","天津","上海","重庆","香港","澳门"]
        all_ip_list=[]
        ip_list = list(filter(None, self.tools_source.splitlines()))
        cz = CzIp()
        self._data.emit((cz.get_version()+"纪录总数:"+str(cz.index_count)+"条\n"))
        for ip in ip_list:
            if ip and re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip):
                all_ip_list.append(ip)
                for d in country:
                    if d  in (cz.get_addr_by_ip(ip)):
                        all_ip_list.remove(ip)
                        break
        for i in all_ip_list:
            result = i + " " + (cz.get_addr_by_ip(i))
            self._data.emit(result)
        self._data.emit(("提取完成"))
        return

class CzIp:
    def __init__(self, db_file='Conf/qqwry.dat'):
        self.f_db = open(db_file, "rb")
        bs = self.f_db.read(8)
        (self.first_index, self.last_index) = struct.unpack('II', bs)
        self.index_count = int((self.last_index - self.first_index) / 7 + 1)
        self.cur_start_ip = None
        self.cur_end_ip_offset = None
        self.cur_end_ip = None
        # print(self.get_version(), " 纪录总数: %d 条 "%(self.index_count))

    def get_version(self):
        '''
        获取版本信息，最后一条IP记录 255.255.255.0-255.255.255.255 是版本信息
        :return: str
        '''
        s = self.get_addr_by_ip(0xffffff00)
        # print(s)
        return s

    def _get_area_addr(self, offset=0):
        if offset:
            self.f_db.seek(offset)
        bs = self.f_db.read(1)
        (byte,) = struct.unpack('B', bs)
        if byte == 0x01 or byte == 0x02:
            p = self.getLong3()
            if p:
                return self.get_offset_string(p)
            else:
                return ""
        else:
            self.f_db.seek(-1, 1)
            return self.get_offset_string(offset)

    def _get_addr(self, offset):
        '''
        获取offset处记录区地址信息(包含国家和地区)
        如果是中国ip，则是 "xx省xx市 xxxxx地区" 这样的形式
        (比如:"福建省 电信", "澳大利亚 墨尔本Goldenit有限公司")
        :param offset:
        :return:str
        '''
        self.f_db.seek(offset + 4)
        bs = self.f_db.read(1)
        (byte,) = struct.unpack('B', bs)
        if byte == 0x01:    # 重定向模式1
            country_offset = self.getLong3()
            self.f_db.seek(country_offset)
            bs = self.f_db.read(1)
            (b,) = struct.unpack('B', bs)
            if b == 0x02:
                country_addr = self.get_offset_string(self.getLong3())
                self.f_db.seek(country_offset + 4)
            else:
                country_addr = self.get_offset_string(country_offset)
            area_addr = self._get_area_addr()
        elif byte == 0x02:  # 重定向模式2
            country_addr = self.get_offset_string(self.getLong3())
            area_addr = self._get_area_addr(offset + 8)
        else:   # 字符串模式
            country_addr = self.get_offset_string(offset + 4)
            area_addr = self._get_area_addr()
        return country_addr + " " + area_addr

    def dump(self, first, last):
        '''
        打印数据库中索引为first到索引为last(不包含last)的记录
        :param first:
        :param last:
        :return:
        '''
        if last > self.index_count:
            last = self.index_count
        for index in range(first, last):
            offset = self.first_index + index * 7
            self.f_db.seek(offset)
            buf = self.f_db.read(7)
            (ip, of1, of2) = struct.unpack("IHB", buf)
            address = self._get_addr(of1 + (of2 << 16))
            print("%d %s %s" % (index, self.ip2str(ip), address))

    def _set_ip_range(self, index):
        offset = self.first_index + index * 7
        self.f_db.seek(offset)
        buf = self.f_db.read(7)
        (self.cur_start_ip, of1, of2) = struct.unpack("IHB", buf)
        self.cur_end_ip_offset = of1 + (of2 << 16)
        self.f_db.seek(self.cur_end_ip_offset)
        buf = self.f_db.read(4)
        (self.cur_end_ip,) = struct.unpack("I", buf)

    def get_addr_by_ip(self, ip):
        '''
        通过ip查找其地址
        :param ip: (int or str)
        :return: str
        '''
        if type(ip) == str:
            ip = self.str2ip(ip)
        L = 0
        R = self.index_count - 1
        while L < R - 1:
            M = int((L + R) / 2)
            self._set_ip_range(M)
            if ip == self.cur_start_ip:
                L = M
                break
            if ip > self.cur_start_ip:
                L = M
            else:
                R = M
        self._set_ip_range(L)
        # version information, 255.255.255.X, urgy but useful
        if ip & 0xffffff00 == 0xffffff00:
            self._set_ip_range(R)
        if self.cur_start_ip <= ip <= self.cur_end_ip:
            address = self._get_addr(self.cur_end_ip_offset)
        else:
            address = "未找到该IP的地址"
        return address

    def get_ip_range(self, ip):
        '''
        返回ip所在记录的IP段
        :param ip: ip(str or int)
        :return: str
        '''
        if type(ip) == str:
            ip = self.str2ip(ip)
        self.get_addr_by_ip(ip)
        range = self.ip2str(self.cur_start_ip) + ' - ' \
                + self.ip2str(self.cur_end_ip)
        return range

    def get_offset_string(self, offset=0):
        '''
        获取文件偏移处的字符串(以'\0'结尾)
        :param offset: 偏移
        :return: str
        '''
        if offset:
            self.f_db.seek(offset)
        bs = b''
        ch = self.f_db.read(1)
        (byte,) = struct.unpack('B', ch)
        while byte != 0:
            bs += ch
            ch = self.f_db.read(1)
            (byte,) = struct.unpack('B', ch)
        return bs.decode('gbk')

    def ip2str(self, ip):
        '''
        整数IP转化为IP字符串
        :param ip:
        :return:
        '''
        return str(ip >> 24) + '.' + str((ip >> 16) & 0xff) + '.' + str((ip >> 8) & 0xff) + '.' + str(ip & 0xff)

    def str2ip(self, s):
        '''
        IP字符串转换为整数IP
        :param s:
        :return:
        '''
        (ip,) = struct.unpack('I', socket.inet_aton(s))
        return ((ip >> 24) & 0xff) | ((ip & 0xff) << 24) | ((ip >> 8) & 0xff00) | ((ip & 0xff00) << 8)

    def getLong3(self, offset=0):
        '''
        3字节的数值
        :param offset:
        :return:
        '''
        if offset:
            self.f_db.seek(offset)
        bs = self.f_db.read(3)
        (a, b) = struct.unpack('HB', bs)
        return (b << 16) + a



# if __name__ == '__main__':
#     cz = CzIp()
#     # print(cz.get_version())
#     print(cz.get_version(), " 纪录总数: %d 条 "%(cz.index_count))
#     # print(cz.get_ip_range(ip))
#     print(cz.get_addr_by_ip('8.8.8.8'))