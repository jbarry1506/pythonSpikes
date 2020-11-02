import pathlib
import os
import pysftp
import vars

home = os.path.expanduser("~")
print(home)


win_path = "C:\\Beast\\Pictures\\transfer\\"
lin_path = "/home/pi/Pictures/PiCam/"

try:
    # srv = pysftp.Connection(host="192.168.0.21", username=vars.user_name, password=vars.beast_xv)
    for f in os.walk(lin_path):
        if os.path.isfile(str(f)):
            print(f)
            print(type(f))
            f_str = str(f)
            lin_path_file = pathlib.Path(lin_path+f_str)
            print(lin_path_file)
        # lin_to_win = pathlib.WindowsPath(lin_path_file)
    #     srv.put(localpath=lin_path_file,remotepath=win_path_file)
except Exception as e:
    print("Connection issue")
    print(e)




# with pysftp.Connection(host, username=username, password=password) as sftp:
#     sftp.put(localpath, path)