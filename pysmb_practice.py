from smb.SMBConnection import SMBConnection
import pprint
import vars

userID = vars.beast_un
password = vars.beast_xv
client_machine_name = 'pi3web'

server_name = vars.beast_hostname
server_ip = vars.beast_ip

domain_name = ''


conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True, is_direct_tcp=True)
conn.connect(vars.beast_ip, port=445)
pprint.pprint(conn)
# file2transfer = open(filename, "r")
# conn.storeFile(share, path+filename, file2transfer, timeout=30)
