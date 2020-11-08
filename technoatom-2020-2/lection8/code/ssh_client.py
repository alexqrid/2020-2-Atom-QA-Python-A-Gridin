import paramiko
ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.1.144', port=2222, key_filename='/Users/y.cherednichenko/.ssh/id_rsa')

stdin, stdout, stderr = ssh.exec_command('date')
print(stdout.readlines())
ssh.close()