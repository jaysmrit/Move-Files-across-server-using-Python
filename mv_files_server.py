import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname ='host_name', user_name ='username',password ='pwd',port = 22)
sftp_client = ssh.open_sftp()

sftp_client.get('read_path','write_path')

sftp_client.close()
ssh.close()
