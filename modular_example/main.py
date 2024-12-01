from modem import modemObj
from wifi import wifiObj
from pathlib import Path
from wifi import WiFi
from app import appObj
import asyncio
import utility

if __name__ == '__main__':
    wifi_obj = WiFi()
    print('From Main: ', wifiObj.a)
    print('From Main: ', wifiObj.b)
    wifiObj.inc_b()
    print('From Main: ', wifiObj.b)
    modemObj.modemPrint()
    print('From Main: ', wifi_obj.b)
    wifiObj.path()

    print('Global Variable: ', utility.a)
    modemObj.updateUtility()
    print('Global Variable: ', utility.a)
    utility.appPath = str(Path(__file__).parents)
    print('App Path: ', utility.appPath)

    asyncio.run(appObj.startMainApp())