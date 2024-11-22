from pathlib import Path
import os

class WiFi:
    def __init__(self):
        self.a = 0
        self.b = 120

    def inc_b(self):
        self.b += 100
    
    def path(self):
        os.system('pwd')
        print('wifi: ', os.getcwd())
        print('wifi: ', Path(__file__).cwd())
        print('wifi: ', Path(__file__).parent.resolve())