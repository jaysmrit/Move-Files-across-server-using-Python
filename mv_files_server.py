import paramiko
def cred_path(host_name,username,pwd,read_path,write_path):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  #Provide the host name from which the file need to be read
  ssh.connect(hostname ='host_name', user_name ='username',password ='pwd',port = 22)
  sftp_client = ssh.open_sftp()

  sftp_client.get('read_path','write_path')

  sftp_client.close()
  ssh.close()
