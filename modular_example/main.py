from modem import modemObj
from wifi import wifiObj

from wifi import WiFi

if __name__ == '__main__':
    wifi_obj = WiFi()
    print('From Main: ', wifiObj.a)
    print('From Main: ', wifiObj.b)
    wifiObj.inc_b()
    print('From Main: ', wifiObj.b)
    modemObj.modemPrint()
    print('From Main: ', wifi_obj.b)
    wifiObj.path()