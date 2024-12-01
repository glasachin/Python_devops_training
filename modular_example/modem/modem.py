from wifi import wifiObj
import utility

class Modem:
    def __init__(self):
        print('From Modem: ', wifiObj.a)
    
    def modemPrint(self):
        print('From Modem: ', wifiObj.b)
    
    def updateUtility(self):
        utility.a = 100