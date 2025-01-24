from multiprocessing.connection import Client
import json
# import common.system_variables as sv

# def sendToMqttApp(data=''):
mqttAppPublishData = {
                'dev_type' : 'daq0',
                'dev_id' : '0',
                'command' : 1,
            }
try:
    
    address = ('127.0.0.1', 8002)
    conn = Client(address, authkey='kimbalNilm'.encode())
    conn.send(json.dumps(mqttAppPublishData))
    conn.send('close')
    conn.close()
except Exception as e:
    print('Error: sendToMqttApp ==> ', e)
