# from gpios import gpioObj
import asyncio

class MainApp:
    def __init__(self):
        self.netConnected_ = False
        self.wdtPulsePin_ = 'SCIF4'
        self.wdtResetInfoPin_ = 'IRQ'
       

    async def genPulse(self):
        # This task generate Pulse 
        while True:
            print('pulse is generating')
            await asyncio.sleep(1)


    async def checkInternet(self):
        # This task checks for internet connectivity
        while True:
            print('checkInternet is running')
            await asyncio.sleep(1)

    async def startMainApp(self):
        asyncio.create_task(self.genPulse())
        asyncio.create_task(self.checkInternet())
        while True:
            print('app running')
            await asyncio.sleep(1)
        