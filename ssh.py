import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('10.11.27.3', port =22, username='un' , password='xxxx')
stdin,stdout,stderr = ssh.exec_command('show ip int brie')
output=stdout.readlines()
# type(output)
print('\n'.join(output))





