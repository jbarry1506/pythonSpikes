import pathlib
import os
import pysftp
import vars
from smb.SMBConnection import SMBConnection

# https://pysmb.readthedocs.io/en/latest/api/smb_SMBConnection.html#smb.SMBConnection.SMBConnection
# https://gist.github.com/joselitosn/e74dbc2812c6479d3678
# https://www.computerhope.com/issues/ch000535.htm

userID = vars.beast_un
password = vars.beast_xv
client_machine_name = 'pi3web'

server_name = vars.beast_hostname
server_ip = vars.beast_ip

domain_name = ''


conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
conn.connect(vars.beast_ip, port=445)

win_path = "C:\\Users\\Beast\\Pictures\\transfer\\"
lin_path = "/home/pi/Pictures/PiCam/"

try:
    # srv = pysftp.Connection(host="192.168.0.21", username=vars.user_name, password=vars.beast_xv)
    for f in os.walk(lin_path):
        for fil in f[2]:
            lin_path_file = pathlib.Path(lin_path+fil)
            print(lin_path_file)
            with open(lin_path_file, 'r') as transfer_file:
                conn.storeFile('beast_pictures',win_path+fil, transfer_file, timeout=30)
                transfer_file.close()
        # lin_to_win = pathlib.WindowsPath(lin_path_file)
    #     srv.put(localpath=lin_path_file,remotepath=win_path_file)
except Exception as e:
    print("Connection issue")
    print(e)

conn.close()


# with pysftp.Connection(host, username=username, password=password) as sftp:
#     sftp.put(localpath, path)
