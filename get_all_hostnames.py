import os
import _socket

for addr in range(33,101):
    try:
        my_host = _socket.gethostbyaddr("192.168.0."+str(addr))
        print(my_host)
    except Exception as e:
        print(str(addr)+" not windows")
        try:
            my_host = os.uname("192.168.0."+str(addr))
        except Exception as e:
            print(e)
            print(str(addr)+" is not used")
