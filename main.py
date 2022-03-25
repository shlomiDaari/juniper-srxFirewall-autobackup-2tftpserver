import paramiko
import datetime
import time
import os


#get time stamp
ct = datetime.datetime.now() #ct stores current time
TIME_STAMP = f'{ct.year}-{ct.month}-{ct.day}'

#Variables SRX Juniper
ip = os.environ.get('SRX_IP')
username = os.environ.get('SRX_USERNAME')
password = os.environ.get('SRX_PASSWORD')
#Variables ftp/tftp server
FTP_USERNAME = os.environ.get('FTP_GESTIOIP_USERNAME')
FTP_PASSWORD = os.environ.get('FTP_GESTIOIP_PASSWORD')
FTP_IP = os.environ.get('FTP_IP')
#ftp path
path = f'//srv/ftp/juniperBackUpUsingPython_{TIME_STAMP}_.conf.gz'
#the Juniper SRX command
command = f'file copy /config/juniper.conf.gz ftp://{FTP_USERNAME}:{FTP_PASSWORD}@{FTP_IP}{path}'.encode('ascii')
print(command)


SESSION = paramiko.SSHClient()  # create the session
SESSION.set_missing_host_key_policy(paramiko.AutoAddPolicy())
SESSION.connect(ip,port=22,username=username,password=password,look_for_keys=False,allow_agent=False) #crate the ssh connection


DEVICE_ACCESS = SESSION.invoke_shell()
# DEVICE_ACCESS.send(b'term length 0\n')
DEVICE_ACCESS.send(b'pwd\n')
DEVICE_ACCESS.send(b'cli\n')
time.sleep(5)
DEVICE_ACCESS.send(command + b'\n')
time.sleep(2)


time.sleep(5)
output = DEVICE_ACCESS.recv(65000)
print(output.decode('ascii'))

SESSION.close()


