from multiprocessing.connection import Listener
import json

listen_add_ = ('127.0.0.1', 8002)
pass_key_ = 'kimbalNilm'
mqtt_listener_ = Listener(listen_add_, authkey=pass_key_.encode())

mqtt_conn = mqtt_listener_.accept()
while True:
    rcvd_msg = mqtt_conn.recv()
    if rcvd_msg != 'close':
        rcvd_msg = json.loads(rcvd_msg)
        print(rcvd_msg)
        # vars.publishMsgQueue.enqueue(rcvd_msg)
        # var.ALERT_RESPONSE_QUEUE.append(rcvd_msg)
    elif rcvd_msg == 'close':
        mqtt_conn.close()