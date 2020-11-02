import pysmb
import vars


conn = SMBConnection(user=vars.beast_un, pw=vars.beast_xv, my_name="pi3web", srv, use_ntlm_v2=True)
conn.connect(ip, port=139)
file2transfer = open(filename, "r")
conn.storeFile(share, path+filename, file2transfer, timeout=30)
