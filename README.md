PLEASE CHANGE THE FOLLOWING IN YOUR Environment Variables on Windows

please follow the instraction in the link below:
https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html

****REMEMBER to use the same name os.environ.get('SRX_USERNAME') like SRX_USERNAME in both Environment Variables and the code. *******
The reason for that is to keep your credential safe. 




ip = os.environ.get('SRX_IP')
username = os.environ.get('SRX_USERNAME')
password = os.environ.get('SRX_PASSWORD')
#Variables ftp/tftp server
FTP_USERNAME = os.environ.get('FTP_GESTIOIP_USERNAME')
FTP_PASSWORD = os.environ.get('FTP_GESTIOIP_PASSWORD')
FTP_IP = os.environ.get('FTP_IP')
