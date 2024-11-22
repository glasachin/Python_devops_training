from wifi import wifiObj


class Modem:
    def __init__(self):
        print('From Modem: ', wifiObj.a)
    
    def modemPrint(self):
        print('From Modem: ', wifiObj.b)