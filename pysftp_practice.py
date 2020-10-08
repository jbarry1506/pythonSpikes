#import mysql.connector

#print('hello from connection test')

#mydb = mysql.connector.connect(
#    host="192.168.0.33",
#    user="pi",
#    passwd=
#)

#print(mydb)
#-----------------------------------------------------------

# test using tilde for home directory
from os import path
from os.path import expanduser
import vars

home = expanduser("~")
pic_directory = home+'/Pictures'
print("File exists:" + str(path.exists(pic_directory)))

#----------------------------------------------------------
# test file transfer
import pysftp

server_pic_dir = "/home/jbarry1506/Pictures/"
pi_pic_dir = "/home/pi/Pictures/"
srv = pysftp.Connection(host="192.168.0.33", username=vars.user_name, password=vars.email_pw)
data = srv.listdir()
test_vid_file = "2019_9_7_20_18_50.h264"
try:
    print(pi_pic_dir+test_vid_file)
    print(server_pic_dir)
    srv.put( pi_pic_dir+test_vid_file, server_pic_dir+test_vid_file )
except Exception as e:
    print(str(e))
    print("The file was not transferred successfully")

srv.close()

#for i in data:
#    print(i)